from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from datetime import datetime, timedelta, timezone
import uuid
import os
import secrets

from .. import models, schemas, auth, database, email_service

router = APIRouter(
    prefix="/api/auth",
    tags=["Autenticación"]
)

RESET_CODE_EXPIRE_MINUTES = int(os.getenv("RESET_CODE_EXPIRE_MINUTES", 10))
PASSWORD_RESET_GENERIC_MESSAGE = "Si el correo existe, enviaremos un codigo de recuperacion"


def _utc_now():
    return datetime.now(timezone.utc)


def _is_expired(fecha_expiracion: datetime, now: datetime) -> bool:
    if fecha_expiracion.tzinfo is None:
        fecha_expiracion = fecha_expiracion.replace(tzinfo=timezone.utc)
    return fecha_expiracion < now

@router.post("/registro", response_model=schemas.UserResponse)
def registrar_usuario(user: schemas.UserCreate, db: Session = Depends(database.get_db)):
    # Verificar si el email ya existe
    db_user = db.query(models.User).filter(models.User.email == user.email).first()
    if db_user:
        raise HTTPException(status_code=400, detail="Email ya registrado")
    
    # Hashear contraseña y crear usuario
    hashed_password = auth.get_password_hash(user.password)
    nuevo_usuario = models.User(
        id=str(uuid.uuid4()),
        email=user.email,
        hashed_password=hashed_password,
        nombre=user.nombre,
        apellido=user.apellido,
        rol=user.rol,
        codigo=user.codigo,
        carrera=user.carrera,
        ciclo=user.ciclo,
        especialidad=user.especialidad,
        departamento=user.departamento,
        nivel_acceso=user.nivel_acceso
    )
    db.add(nuevo_usuario)
    db.commit()
    db.refresh(nuevo_usuario)
    return nuevo_usuario

@router.post("/login", response_model=schemas.Token)
def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(database.get_db)):
    # Buscar usuario por email (OAuth2PasswordRequestForm usa 'username' por defecto, le pasaremos el email ahí)
    user = db.query(models.User).filter(models.User.email == form_data.username).first()
    
    # Verificar usuario y contraseña
    if not user or not auth.verify_password(form_data.password, user.hashed_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Email o contraseña incorrectos",
            headers={"WWW-Authenticate": "Bearer"},
        )
    
    # Generar Token JWT
    access_token_expires = timedelta(minutes=auth.ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = auth.create_access_token(
        data={"sub": user.email},
        expires_delta=access_token_expires
    )
    
    return {
        "access_token": access_token, 
        "token_type": "bearer",
        "user": user
    }

@router.get("/me", response_model=schemas.UserResponse)
def obtener_perfil(current_user: models.User = Depends(auth.get_current_user)):
    # Este endpoint está protegido. Solo funciona si envías un Token válido.
    return current_user

@router.put("/change-password", response_model=schemas.PasswordResetMessage)
def cambiar_password_perfil(
    request: schemas.ChangePasswordRequest,
    db: Session = Depends(database.get_db),
    current_user: models.User = Depends(auth.get_current_user)
):
    if not auth.verify_password(request.contrasenia_actual, current_user.hashed_password):
        raise HTTPException(status_code=400, detail="La contrasenia actual es incorrecta")

    if auth.verify_password(request.nueva_contrasenia, current_user.hashed_password):
        raise HTTPException(status_code=400, detail="La nueva contrasenia debe ser diferente a la actual")

    current_user.hashed_password = auth.get_password_hash(request.nueva_contrasenia)
    db.commit()
    return {"message": "Contrasena actualizada correctamente"}

@router.post("/forgot-password", response_model=schemas.PasswordResetMessage)
def solicitar_recuperacion_password(request: schemas.ForgotPasswordRequest, db: Session = Depends(database.get_db)):
    user = db.query(models.User).filter(models.User.email == request.email).first()
    if not user:
        return {"message": PASSWORD_RESET_GENERIC_MESSAGE}

    codigo = f"{secrets.randbelow(1000000):06d}"
    codigo_hash = auth.get_password_hash(codigo)
    fecha_expiracion = _utc_now() + timedelta(minutes=RESET_CODE_EXPIRE_MINUTES)

    db.query(models.CodigoRecuperacionContrasena).filter(
        models.CodigoRecuperacionContrasena.usuario_id == user.id,
        models.CodigoRecuperacionContrasena.estado == "ACTIVO"
    ).update({"estado": "INVALIDADO"}, synchronize_session=False)

    codigo_recuperacion = models.CodigoRecuperacionContrasena(
        id=str(uuid.uuid4()),
        usuario_id=user.id,
        codigo_hash=codigo_hash,
        fecha_expiracion=fecha_expiracion
    )
    db.add(codigo_recuperacion)
    db.commit()

    try:
        email_service.send_password_reset_code(user.email, codigo, user.nombre)
    except Exception:
        codigo_recuperacion.estado = "ERROR_ENVIO"
        db.commit()
        raise HTTPException(status_code=500, detail="No se pudo enviar el correo de recuperacion")

    return {"message": PASSWORD_RESET_GENERIC_MESSAGE}

@router.post("/reset-password", response_model=schemas.PasswordResetMessage)
def restablecer_password(request: schemas.ResetPasswordRequest, db: Session = Depends(database.get_db)):
    user = db.query(models.User).filter(models.User.email == request.email).first()
    if not user:
        raise HTTPException(status_code=400, detail="Codigo invalido o expirado")

    now = _utc_now()
    codigos_activos = db.query(models.CodigoRecuperacionContrasena).filter(
        models.CodigoRecuperacionContrasena.usuario_id == user.id,
        models.CodigoRecuperacionContrasena.estado == "ACTIVO"
    ).order_by(models.CodigoRecuperacionContrasena.fecha_creacion.desc()).all()

    for codigo_recuperacion in codigos_activos:
        if _is_expired(codigo_recuperacion.fecha_expiracion, now):
            codigo_recuperacion.estado = "EXPIRADO"
            continue

        if auth.verify_password(request.codigo, codigo_recuperacion.codigo_hash):
            user.hashed_password = auth.get_password_hash(request.nueva_contrasenia)
            codigo_recuperacion.estado = "USADO"
            codigo_recuperacion.fecha_uso = now
            db.commit()
            return {"message": "Contrasena actualizada correctamente"}

    db.commit()
    raise HTTPException(status_code=400, detail="Codigo invalido o expirado")
