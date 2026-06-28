from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from app.database import engine
from app.models import Base
from app.routers import auth, cursos, usuarios, matriculas, tareas, asistencias, entregas, notas, asignaciones, contenidos, cursos_estudiante

# Crear las tablas en la base de datos si no existen
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="NuevaSchool API",
    description="Backend de Sistema de Gestión Académica NuevaSchool",
    version="1.0.0"
)

# Middleware para normalizar la barra diagonal final sin redirecciones 307
@app.middleware("http")
async def normalizar_barra_final_middleware(request: Request, call_next):
    path = request.url.path
    parts = path.split("/")
    # Si la ruta es de listado API (ej: /api/usuarios tiene 2 segmentos),
    # no es de autenticación, no termina con '/' y no tiene extensión de archivo
    if (path.startswith("/api") and 
        not path.startswith("/api/auth") and 
        len(parts) == 3 and 
        not path.endswith("/") and 
        "." not in parts[-1]):
        # Modificamos el path en el scope de ASGI internamente para que FastAPI
        # resuelva la ruta con '/' sin emitir un 307 Redirect al cliente (evita perder cabeceras)
        request.scope["path"] = path + "/"
    return await call_next(request)

# Configuración de CORS para permitir al frontend conectarse
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/", tags=["Health Check"])
def health_check():
    return {"status": "ok", "message": "API NuevaSchool funcionando correctamente"}

# Incluir routers reales
app.include_router(auth.router)
app.include_router(cursos.router)
app.include_router(usuarios.router)
app.include_router(matriculas.router)
app.include_router(tareas.router)
app.include_router(asistencias.router)
app.include_router(entregas.router)
app.include_router(notas.router)
app.include_router(asignaciones.router)
app.include_router(contenidos.router)
app.include_router(cursos_estudiante.router)
