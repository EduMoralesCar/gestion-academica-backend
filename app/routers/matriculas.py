from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
import uuid
from typing import List

from .. import models, schemas, auth, database

router = APIRouter(
    prefix="/api/matriculas",
    tags=["Matrículas"]
)

@router.get("/", response_model=List[schemas.MatriculaResponse])
def obtener_matriculas(db: Session = Depends(database.get_db), current_user: models.User = Depends(auth.get_current_user)):
    """Obtener todas las matrículas (solo admin)"""
    if current_user.rol != models.UserRole.ADMIN:
        raise HTTPException(status_code=403, detail="Solo administradores pueden ver todas las matrículas")
    return db.query(models.Matricula).all()

@router.post("/", response_model=schemas.MatriculaResponse)
def crear_matricula(matricula: schemas.MatriculaCreate, db: Session = Depends(database.get_db), current_user: models.User = Depends(auth.get_current_user)):
    """Crear una nueva matrícula (solo admin)"""
    if current_user.rol != models.UserRole.ADMIN:
        raise HTTPException(status_code=403, detail="Solo los administradores pueden crear matrículas")
    
    nueva_matricula = models.Matricula(
        id=str(uuid.uuid4()),
        estudiante_id=matricula.estudiante_id,
        curso_id=matricula.curso_id
    )
    db.add(nueva_matricula)
    db.commit()
    db.refresh(nueva_matricula)
    return nueva_matricula

@router.put("/{matricula_id}", response_model=schemas.MatriculaResponse)
def actualizar_matricula(matricula_id: str, matricula: schemas.MatriculaCreate, db: Session = Depends(database.get_db), current_user: models.User = Depends(auth.get_current_user)):
    """Actualizar una matrícula (cambiar estado, etc)"""
    if current_user.rol != models.UserRole.ADMIN:
        raise HTTPException(status_code=403, detail="Solo administradores pueden actualizar matrículas")
    
    db_matricula = db.query(models.Matricula).filter(models.Matricula.id == matricula_id).first()
    if not db_matricula:
        raise HTTPException(status_code=404, detail="Matrícula no encontrada")
    
    db_matricula.estudiante_id = matricula.estudiante_id
    db_matricula.curso_id = matricula.curso_id
    
    db.commit()
    db.refresh(db_matricula)
    return db_matricula

@router.delete("/{matricula_id}", status_code=status.HTTP_204_NO_CONTENT)
def eliminar_matricula(matricula_id: str, db: Session = Depends(database.get_db), current_user: models.User = Depends(auth.get_current_user)):
    """Eliminar una matrícula"""
    if current_user.rol != models.UserRole.ADMIN:
        raise HTTPException(status_code=403, detail="Solo administradores pueden eliminar matrículas")
    
    db_matricula = db.query(models.Matricula).filter(models.Matricula.id == matricula_id).first()
    if not db_matricula:
        raise HTTPException(status_code=404, detail="Matrícula no encontrada")
    
    db.delete(db_matricula)
    db.commit()
    return None