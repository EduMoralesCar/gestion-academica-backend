from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from .. import models, schemas, auth, database
from ..services import matriculas as matriculas_service

router = APIRouter(
    prefix="/api/matriculas",
    tags=["Matriculas"]
)

@router.get("/", response_model=List[schemas.MatriculaResponse])
def obtener_matriculas(db: Session = Depends(database.get_db), current_user: models.User = Depends(auth.get_current_user)):
    return db.query(models.Matricula).all()

@router.post("/", response_model=schemas.MatriculaResponse)
def matricular_estudiante(matricula: schemas.MatriculaCreate, db: Session = Depends(database.get_db), current_user: models.User = Depends(auth.get_current_user)):
    if current_user.rol != models.UserRole.ADMIN:
        raise HTTPException(status_code=403, detail="Solo los administradores pueden matricular estudiantes")
        
    return matriculas_service.crear_matricula(db, matricula.estudiante_id, matricula.curso_id)

@router.put("/{matricula_id}", response_model=schemas.MatriculaResponse)
def actualizar_matricula(matricula_id: str, matricula: schemas.MatriculaCreate, db: Session = Depends(database.get_db), current_user: models.User = Depends(auth.get_current_user)):
    if current_user.rol != models.UserRole.ADMIN:
        raise HTTPException(status_code=403, detail="Solo los administradores pueden actualizar matrículas")
        
    db_matricula = db.query(models.Matricula).filter(models.Matricula.id == matricula_id).first()
    if not db_matricula:
        raise HTTPException(status_code=404, detail="Matrícula no encontrada")
        
    db_matricula.estudiante_id = matricula.estudiante_id
    db_matricula.curso_id = matricula.curso_id
    
    db.commit()
    db.refresh(db_matricula)
    return db_matricula
