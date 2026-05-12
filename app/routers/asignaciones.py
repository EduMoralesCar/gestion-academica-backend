from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
import uuid
from typing import List

from .. import models, schemas, auth, database

router = APIRouter(
    prefix="/api/asignaciones",
    tags=["Asignaciones Docente"]
)

@router.get("/", response_model=List[schemas.AsignacionDocenteResponse])
def obtener_asignaciones(db: Session = Depends(database.get_db), current_user: models.User = Depends(auth.get_current_user)):
    return db.query(models.AsignacionDocente).all()

@router.post("/", response_model=schemas.AsignacionDocenteResponse)
def asignar_docente(asignacion: schemas.AsignacionDocenteCreate, db: Session = Depends(database.get_db), current_user: models.User = Depends(auth.get_current_user)):
    if current_user.rol != models.UserRole.ADMIN:
        raise HTTPException(status_code=403, detail="Solo los administradores pueden asignar docentes a cursos")
        
    nueva_asignacion = models.AsignacionDocente(
        id=str(uuid.uuid4()),
        docente_id=asignacion.docente_id,
        curso_id=asignacion.curso_id
    )
    db.add(nueva_asignacion)
    db.commit()
    db.refresh(nueva_asignacion)
    return nueva_asignacion

@router.put("/{asignacion_id}", response_model=schemas.AsignacionDocenteResponse)
def actualizar_asignacion(asignacion_id: str, asignacion: schemas.AsignacionDocenteCreate, db: Session = Depends(database.get_db), current_user: models.User = Depends(auth.get_current_user)):
    if current_user.rol != models.UserRole.ADMIN:
        raise HTTPException(status_code=403, detail="Solo los administradores pueden actualizar asignaciones")
        
    db_asignacion = db.query(models.AsignacionDocente).filter(models.AsignacionDocente.id == asignacion_id).first()
    if not db_asignacion:
        raise HTTPException(status_code=404, detail="Asignación no encontrada")
        
    db_asignacion.docente_id = asignacion.docente_id
    db_asignacion.curso_id = asignacion.curso_id
    
    db.commit()
    db.refresh(db_asignacion)
    return db_asignacion
