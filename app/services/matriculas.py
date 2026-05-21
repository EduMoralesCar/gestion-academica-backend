from sqlalchemy.orm import Session
import uuid

from .. import models


def obtener_matricula(db: Session, matricula_id: str):
    return db.query(models.Matricula).filter(models.Matricula.id == matricula_id).first()


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
