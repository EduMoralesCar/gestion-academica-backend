from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from .. import models, schemas, auth, database

router = APIRouter(
    prefix="/api/usuarios",
    tags=["Usuarios"]
)

@router.get("/", response_model=List[schemas.UserResponse])
def obtener_usuarios(db: Session = Depends(database.get_db), current_user: models.User = Depends(auth.get_current_user)):
    # Solo el Admin o Docentes pueden ver la lista general de usuarios
    if current_user.rol not in [models.UserRole.ADMIN, models.UserRole.DOCENTE]:
        raise HTTPException(status_code=403, detail="No tienes permisos para ver los usuarios")
    
    usuarios = db.query(models.User).all()
    return usuarios

@router.put("/{user_id}", response_model=schemas.UserResponse)
def actualizar_usuario(user_id: str, user: schemas.UserBase, db: Session = Depends(database.get_db), current_user: models.User = Depends(auth.get_current_user)):
    if current_user.rol != models.UserRole.ADMIN:
        raise HTTPException(status_code=403, detail="Solo los administradores pueden actualizar usuarios")
        
    db_user = db.query(models.User).filter(models.User.id == user_id).first()
    if not db_user:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
        
    db_user.email = user.email
    db_user.nombre = user.nombre
    db_user.apellido = user.apellido
    db_user.rol = user.rol
    db_user.codigo = user.codigo
    db_user.carrera = user.carrera
    db_user.ciclo = user.ciclo
    db_user.especialidad = user.especialidad
    db_user.departamento = user.departamento
    db_user.nivel_acceso = user.nivel_acceso
    
    db.commit()
    db.refresh(db_user)
    return db_user

@router.delete("/{user_id}", status_code=204)
def eliminar_usuario(user_id: str, db: Session = Depends(database.get_db), current_user: models.User = Depends(auth.get_current_user)):
    if current_user.rol != models.UserRole.ADMIN:
        raise HTTPException(status_code=403, detail="Solo los administradores pueden eliminar usuarios")
        
    db_user = db.query(models.User).filter(models.User.id == user_id).first()
    if not db_user:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
        
    db.delete(db_user)
    db.commit()
    return None
