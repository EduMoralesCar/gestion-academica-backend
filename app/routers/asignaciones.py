from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
import uuid
from typing import List, Optional

from .. import models, schemas, auth, database

router = APIRouter(
    prefix="/api/asignaciones",
    tags=["Asignaciones Docente"]
)

def validar_docente(docente_id: str, db: Session):
    docente = db.query(models.User).filter(models.User.id == docente_id).first()
    if not docente:
        raise HTTPException(status_code=404, detail="Docente no encontrado")
    if docente.rol != models.UserRole.DOCENTE:
        raise HTTPException(status_code=400, detail="El usuario indicado no tiene rol de DOCENTE")
    return docente

def validar_curso(curso_id: str, db: Session):
    curso = db.query(models.Curso).filter(models.Curso.id == curso_id).first()
    if not curso:
        raise HTTPException(status_code=404, detail="Curso no encontrado")
    return curso

@router.get("/", response_model=List[schemas.AsignacionDocenteResponse])
def obtener_asignaciones(docente_id: Optional[str] = None, curso_id: Optional[str] = None, db: Session = Depends(database.get_db), current_user: models.User = Depends(auth.get_current_user)):
    # Los estudiantes no pueden consultar asignaciones
    if current_user.rol == models.UserRole.ESTUDIANTE:
        raise HTTPException(status_code=403, detail="No tienes permisos para ver las asignaciones")

    query = db.query(models.AsignacionDocente)

    # Si es docente sólo puede ver sus propias asignaciones
    if current_user.rol == models.UserRole.DOCENTE:
        query = query.filter(models.AsignacionDocente.docente_id == current_user.id)

    # Filtros opcionales (solo aplican para quien tenga permiso)
    if docente_id:
        query = query.filter(models.AsignacionDocente.docente_id == docente_id)
    if curso_id:
        query = query.filter(models.AsignacionDocente.curso_id == curso_id)

    return query.all()


@router.get("/{asignacion_id}", response_model=schemas.AsignacionDocenteResponse)
def obtener_asignacion_por_id(asignacion_id: str, db: Session = Depends(database.get_db), current_user: models.User = Depends(auth.get_current_user)):
    asignacion = db.query(models.AsignacionDocente).filter(models.AsignacionDocente.id == asignacion_id).first()
    if not asignacion:
        raise HTTPException(status_code=404, detail="Asignación no encontrada")

    # Restricción: estudiantes no pueden ver, docentes sólo su asignación
    if current_user.rol == models.UserRole.ESTUDIANTE:
        raise HTTPException(status_code=403, detail="No tienes permisos para ver la asignación")
    if current_user.rol == models.UserRole.DOCENTE and asignacion.docente_id != current_user.id:
        raise HTTPException(status_code=403, detail="No tienes permisos para ver esta asignación")

    return asignacion

@router.post("/", status_code=201, response_model=schemas.AsignacionDocenteResponse)
def asignar_docente(asignacion: schemas.AsignacionDocenteCreate, db: Session = Depends(database.get_db), current_user: models.User = Depends(auth.get_current_user)):
    if current_user.rol != models.UserRole.ADMIN:
        raise HTTPException(status_code=403, detail="Solo los administradores pueden asignar docentes a cursos")

    validar_docente(asignacion.docente_id, db)
    validar_curso(asignacion.curso_id, db)
        
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

    validar_docente(asignacion.docente_id, db)
    validar_curso(asignacion.curso_id, db)
        
    db_asignacion.docente_id = asignacion.docente_id
    db_asignacion.curso_id = asignacion.curso_id
    
    db.commit()
    db.refresh(db_asignacion)
    return db_asignacion


@router.delete("/{asignacion_id}", status_code=204)
def eliminar_asignacion(asignacion_id: str, db: Session = Depends(database.get_db), current_user: models.User = Depends(auth.get_current_user)):
    if current_user.rol != models.UserRole.ADMIN:
        raise HTTPException(status_code=403, detail="Solo los administradores pueden eliminar asignaciones")

    db_asignacion = db.query(models.AsignacionDocente).filter(models.AsignacionDocente.id == asignacion_id).first()
    if not db_asignacion:
        raise HTTPException(status_code=404, detail="Asignación no encontrada")

    db.delete(db_asignacion)
    db.commit()
    return None
