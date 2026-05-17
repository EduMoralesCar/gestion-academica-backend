from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

from .. import models, schemas, auth, database

router = APIRouter(
    prefix="/api/estudiante/cursos",
    tags=["Cursos Estudiante"]
)

@router.get("", response_model=List[schemas.CursoResponse])
def obtener_mis_cursos(
    current_user: models.User = Depends(auth.get_current_user),
    db: Session = Depends(database.get_db)
):
    """
    TAREA 1: Obtiene todos los cursos asignados al estudiante autenticado.
    Solo accesible para estudiantes.
    """
    if current_user.rol != models.UserRole.ESTUDIANTE:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Solo estudiantes pueden acceder a sus cursos"
        )
    
    # Obtener todas las matrículas activas del estudiante
    matriculas = db.query(models.Matricula).filter(
        models.Matricula.estudiante_id == current_user.id,
        models.Matricula.estado == models.EstadoMatricula.activo
    ).all()
    
    if not matriculas:
        return []
    
    # Extraer los cursos de las matrículas
    cursos = [matricula.curso for matricula in matriculas]
    return cursos


@router.get("/{curso_id}", response_model=schemas.CursoResponse)
def obtener_detalle_curso(
    curso_id: str,
    current_user: models.User = Depends(auth.get_current_user),
    db: Session = Depends(database.get_db)
):
    """
    TAREA 2: Obtiene el detalle de un curso específico.
    Verifica que el estudiante esté matriculado en ese curso.
    """
    if current_user.rol != models.UserRole.ESTUDIANTE:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Solo estudiantes pueden acceder a cursos"
        )
    
    # Verificar que el estudiante está matriculado en este curso
    matricula = db.query(models.Matricula).filter(
        models.Matricula.estudiante_id == current_user.id,
        models.Matricula.curso_id == curso_id,
        models.Matricula.estado == models.EstadoMatricula.activo
    ).first()
    
    if not matricula:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="No estás matriculado en este curso"
        )
    
    curso = db.query(models.Curso).filter(models.Curso.id == curso_id).first()
    
    if not curso:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Curso no encontrado"
        )
    
    return curso