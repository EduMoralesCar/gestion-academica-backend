# Issue: Tablas no creadas al migrar/cambiar base de datos de Supabase en Render

## Descripción del Problema
Al realizar la migración de la base de datos de Supabase (cambio de cuenta y de `DATABASE_URL`), se actualizaron correctamente las variables de entorno en Render. Sin embargo, aunque el backend reportaba conexión exitosa, la aplicación frontend/backend fallaba debido a que las tablas no existían en la nueva base de datos.

## Causa Raíz
El servidor FastAPI (`main.py`) no tenía automatizada la creación de tablas al iniciar. Dependía exclusivamente de la ejecución manual del script `create_db.py`. Como Render solo ejecuta el comando de inicio para levantar el servidor web (`uvicorn main:app`), la base de datos permanecía vacía.

## Solución Aplicada

### 1. Inicialización y Carga Manual (Temporal)
Se ejecutaron los scripts del backend de forma local apuntando a la nueva base de datos para restaurar el servicio inmediatamente:
* `python create_db.py`: Crea la estructura de todas las tablas en la nueva base de datos.
* `python seed_db.py`: Carga los datos iniciales y usuarios de prueba.

### 2. Automatización en el Código (Solución Definitiva)
Se modificó el archivo principal del backend `main.py` para asegurar que el motor de base de datos (`engine`) cree automáticamente las tablas en cada inicio si es que no existen:

```diff
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
+from app.database import engine
+from app.models import Base
from app.routers import auth, cursos, usuarios, matriculas, tareas, asistencias, entregas, notas, asignaciones, contenidos, cursos_estudiante

+# Crear las tablas en la base de datos si no existen al iniciar la app
+Base.metadata.create_all(bind=engine)

app = FastAPI(...)
```

Esto garantiza que ante futuros cambios de base de datos, la estructura se creará sola al arrancar el backend en Render.
