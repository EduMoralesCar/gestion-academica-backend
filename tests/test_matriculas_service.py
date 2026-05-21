from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app import models
from app.database import Base
from app.services import matriculas as matriculas_service


def crear_db_prueba():
    engine = create_engine("sqlite:///:memory:")
    TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    Base.metadata.create_all(bind=engine)
    return TestingSessionLocal()


def crear_estudiante(db, estudiante_id="estudiante-1"):
    estudiante = models.User(
        id=estudiante_id,
        email=f"{estudiante_id}@nuevaschool.pe",
        hashed_password="hash",
        nombre="Ana",
        apellido="Lopez",
        rol=models.UserRole.ESTUDIANTE
    )
    db.add(estudiante)
    db.commit()
    return estudiante


def crear_curso(db, curso_id="curso-1"):
    curso = models.Curso(
        id=curso_id,
        nombre="Matematica",
        codigo=f"MAT-{curso_id}",
        creditos=4,
        ciclo=1,
        modalidad=models.ModalidadCurso.virtual
    )
    db.add(curso)
    db.commit()
    return curso


def test_crear_y_consultar_matricula_activa():
    db = crear_db_prueba()
    crear_estudiante(db)
    crear_curso(db)

    matricula = matriculas_service.crear_matricula(db, "estudiante-1", "curso-1")
    matricula_activa = matriculas_service.obtener_matricula_activa(db, "estudiante-1", "curso-1")

    assert matricula_activa.id == matricula.id
    assert matricula_activa.estado == models.EstadoMatricula.activo


def test_listar_matriculas_activas_por_curso():
    db = crear_db_prueba()
    crear_estudiante(db)
    crear_curso(db)
    matriculas_service.crear_matricula(db, "estudiante-1", "curso-1")

    matriculas = matriculas_service.listar_matriculas_activas_por_curso(db, "curso-1")

    assert len(matriculas) == 1
    assert matriculas[0].estudiante_id == "estudiante-1"


def test_retirar_matricula_conserva_registro_como_retirado():
    db = crear_db_prueba()
    crear_estudiante(db)
    crear_curso(db)
    matricula = matriculas_service.crear_matricula(db, "estudiante-1", "curso-1")

    retirada = matriculas_service.retirar_matricula(db, matricula)
    matricula_activa = matriculas_service.obtener_matricula_activa(db, "estudiante-1", "curso-1")

    assert retirada.estado == models.EstadoMatricula.retirado
    assert matricula_activa is None
