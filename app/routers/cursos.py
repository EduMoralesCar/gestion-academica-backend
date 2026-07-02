from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
import uuid
from typing import List

from .. import models, schemas, auth, database

router = APIRouter(
    prefix="/api/cursos",
    tags=["Cursos"]
)

@router.get("/", response_model=List[schemas.CursoResponse])
def obtener_cursos(db: Session = Depends(database.get_db), current_user: models.User = Depends(auth.get_current_user)):
    # Todos los usuarios logueados pueden ver la lista de cursos
    cursos = db.query(models.Curso).all()
    return cursos

@router.post("/", response_model=schemas.CursoResponse)
def crear_curso(curso: schemas.CursoBase, db: Session = Depends(database.get_db), current_user: models.User = Depends(auth.get_current_user)):
    # Solo Administradores pueden crear cursos y asignar al docente
    if current_user.rol != models.UserRole.ADMIN:
        raise HTTPException(status_code=403, detail="Solo los administradores pueden crear cursos")

    nuevo_curso = models.Curso(
        id=str(uuid.uuid4()),
        nombre=curso.nombre,
        codigo=curso.codigo,
        creditos=curso.creditos,
        ciclo=curso.ciclo,
        modalidad=curso.modalidad,
        zoom_link=curso.zoom_link,
        carreras=curso.carreras
    )
    db.add(nuevo_curso)
    db.commit()
    db.refresh(nuevo_curso)
    return nuevo_curso

@router.put("/{curso_id}", response_model=schemas.CursoResponse)
def actualizar_curso(curso_id: str, curso: schemas.CursoBase, db: Session = Depends(database.get_db), current_user: models.User = Depends(auth.get_current_user)):
    if current_user.rol != models.UserRole.ADMIN:
        raise HTTPException(status_code=403, detail="Solo los administradores pueden actualizar cursos")
    
    db_curso = db.query(models.Curso).filter(models.Curso.id == curso_id).first()
    if not db_curso:
        raise HTTPException(status_code=404, detail="Curso no encontrado")
        
    db_curso.nombre = curso.nombre
    db_curso.codigo = curso.codigo
    db_curso.creditos = curso.creditos
    db_curso.ciclo = curso.ciclo
    db_curso.modalidad = curso.modalidad
    db_curso.zoom_link = curso.zoom_link
    db_curso.carreras = curso.carreras
    
    db.commit()
    db.refresh(db_curso)
    return db_curso

@router.delete("/{curso_id}", status_code=status.HTTP_204_NO_CONTENT)
def eliminar_curso(curso_id: str, db: Session = Depends(database.get_db), current_user: models.User = Depends(auth.get_current_user)):
    if current_user.rol != models.UserRole.ADMIN:
        raise HTTPException(status_code=403, detail="Solo los administradores pueden eliminar cursos")
        
    db_curso = db.query(models.Curso).filter(models.Curso.id == curso_id).first()
    if not db_curso:
        raise HTTPException(status_code=404, detail="Curso no encontrado")
        
    db.delete(db_curso)
    db.commit()
    return None
