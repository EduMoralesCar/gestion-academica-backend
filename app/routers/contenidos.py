from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
import uuid
from typing import List

from .. import models, schemas, auth, database

router = APIRouter(
    prefix="/api/contenidos",
    tags=["Contenidos Semana (Temarios)"]
)

@router.get("/", response_model=List[schemas.ContenidoSemanaResponse])
def obtener_contenidos(db: Session = Depends(database.get_db), current_user: models.User = Depends(auth.get_current_user)):
    return db.query(models.ContenidoSemana).all()

@router.post("/", response_model=schemas.ContenidoSemanaResponse)
def crear_contenido(contenido: schemas.ContenidoSemanaCreate, db: Session = Depends(database.get_db), current_user: models.User = Depends(auth.get_current_user)):
    if current_user.rol not in [models.UserRole.DOCENTE, models.UserRole.ADMIN]:
        raise HTTPException(status_code=403, detail="Solo los docentes pueden crear contenido de la semana")
        
    nuevo_contenido = models.ContenidoSemana(
        id=str(uuid.uuid4()),
        curso_id=contenido.curso_id,
        semana_numero=contenido.semana_numero,
        titulo=contenido.titulo,
        descripcion=contenido.descripcion,
        archivo_url=contenido.archivo_url
    )
    db.add(nuevo_contenido)
    db.commit()
    db.refresh(nuevo_contenido)
    return nuevo_contenido

@router.put("/{contenido_id}", response_model=schemas.ContenidoSemanaResponse)
def actualizar_contenido(contenido_id: str, contenido: schemas.ContenidoSemanaBase, db: Session = Depends(database.get_db), current_user: models.User = Depends(auth.get_current_user)):
    if current_user.rol not in [models.UserRole.DOCENTE, models.UserRole.ADMIN]:
        raise HTTPException(status_code=403, detail="Solo los docentes pueden actualizar contenido")
        
    db_contenido = db.query(models.ContenidoSemana).filter(models.ContenidoSemana.id == contenido_id).first()
    if not db_contenido:
        raise HTTPException(status_code=404, detail="Contenido no encontrado")
        
    db_contenido.semana_numero = contenido.semana_numero
    db_contenido.titulo = contenido.titulo
    db_contenido.descripcion = contenido.descripcion
    db_contenido.archivo_url = contenido.archivo_url
    
    db.commit()
    db.refresh(db_contenido)
    return db_contenido

@router.delete("/{contenido_id}", status_code=status.HTTP_204_NO_CONTENT)
def eliminar_contenido(contenido_id: str, db: Session = Depends(database.get_db), current_user: models.User = Depends(auth.get_current_user)):
    if current_user.rol not in [models.UserRole.DOCENTE, models.UserRole.ADMIN]:
        raise HTTPException(status_code=403, detail="Solo los docentes pueden eliminar contenido")
        
    db_contenido = db.query(models.ContenidoSemana).filter(models.ContenidoSemana.id == contenido_id).first()
    if not db_contenido:
        raise HTTPException(status_code=404, detail="Contenido no encontrado")
        
    db.delete(db_contenido)
    db.commit()
    return None
