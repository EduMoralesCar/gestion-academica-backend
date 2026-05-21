# Asignacion de estudiantes a cursos

## Analisis de estructura actual

El proyecto usa FastAPI con routers bajo `app/routers`, modelos SQLAlchemy en `app/models.py` y schemas Pydantic en `app/schemas.py`.

La relacion entre estudiantes y cursos ya existe mediante el modelo `Matricula`, por lo que no es necesario crear una nueva tabla. Esta entidad conecta `users.id` con `cursos.id` y contiene el campo `estado`, definido por `EstadoMatricula` con los valores `activo` y `retirado`.

Los estudiantes se representan como usuarios con rol `ESTUDIANTE`. Los cursos se representan con el modelo `Curso`. La ruta actual `/api/matriculas` permite crear y actualizar matriculas, pero no valida existencia de estudiante, existencia de curso, rol del estudiante, duplicados ni retiro seguro.

La implementacion de Persona 2 debe extender la logica existente de matriculas y mantener compatibilidad con el frontend actual.
