from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from datetime import timedelta
import uuid

from .. import models, schemas, auth, database

router = APIRouter(
    prefix="/api/auth",
    tags=["Autenticación"]
)

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
