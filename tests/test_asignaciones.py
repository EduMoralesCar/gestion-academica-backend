from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import pytest

from app import main
from app import models, database, auth
from app.database import Base

SQLALCHEMY_DATABASE_URL = "sqlite:///:memory:"
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def override_get_db():
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()


@pytest.fixture(scope="module")
def test_app():
    # Crear tablas
    Base.metadata.create_all(bind=engine)

    # Inicializar datos
    db = TestingSessionLocal()
    admin = models.User(id="admin-id", email="admin@ex.com", hashed_password="x", nombre="Admin", apellido="A", rol=models.UserRole.ADMIN)
    docente = models.User(id="doc-id", email="doc@ex.com", hashed_password="x", nombre="Doc", apellido="D", rol=models.UserRole.DOCENTE)
    estudiante = models.User(id="est-id", email="est@ex.com", hashed_password="x", nombre="Est", apellido="E", rol=models.UserRole.ESTUDIANTE)
    curso = models.Curso(id="curso-id", nombre="Curso1", codigo="C1", creditos=3, ciclo=1, modalidad="virtual")
    db.add_all([admin, docente, estudiante, curso])
    db.commit()

    # Crear cliente
    app = main.app
    app.dependency_overrides[database.get_db] = override_get_db

    yield app

    # Teardown
    Base.metadata.drop_all(bind=engine)


def test_post_asignacion_admin_crea_ok(test_app):
    client = TestClient(test_app)

    # override current user as admin
    def get_admin():
        db = TestingSessionLocal()
        return db.query(models.User).filter(models.User.id == "admin-id").first()

    test_app.dependency_overrides[auth.get_current_user] = get_admin

    resp = client.post("/api/asignaciones/", json={"docente_id": "doc-id", "curso_id": "curso-id"})
    assert resp.status_code == 201
    data = resp.json()
    assert data["docente_id"] == "doc-id"
    assert data["curso_id"] == "curso-id"


def test_post_asignacion_con_usuario_no_docente_falla(test_app):
    client = TestClient(test_app)

    def get_admin():
        db = TestingSessionLocal()
        return db.query(models.User).filter(models.User.id == "admin-id").first()

    test_app.dependency_overrides[auth.get_current_user] = get_admin

    # Intentar asignar con un usuario que no es docente
    resp = client.post("/api/asignaciones/", json={"docente_id": "est-id", "curso_id": "curso-id"})
    assert resp.status_code == 400


def test_get_asignaciones_docente_ve_sus_asignaciones(test_app):
    client = TestClient(test_app)

    def get_docente():
        db = TestingSessionLocal()
        return db.query(models.User).filter(models.User.id == "doc-id").first()

    test_app.dependency_overrides[auth.get_current_user] = get_docente

    resp = client.get("/api/asignaciones/")
    assert resp.status_code == 200
    data = resp.json()
    # Debe contener al menos una asignación hecha en la prueba anterior
    assert any(a["docente_id"] == "doc-id" for a in data)
