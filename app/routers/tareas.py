from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
import uuid
from typing import List

from .. import models, schemas, auth, database

router = APIRouter(
    prefix="/api/tareas",
    tags=["Tareas"]
)

@router.get("/", response_model=List[schemas.TareaResponse])
def obtener_tareas(db: Session = Depends(database.get_db), current_user: models.User = Depends(auth.get_current_user)):
    """Obtener todas las tareas"""
    return db.query(models.Tarea).all()

@router.post("/", response_model=schemas.TareaResponse)
def crear_tarea(tarea: schemas.TareaBase, db: Session = Depends(database.get_db), current_user: models.User = Depends(auth.get_current_user)):
    """Crear una nueva tarea (solo docentes y admins)"""
    if current_user.rol not in [models.UserRole.DOCENTE, models.UserRole.ADMIN]:
        raise HTTPException(status_code=403, detail="Solo los docentes pueden crear tareas")

    nueva_tarea = models.Tarea(
        id=str(uuid.uuid4()),
        curso_id=tarea.curso_id,
        titulo=tarea.titulo,
        descripcion=tarea.descripcion,
        fecha_entrega=tarea.fecha_entrega,
        puntaje_total=tarea.puntaje_total,
        archivo_referencia=tarea.archivo_referencia
    )
    db.add(nueva_tarea)
    db.commit()
    db.refresh(nueva_tarea)
    return nueva_tarea

@router.put("/{tarea_id}", response_model=schemas.TareaResponse)
def actualizar_tarea(tarea_id: str, tarea: schemas.TareaBase, db: Session = Depends(database.get_db), current_user: models.User = Depends(auth.get_current_user)):
    """Actualizar una tarea (solo docentes)"""
    if current_user.rol not in [models.UserRole.DOCENTE, models.UserRole.ADMIN]:
        raise HTTPException(status_code=403, detail="Solo docentes pueden actualizar tareas")

    db_tarea = db.query(models.Tarea).filter(models.Tarea.id == tarea_id).first()
    if not db_tarea:
        raise HTTPException(status_code=404, detail="Tarea no encontrada")

    db_tarea.titulo = tarea.titulo
    db_tarea.descripcion = tarea.descripcion
    db_tarea.fecha_entrega = tarea.fecha_entrega
    db_tarea.puntaje_total = tarea.puntaje_total
    db_tarea.archivo_referencia = tarea.archivo_referencia

    db.commit()
    db.refresh(db_tarea)
    return db_tarea

@router.delete("/{tarea_id}", status_code=status.HTTP_204_NO_CONTENT)
def eliminar_tarea(tarea_id: str, db: Session = Depends(database.get_db), current_user: models.User = Depends(auth.get_current_user)):
    """Eliminar una tarea"""
    if current_user.rol not in [models.UserRole.DOCENTE, models.UserRole.ADMIN]:
        raise HTTPException(status_code=403, detail="Solo docentes pueden eliminar tareas")

    db_tarea = db.query(models.Tarea).filter(models.Tarea.id == tarea_id).first()
    if not db_tarea:
        raise HTTPException(status_code=404, detail="Tarea no encontrada")

    db.delete(db_tarea)
    db.commit()
    return None
