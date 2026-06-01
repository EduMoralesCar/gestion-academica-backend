from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routers import auth, cursos, usuarios, matriculas, tareas, asistencias, entregas, notas, asignaciones, contenidos, cursos_estudiante

app = FastAPI(
    title="NuevaSchool API",
    description="Backend de Sistema de Gestión Académica NuevaSchool",
    version="1.0.0"
)

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
