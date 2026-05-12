from sqlalchemy import Column, String, Integer, ForeignKey, DateTime, Float, Enum as SQLEnum
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
import enum
from .database import Base

# --- ENUMS ---
class UserRole(str, enum.Enum):
    ADMIN = 'ADMIN'
    DOCENTE = 'DOCENTE'
    ESTUDIANTE = 'ESTUDIANTE'

class ModalidadCurso(str, enum.Enum):
    presencial = 'presencial'
    virtual = 'virtual'

class EstadoMatricula(str, enum.Enum):
    activo = 'activo'
    retirado = 'retirado'

# --- MODELOS ---
class User(Base):
    __tablename__ = "users"
    id = Column(String, primary_key=True, index=True)
    email = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    nombre = Column(String, nullable=False)
    apellido = Column(String, nullable=False)
    rol = Column(SQLEnum(UserRole), nullable=False)
    profilePicture = Column(String, nullable=True)
    createdAt = Column(DateTime(timezone=True), server_default=func.now())

    # Campos Específicos (Nulos si el rol no coincide)
    codigo = Column(String, nullable=True) # Estudiante
    carrera = Column(String, nullable=True) # Estudiante
    ciclo = Column(Integer, nullable=True) # Estudiante
    especialidad = Column(String, nullable=True) # Docente
    departamento = Column(String, nullable=True) # Docente
    nivel_acceso = Column(String, nullable=True) # Admin
    estado = Column(String, default='activo') # Todos

    # Relaciones
    asignaciones_docente = relationship("AsignacionDocente", back_populates="docente")
    matriculas = relationship("Matricula", back_populates="estudiante")

class Curso(Base):
    __tablename__ = "cursos"
    id = Column(String, primary_key=True, index=True)
    nombre = Column(String, nullable=False)
    codigo = Column(String, unique=True, index=True)
    creditos = Column(Integer)
    ciclo = Column(Integer)
    modalidad = Column(SQLEnum(ModalidadCurso))
    zoom_link = Column(String, nullable=True)
    createdAt = Column(DateTime(timezone=True), server_default=func.now())

    # Relaciones
    docentes = relationship("AsignacionDocente", back_populates="curso")
    matriculas = relationship("Matricula", back_populates="curso")
    tareas = relationship("Tarea", back_populates="curso")
    asistencias = relationship("Asistencia", back_populates="curso")
    contenidos = relationship("ContenidoSemana", back_populates="curso")

class AsignacionDocente(Base):
    __tablename__ = "asignaciones_docente"
    id = Column(String, primary_key=True, index=True)
    docente_id = Column(String, ForeignKey("users.id"))
    curso_id = Column(String, ForeignKey("cursos.id"))
    fecha_asignacion = Column(DateTime(timezone=True), server_default=func.now())

    # Relaciones
    docente = relationship("User", back_populates="asignaciones_docente")
    curso = relationship("Curso", back_populates="docentes")

class Matricula(Base):
    __tablename__ = "matriculas"
    id = Column(String, primary_key=True, index=True)
    estudiante_id = Column(String, ForeignKey("users.id"))
    curso_id = Column(String, ForeignKey("cursos.id"))
    fecha_matricula = Column(DateTime(timezone=True), server_default=func.now())
    estado = Column(SQLEnum(EstadoMatricula), default=EstadoMatricula.activo)

    # Relaciones
    estudiante = relationship("User", back_populates="matriculas")
    curso = relationship("Curso", back_populates="matriculas")
    notas = relationship("Nota", back_populates="matricula")

class Nota(Base):
    __tablename__ = "notas"
    id = Column(String, primary_key=True, index=True)
    matricula_id = Column(String, ForeignKey("matriculas.id"))
    tipo = Column(String) # PC1, parcial, final...
    calificacion = Column(Float)
    peso = Column(Float)
    fecha = Column(DateTime(timezone=True), server_default=func.now())

    # Relaciones
    matricula = relationship("Matricula", back_populates="notas")

class ContenidoSemana(Base):
    __tablename__ = "contenidos_semana"
    id = Column(String, primary_key=True, index=True)
    curso_id = Column(String, ForeignKey("cursos.id"))
    semana_numero = Column(Integer, nullable=False)
    titulo = Column(String, nullable=False)
    descripcion = Column(String, nullable=True)
    archivo_url = Column(String, nullable=True)
    createdAt = Column(DateTime(timezone=True), server_default=func.now())

    # Relaciones
    curso = relationship("Curso", back_populates="contenidos")

class Tarea(Base):
    __tablename__ = "tareas"
    id = Column(String, primary_key=True, index=True)
    curso_id = Column(String, ForeignKey("cursos.id"))
    titulo = Column(String, nullable=False)
    descripcion = Column(String)
    fecha_entrega = Column(DateTime(timezone=True))
    puntaje_total = Column(Integer)
    archivo_referencia = Column(String, nullable=True)
    createdAt = Column(DateTime(timezone=True), server_default=func.now())

    # Relaciones
    curso = relationship("Curso", back_populates="tareas")
    entregas = relationship("Entrega", back_populates="tarea")

class Entrega(Base):
    __tablename__ = "entregas"
    id = Column(String, primary_key=True, index=True)
    tarea_id = Column(String, ForeignKey("tareas.id"))
    estudiante_id = Column(String, ForeignKey("users.id"))
    archivo = Column(String)
    fecha_entrega = Column(DateTime(timezone=True), server_default=func.now())
    calificacion = Column(Float, nullable=True)
    comentarios = Column(String, nullable=True)

    # Relaciones
    tarea = relationship("Tarea", back_populates="entregas")

class Asistencia(Base):
    __tablename__ = "asistencias"
    id = Column(String, primary_key=True, index=True)
    curso_id = Column(String, ForeignKey("cursos.id"))
    estudiante_id = Column(String, ForeignKey("users.id"))
    fecha = Column(DateTime(timezone=True))
    estado = Column(String) # presente, ausente, tardanza

    # Relaciones
    curso = relationship("Curso", back_populates="asistencias")
