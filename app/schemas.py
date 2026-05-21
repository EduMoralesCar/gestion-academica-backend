from pydantic import BaseModel, EmailStr, Field
from typing import Optional, List
from datetime import datetime
from enum import Enum

class UserRole(str, Enum):
    ADMIN = 'ADMIN'
    DOCENTE = 'DOCENTE'
    ESTUDIANTE = 'ESTUDIANTE'

class UserBase(BaseModel):
    email: EmailStr
    nombre: str
    apellido: str
    rol: UserRole
    
    # Campos opcionales según el rol
    codigo: Optional[str] = None
    carrera: Optional[str] = None
    ciclo: Optional[int] = None
    especialidad: Optional[str] = None
    departamento: Optional[str] = None
    nivel_acceso: Optional[str] = None

class UserCreate(UserBase):
    password: str

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "email": "miguel@nuevaschool.edu",
                    "nombre": "Miguel",
                    "apellido": "Gomez",
                    "rol": "DOCENTE",
                    "password": "superpassword",
                    "codigo": "",
                    "carrera": "",
                    "ciclo": 0,
                    "especialidad": "Matemáticas",
                    "departamento": "Ciencias Exactas",
                    "nivel_acceso": ""
                }
            ]
        }
    }

class UserResponse(UserBase):
    id: str
    createdAt: datetime
    profilePicture: Optional[str] = None
    
    class Config:
        from_attributes = True

class CursoBase(BaseModel):
    nombre: str
    codigo: str
    creditos: int
    ciclo: int
    modalidad: str
    zoom_link: Optional[str] = None

class CursoCreate(CursoBase):
    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "nombre": "Matemáticas Avanzadas",
                    "codigo": "MAT-101",
                    "creditos": 4,
                    "ciclo": 1,
                    "modalidad": "virtual",
                    "zoom_link": "https://zoom.us/j/123456789"
                }
            ]
        }
    }

class AsignacionDocenteCreate(BaseModel):
    docente_id: str
    curso_id: str
    
    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "docente_id": "id-del-profesor",
                    "curso_id": "id-del-curso"
                }
            ]
        }
    }

class AsignacionDocenteResponse(AsignacionDocenteCreate):
    id: str
    fecha_asignacion: datetime
    class Config:
        from_attributes = True

class CursoResponse(CursoBase):
    id: str
    createdAt: datetime

    class Config:
        from_attributes = True

class MatriculaCreate(BaseModel):
    estudiante_id: str
    curso_id: str
    
    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "estudiante_id": "escribe-el-id-del-estudiante-aqui",
                    "curso_id": "escribe-el-id-del-curso-aqui"
                }
            ]
        }
    }

class MatriculaResponse(MatriculaCreate):
    id: str
    fecha_matricula: datetime
    estado: str
    
    class Config:
        from_attributes = True

class EstudianteMatriculadoResponse(UserResponse):
    matricula_id: str
    fecha_matricula: datetime
    estado_matricula: str

class CursoEstudiantesResponse(BaseModel):
    curso: CursoResponse
    estudiantes: List[EstudianteMatriculadoResponse]
    total: int

# --- Auth Schemas ---
class Token(BaseModel):
    access_token: str
    token_type: str
    user: UserResponse

class TokenData(BaseModel):
    email: Optional[str] = None

class ForgotPasswordRequest(BaseModel):
    email: EmailStr

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "email": "estudiante@nuevaschool.pe"
                }
            ]
        }
    }

class ResetPasswordRequest(BaseModel):
    email: EmailStr
    codigo: str = Field(..., min_length=6, max_length=6, pattern=r"^\d{6}$")
    nueva_contrasenia: str = Field(..., min_length=6)

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "email": "estudiante@nuevaschool.pe",
                    "codigo": "123456",
                    "nueva_contrasenia": "nuevaClave123"
                }
            ]
        }
    }

class PasswordResetMessage(BaseModel):
    message: str

class ChangePasswordRequest(BaseModel):
    contrasenia_actual: str = Field(..., min_length=6)
    nueva_contrasenia: str = Field(..., min_length=6)

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "contrasenia_actual": "claveActual123",
                    "nueva_contrasenia": "nuevaClave123"
                }
            ]
        }
    }

class ContenidoSemanaBase(BaseModel):
    curso_id: str
    semana_numero: int
    titulo: str
    descripcion: Optional[str] = None
    archivo_url: Optional[str] = None

class ContenidoSemanaCreate(ContenidoSemanaBase):
    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "curso_id": "id-del-curso",
                    "semana_numero": 1,
                    "titulo": "Introducción a la materia",
                    "descripcion": "Leer el PDF antes de la clase.",
                    "archivo_url": "https://link-al-pdf.com/tema1.pdf"
                }
            ]
        }
    }

class ContenidoSemanaResponse(ContenidoSemanaBase):
    id: str
    createdAt: datetime
    class Config:
        from_attributes = True

class TareaBase(BaseModel):
    curso_id: str
    titulo: str
    descripcion: Optional[str] = None
    fecha_entrega: datetime
    puntaje_total: int
    archivo_referencia: Optional[str] = None

    model_config = {
        "json_schema_extra": {
            "examples": [{
                "curso_id": "id-del-curso",
                "titulo": "Ensayo sobre historia",
                "descripcion": "Escribir 5 páginas sobre la revolución.",
                "fecha_entrega": "2026-06-01T23:59:00Z",
                "puntaje_total": 20,
                "archivo_referencia": "http://link-al-pdf.com/doc.pdf"
            }]
        }
    }

class TareaResponse(TareaBase):
    id: str
    createdAt: datetime
    class Config:
        from_attributes = True

class AsistenciaBase(BaseModel):
    curso_id: str
    estudiante_id: str
    fecha: datetime
    estado: str # presente, ausente, tardanza

    model_config = {
        "json_schema_extra": {
            "examples": [{
                "curso_id": "id-del-curso",
                "estudiante_id": "id-del-estudiante",
                "fecha": "2026-05-06T10:00:00Z",
                "estado": "presente"
            }]
        }
    }

class AsistenciaResponse(AsistenciaBase):
    id: str
    class Config:
        from_attributes = True

class EntregaBase(BaseModel):
    tarea_id: str
    archivo: str

    model_config = {
        "json_schema_extra": {
            "examples": [{
                "tarea_id": "id-de-la-tarea",
                "archivo": "http://link-al-drive.com/mi-tarea.pdf"
            }]
        }
    }

class EntregaResponse(EntregaBase):
    id: str
    estudiante_id: str
    fecha_entrega: datetime
    calificacion: Optional[float] = None
    comentarios: Optional[str] = None
    class Config:
        from_attributes = True

class NotaBase(BaseModel):
    matricula_id: str
    tipo: str
    calificacion: float
    peso: float

    model_config = {
        "json_schema_extra": {
            "examples": [{
                "matricula_id": "id-de-la-matricula",
                "tipo": "Examen Parcial",
                "calificacion": 18.5,
                "peso": 0.3
            }]
        }
    }

class NotaResponse(NotaBase):
    id: str
    fecha: datetime
    class Config:
        from_attributes = True
