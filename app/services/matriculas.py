import uuid

from sqlalchemy.orm import Session

from .. import models


def obtener_estudiante(db: Session, estudiante_id: str):
    return db.query(models.User).filter(models.User.id == estudiante_id).first()


def obtener_curso(db: Session, curso_id: str):
    return db.query(models.Curso).filter(models.Curso.id == curso_id).first()


def obtener_matricula(db: Session, matricula_id: str):
    return db.query(models.Matricula).filter(models.Matricula.id == matricula_id).first()


def obtener_matricula_activa(db: Session, estudiante_id: str, curso_id: str):
    return db.query(models.Matricula).filter(
        models.Matricula.estudiante_id == estudiante_id,
        models.Matricula.curso_id == curso_id,
        models.Matricula.estado == models.EstadoMatricula.activo
    ).first()


def obtener_matricula_retirada(db: Session, estudiante_id: str, curso_id: str):
    return db.query(models.Matricula).filter(
        models.Matricula.estudiante_id == estudiante_id,
        models.Matricula.curso_id == curso_id,
        models.Matricula.estado == models.EstadoMatricula.retirado
    ).first()


def listar_matriculas_activas_por_curso(db: Session, curso_id: str):
    return db.query(models.Matricula).filter(
        models.Matricula.curso_id == curso_id,
        models.Matricula.estado == models.EstadoMatricula.activo
    ).all()


def crear_matricula(db: Session, estudiante_id: str, curso_id: str):
    nueva_matricula = models.Matricula(
        id=str(uuid.uuid4()),
        estudiante_id=estudiante_id,
        curso_id=curso_id
    )
    db.add(nueva_matricula)
    db.commit()
    db.refresh(nueva_matricula)
    return nueva_matricula


def retirar_matricula(db: Session, matricula: models.Matricula):
    matricula.estado = models.EstadoMatricula.retirado
    db.commit()
    db.refresh(matricula)
    return matricula


def reactivar_matricula(db: Session, matricula: models.Matricula):
    matricula.estado = models.EstadoMatricula.activo
    db.commit()
    db.refresh(matricula)
    return matricula
