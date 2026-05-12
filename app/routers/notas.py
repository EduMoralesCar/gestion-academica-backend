from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
import uuid
from typing import List

from .. import models, schemas, auth, database

router = APIRouter(
    prefix="/api/notas",
    tags=["Notas"]
)

@router.get("/", response_model=List[schemas.NotaResponse])
def obtener_notas(db: Session = Depends(database.get_db), current_user: models.User = Depends(auth.get_current_user)):
    return db.query(models.Nota).all()

@router.post("/", response_model=schemas.NotaResponse)
def registrar_nota(nota: schemas.NotaBase, db: Session = Depends(database.get_db), current_user: models.User = Depends(auth.get_current_user)):
    # Solo un DOCENTE o ADMIN puede poner calificaciones
    if current_user.rol not in [models.UserRole.DOCENTE, models.UserRole.ADMIN]:
        raise HTTPException(status_code=403, detail="No tienes permisos para registrar notas. Solo docentes o administradores.")
        
    nueva_nota = models.Nota(
        id=str(uuid.uuid4()),
        matricula_id=nota.matricula_id,
        tipo=nota.tipo,
        calificacion=nota.calificacion,
        peso=nota.peso
    )
    db.add(nueva_nota)
    db.commit()
    db.refresh(nueva_nota)
    return nueva_nota

@router.put("/{nota_id}", response_model=schemas.NotaResponse)
def actualizar_nota(nota_id: str, nota: schemas.NotaBase, db: Session = Depends(database.get_db), current_user: models.User = Depends(auth.get_current_user)):
    if current_user.rol not in [models.UserRole.DOCENTE, models.UserRole.ADMIN]:
        raise HTTPException(status_code=403, detail="Solo docentes o administradores pueden actualizar notas")
        
    db_nota = db.query(models.Nota).filter(models.Nota.id == nota_id).first()
    if not db_nota:
        raise HTTPException(status_code=404, detail="Nota no encontrada")
        
    db_nota.matricula_id = nota.matricula_id
    db_nota.tipo = nota.tipo
    db_nota.calificacion = nota.calificacion
    db_nota.peso = nota.peso
    
    db.commit()
    db.refresh(db_nota)
    return db_nota
