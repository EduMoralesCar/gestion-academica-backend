from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
import uuid
from typing import List

from .. import models, schemas, auth, database

router = APIRouter(
    prefix="/api/entregas",
    tags=["Entregas Tareas"]
)

@router.get("/", response_model=List[schemas.EntregaResponse])
def obtener_entregas(db: Session = Depends(database.get_db), current_user: models.User = Depends(auth.get_current_user)):
    """Obtener todas las entregas (solo admin y docentes)"""
    if current_user.rol not in [models.UserRole.ADMIN, models.UserRole.DOCENTE]:
        raise HTTPException(status_code=403, detail="No tienes permisos para ver entregas")
    return db.query(models.Entrega).all()

@router.post("/", response_model=schemas.EntregaResponse)
def crear_entrega(entrega: schemas.EntregaBase, db: Session = Depends(database.get_db), current_user: models.User = Depends(auth.get_current_user)):
    """Crear una nueva entrega (solo estudiantes)"""
    if current_user.rol != models.UserRole.ESTUDIANTE:
        raise HTTPException(status_code=403, detail="Solo los estudiantes pueden crear entregas")
    
    nueva_entrega = models.Entrega(
        id=str(uuid.uuid4()),
        tarea_id=entrega.tarea_id,
        estudiante_id=current_user.id,
        archivo=entrega.archivo
    )
    db.add(nueva_entrega)
    db.commit()
    db.refresh(nueva_entrega)
    return nueva_entrega

@router.put("/{entrega_id}", response_model=schemas.EntregaResponse)
def actualizar_entrega(entrega_id: str, entrega: schemas.EntregaBase, db: Session = Depends(database.get_db), current_user: models.User = Depends(auth.get_current_user)):
    """Actualizar una entrega (docentes califican)"""
    if current_user.rol not in [models.UserRole.DOCENTE, models.UserRole.ADMIN]:
        raise HTTPException(status_code=403, detail="Solo docentes pueden actualizar entregas")
    
    db_entrega = db.query(models.Entrega).filter(models.Entrega.id == entrega_id).first()
    if not db_entrega:
        raise HTTPException(status_code=404, detail="Entrega no encontrada")
    
    db_entrega.tarea_id = entrega.tarea_id
    db_entrega.archivo = entrega.archivo
    
    db.commit()
    db.refresh(db_entrega)
    return db_entrega