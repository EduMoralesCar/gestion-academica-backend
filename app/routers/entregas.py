from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
import uuid
from typing import List

from .. import models, schemas, auth, database

router = APIRouter(
    prefix="/api/entregas",
    tags=["Entregas"]
)

@router.get("/", response_model=List[schemas.EntregaResponse])
def obtener_entregas(db: Session = Depends(database.get_db), current_user: models.User = Depends(auth.get_current_user)):
    return db.query(models.Entrega).all()

@router.post("/", response_model=schemas.EntregaResponse)
def subir_entrega(entrega: schemas.EntregaBase, db: Session = Depends(database.get_db), current_user: models.User = Depends(auth.get_current_user)):
    # Solo un ESTUDIANTE puede enviar una tarea
    if current_user.rol != models.UserRole.ESTUDIANTE:
        raise HTTPException(status_code=403, detail="Solo los estudiantes pueden subir entregas de tareas")
        
    nueva_entrega = models.Entrega(
        id=str(uuid.uuid4()),
        tarea_id=entrega.tarea_id,
        estudiante_id=current_user.id, # Asignamos automáticamente al estudiante que hace la petición
        archivo=entrega.archivo
    )
    db.add(nueva_entrega)
    db.commit()
    db.refresh(nueva_entrega)
    return nueva_entrega

@router.put("/{entrega_id}", response_model=schemas.EntregaResponse)
def actualizar_entrega(entrega_id: str, entrega: schemas.EntregaBase, db: Session = Depends(database.get_db), current_user: models.User = Depends(auth.get_current_user)):
    if current_user.rol != models.UserRole.ESTUDIANTE:
        raise HTTPException(status_code=403, detail="Solo los estudiantes pueden actualizar sus entregas")
        
    db_entrega = db.query(models.Entrega).filter(models.Entrega.id == entrega_id).first()
    if not db_entrega:
        raise HTTPException(status_code=404, detail="Entrega no encontrada")
        
    if db_entrega.estudiante_id != current_user.id:
        raise HTTPException(status_code=403, detail="No puedes modificar la entrega de otro estudiante")
        
    db_entrega.archivo = entrega.archivo
    
    db.commit()
    db.refresh(db_entrega)
    return db_entrega
