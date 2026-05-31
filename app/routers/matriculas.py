from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from .. import models, schemas, auth, database
from ..services import matriculas as matriculas_service

router = APIRouter(
    prefix="/api/matriculas",
    tags=["Matriculas"]
)


def validar_admin(current_user: models.User, accion: str):
    if current_user.rol != models.UserRole.ADMIN:
        raise HTTPException(status_code=403, detail=f"Solo los administradores pueden {accion}")


def obtener_estudiante_o_404(db: Session, estudiante_id: str):
    estudiante = matriculas_service.obtener_estudiante(db, estudiante_id)
    if not estudiante:
        raise HTTPException(status_code=404, detail="Estudiante no encontrado")
    return estudiante


def obtener_curso_o_404(db: Session, curso_id: str):
    curso = matriculas_service.obtener_curso(db, curso_id)
    if not curso:
        raise HTTPException(status_code=404, detail="Curso no encontrado")
    return curso


@router.get("/", response_model=List[schemas.MatriculaResponse])
def obtener_matriculas(db: Session = Depends(database.get_db), current_user: models.User = Depends(auth.get_current_user)):
    return db.query(models.Matricula).all()


@router.get("/curso/{curso_id}/estudiantes", response_model=schemas.CursoEstudiantesResponse)
def obtener_estudiantes_por_curso(curso_id: str, db: Session = Depends(database.get_db), current_user: models.User = Depends(auth.get_current_user)):
    curso = obtener_curso_o_404(db, curso_id)

    matriculas = matriculas_service.listar_matriculas_activas_por_curso(db, curso_id)
    estudiantes = [
        schemas.EstudianteMatriculadoResponse(
            id=matricula.estudiante.id,
            email=matricula.estudiante.email,
            nombre=matricula.estudiante.nombre,
            apellido=matricula.estudiante.apellido,
            rol=matricula.estudiante.rol,
            codigo=matricula.estudiante.codigo,
            carrera=matricula.estudiante.carrera,
            ciclo=matricula.estudiante.ciclo,
            especialidad=matricula.estudiante.especialidad,
            departamento=matricula.estudiante.departamento,
            nivel_acceso=matricula.estudiante.nivel_acceso,
            createdAt=matricula.estudiante.createdAt,
            profilePicture=matricula.estudiante.profilePicture,
            matricula_id=matricula.id,
            fecha_matricula=matricula.fecha_matricula,
            estado_matricula=matricula.estado
        )
        for matricula in matriculas
    ]
    return {
        "curso": curso,
        "estudiantes": estudiantes,
        "total": len(estudiantes)
    }

@router.post("/", response_model=schemas.MatriculaResponse)
def matricular_estudiante(matricula: schemas.MatriculaCreate, db: Session = Depends(database.get_db), current_user: models.User = Depends(auth.get_current_user)):
    validar_admin(current_user, "matricular estudiantes")

    estudiante = obtener_estudiante_o_404(db, matricula.estudiante_id)
    if estudiante.rol != models.UserRole.ESTUDIANTE:
        raise HTTPException(status_code=400, detail="El usuario indicado no tiene rol de estudiante")

    obtener_curso_o_404(db, matricula.curso_id)

    matricula_existente = matriculas_service.obtener_matricula_activa(db, matricula.estudiante_id, matricula.curso_id)
    if matricula_existente:
        raise HTTPException(status_code=400, detail="El estudiante ya se encuentra matriculado en este curso")

    matricula_retirada = matriculas_service.obtener_matricula_retirada(db, matricula.estudiante_id, matricula.curso_id)
    if matricula_retirada:
        return matriculas_service.reactivar_matricula(db, matricula_retirada)

    return matriculas_service.crear_matricula(db, matricula.estudiante_id, matricula.curso_id)


@router.put("/{matricula_id}", response_model=schemas.MatriculaResponse)
def actualizar_matricula(matricula_id: str, matricula: schemas.MatriculaCreate, db: Session = Depends(database.get_db), current_user: models.User = Depends(auth.get_current_user)):
    validar_admin(current_user, "actualizar matrículas")

    db_matricula = matriculas_service.obtener_matricula(db, matricula_id)
    if not db_matricula:
        raise HTTPException(status_code=404, detail="Matrícula no encontrada")

    estudiante = obtener_estudiante_o_404(db, matricula.estudiante_id)
    if estudiante.rol != models.UserRole.ESTUDIANTE:
        raise HTTPException(status_code=400, detail="El usuario indicado no tiene rol de estudiante")

    obtener_curso_o_404(db, matricula.curso_id)

    matricula_existente = matriculas_service.obtener_matricula_activa(db, matricula.estudiante_id, matricula.curso_id)
    if matricula_existente and matricula_existente.id != matricula_id:
        raise HTTPException(status_code=400, detail="El estudiante ya se encuentra matriculado en este curso")

    db_matricula.estudiante_id = matricula.estudiante_id
    db_matricula.curso_id = matricula.curso_id
    
    db.commit()
    db.refresh(db_matricula)
    return db_matricula


@router.delete("/curso/{curso_id}/estudiantes/{estudiante_id}", response_model=schemas.MatriculaResponse)
def retirar_estudiante_de_curso(curso_id: str, estudiante_id: str, db: Session = Depends(database.get_db), current_user: models.User = Depends(auth.get_current_user)):
    validar_admin(current_user, "retirar estudiantes de cursos")

    obtener_estudiante_o_404(db, estudiante_id)
    obtener_curso_o_404(db, curso_id)

    matricula = matriculas_service.obtener_matricula_activa(db, estudiante_id, curso_id)
    if not matricula:
        raise HTTPException(status_code=404, detail="Matrícula activa no encontrada")

    return matriculas_service.retirar_matricula(db, matricula)
