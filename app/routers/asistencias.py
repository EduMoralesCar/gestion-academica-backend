from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
import uuid
from typing import List

from .. import models, schemas, auth, database

router = APIRouter(
    prefix="/api/asistencias",
    tags=["Asistencias"]
)

@router.get("/", response_model=List[schemas.AsistenciaResponse])
def obtener_asistencias(db: Session = Depends(database.get_db), current_user: models.User = Depends(auth.get_current_user)):
    if current_user.rol == models.UserRole.ADMIN:
        return db.query(models.Asistencia).all()
    elif current_user.rol == models.UserRole.DOCENTE:
        cursos_ids = [c.curso_id for c in current_user.asignaciones_docente]
        return db.query(models.Asistencia).filter(models.Asistencia.curso_id.in_(cursos_ids)).all()
    else:
        return db.query(models.Asistencia).filter(models.Asistencia.estudiante_id == current_user.id).all()

@router.post("/", response_model=schemas.AsistenciaResponse)
def registrar_asistencia(asistencia: schemas.AsistenciaBase, db: Session = Depends(database.get_db), current_user: models.User = Depends(auth.get_current_user)):
    if current_user.rol != models.UserRole.DOCENTE and current_user.rol != models.UserRole.ADMIN:
        raise HTTPException(status_code=403, detail="Solo los docentes pueden registrar asistencia")
        
    nueva_asistencia = models.Asistencia(
        id=str(uuid.uuid4()),
        curso_id=asistencia.curso_id,
        estudiante_id=asistencia.estudiante_id,
        fecha=asistencia.fecha,
        estado=asistencia.estado
    )
    db.add(nueva_asistencia)
    db.commit()
    db.refresh(nueva_asistencia)
    return nueva_asistencia
