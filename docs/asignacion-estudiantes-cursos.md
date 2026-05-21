# Asignacion de estudiantes a cursos

## Analisis de estructura actual

El proyecto usa FastAPI con routers bajo `app/routers`, modelos SQLAlchemy en `app/models.py` y schemas Pydantic en `app/schemas.py`.

La relacion entre estudiantes y cursos ya existe mediante el modelo `Matricula`, por lo que no es necesario crear una nueva tabla. Esta entidad conecta `users.id` con `cursos.id` y contiene el campo `estado`, definido por `EstadoMatricula` con los valores `activo` y `retirado`.

Los estudiantes se representan como usuarios con rol `ESTUDIANTE`. Los cursos se representan con el modelo `Curso`. La ruta actual `/api/matriculas` permite crear y actualizar matriculas, pero no valida existencia de estudiante, existencia de curso, rol del estudiante, duplicados ni retiro seguro.

La implementacion de Persona 2 debe extender la logica existente de matriculas y mantener compatibilidad con el frontend actual.

## Validacion local

Comandos ejecutados:

```bash
py -3 -m compileall app tests
py -3 -m pytest tests
```

Resultado:

- Compilacion correcta de `app` y `tests`.
- Pruebas de servicios de matriculas: 4 aprobadas.
- Advertencia existente de SQLAlchemy por `declarative_base`, sin impacto en esta funcionalidad.

## Endpoints implementados

- `POST /api/matriculas/`: asigna un estudiante a un curso.
- `GET /api/matriculas/curso/{curso_id}/estudiantes`: lista estudiantes activos del curso.
- `DELETE /api/matriculas/curso/{curso_id}/estudiantes/{estudiante_id}`: retira al estudiante del curso cambiando la matricula a estado `retirado`.

## Validaciones agregadas

- Solo usuarios `ADMIN` pueden asignar, actualizar o retirar matriculas.
- El estudiante debe existir.
- El usuario indicado debe tener rol `ESTUDIANTE`.
- El curso debe existir.
- No se permite duplicar una matricula activa del mismo estudiante en el mismo curso.
- Si una matricula retirada vuelve a asignarse, se reactiva el registro existente para evitar duplicados historicos.
- El retiro valida estudiante, curso y matricula activa antes de cambiar el estado.

## Preparacion para PR

La rama `feature/asignacion-estudiante-endpoints` queda preparada para Pull Request hacia `dev`. No se realizaron merges, rebases ni cambios sobre `dev` o `main`.
