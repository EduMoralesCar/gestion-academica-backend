from sqlalchemy.orm import Session

from .. import models


def obtener_matricula(db: Session, matricula_id: str):
    return db.query(models.Matricula).filter(models.Matricula.id == matricula_id).first()
