import uuid
from datetime import datetime, timezone
from app.database import SessionLocal, engine
from app import models, auth

def seed():
    db = SessionLocal()
    try:
        # Limpiar datos existentes
        print("Limpiando base de datos...")
        db.query(models.Asistencia).delete()
        db.query(models.Entrega).delete()
        db.query(models.Tarea).delete()
        db.query(models.Nota).delete()
        db.query(models.Matricula).delete()
        db.query(models.AsignacionDocente).delete()
        db.query(models.ContenidoSemana).delete()
        db.query(models.Curso).delete()
        db.query(models.User).delete()
        db.commit()

        print("Insertando usuarios...")
        usuarios = [
            # ADMIN
            {
                "id": "admin-1",
                "email": "admin@nuevaschool.pe",
                "nombre": "Carlos",
                "apellido": "Huamán",
                "rol": models.UserRole.ADMIN,
                "password": "admin123",
                "codigo": "A26001",
                "nivel_acceso": "super",
                "estado": "activo",
            },
            # DOCENTES
            {
                "id": "docente-1",
                "email": "docente@nuevaschool.pe",
                "nombre": "Juan",
                "apellido": "Pérez",
                "rol": models.UserRole.DOCENTE,
                "password": "docente123",
                "codigo": "D26001",
                "especialidad": "Desarrollo de Software",
                "departamento": "Ingeniería",
                "estado": "activo",
            },
            {
                "id": "docente-2",
                "email": "D26002@nuevaschool.pe",
                "nombre": "María",
                "apellido": "García",
                "rol": models.UserRole.DOCENTE,
                "password": "docente123",
                "codigo": "D26002",
                "especialidad": "Matemáticas y Estadística",
                "departamento": "Ciencias",
                "estado": "activo",
            },
            {
                "id": "docente-3",
                "email": "D26003@nuevaschool.pe",
                "nombre": "Luis",
                "apellido": "López",
                "rol": models.UserRole.DOCENTE,
                "password": "docente123",
                "codigo": "D26003",
                "especialidad": "Idiomas",
                "departamento": "Humanidades",
                "estado": "activo",
            },
            # ESTUDIANTES
            {
                "id": "estudiante-1",
                "email": "estudiante@nuevaschool.pe",
                "nombre": "Pedro",
                "apellido": "Rodríguez",
                "rol": models.UserRole.ESTUDIANTE,
                "password": "estudiante123",
                "codigo": "U26001",
                "carrera": "Ingeniería de Sistemas e Informática",
                "ciclo": 5,
                "estado": "activo",
            },
            {
                "id": "estudiante-2",
                "email": "U26002@nuevaschool.pe",
                "nombre": "Ana",
                "apellido": "Martínez",
                "rol": models.UserRole.ESTUDIANTE,
                "password": "estudiante123",
                "codigo": "U26002",
                "carrera": "Ingeniería de Sistemas e Informática",
                "ciclo": 5,
                "estado": "activo",
            },
            {
                "id": "estudiante-3",
                "email": "U26003@nuevaschool.pe",
                "nombre": "Carlos",
                "apellido": "López",
                "rol": models.UserRole.ESTUDIANTE,
                "password": "estudiante123",
                "codigo": "U26003",
                "carrera": "Ingeniería de Sistemas e Informática",
                "ciclo": 5,
                "estado": "activo",
            },
            {
                "id": "estudiante-4",
                "email": "U26004@nuevaschool.pe",
                "nombre": "Diana",
                "apellido": "Soto",
                "rol": models.UserRole.ESTUDIANTE,
                "password": "estudiante123",
                "codigo": "U26004",
                "carrera": "Administración de Empresas",
                "ciclo": 3,
                "estado": "activo",
            },
            {
                "id": "estudiante-5",
                "email": "U26005@nuevaschool.pe",
                "nombre": "Gabriel",
                "apellido": "Quispe",
                "rol": models.UserRole.ESTUDIANTE,
                "password": "estudiante123",
                "codigo": "U26005",
                "carrera": "Ingeniería de Sistemas e Informática",
                "ciclo": 7,
                "estado": "activo",
            },
            {
                "id": "estudiante-6",
                "email": "U26006@nuevaschool.pe",
                "nombre": "Francisco",
                "apellido": "Flores",
                "rol": models.UserRole.ESTUDIANTE,
                "password": "estudiante123",
                "codigo": "U26006",
                "carrera": "Administración de Empresas",
                "ciclo": 3,
                "estado": "activo",
            },
            {
                "id": "estudiante-7",
                "email": "U26007@nuevaschool.pe",
                "nombre": "Gloria",
                "apellido": "Ruiz",
                "rol": models.UserRole.ESTUDIANTE,
                "password": "estudiante123",
                "codigo": "U26007",
                "carrera": "Ingeniería de Sistemas e Informática",
                "ciclo": 5,
                "estado": "activo",
            },
            {
                "id": "estudiante-8",
                "email": "U26008@nuevaschool.pe",
                "nombre": "Hernán",
                "apellido": "Mendoza",
                "rol": models.UserRole.ESTUDIANTE,
                "password": "estudiante123",
                "codigo": "U26008",
                "carrera": "Administración de Empresas",
                "ciclo": 2,
                "estado": "activo",
            },
            {
                "id": "estudiante-9",
                "email": "U26009@nuevaschool.pe",
                "nombre": "Iris",
                "apellido": "Condori",
                "rol": models.UserRole.ESTUDIANTE,
                "password": "estudiante123",
                "codigo": "U26009",
                "carrera": "Ingeniería de Sistemas e Informática",
                "ciclo": 5,
                "estado": "activo",
            },
            {
                "id": "estudiante-10",
                "email": "U26010@nuevaschool.pe",
                "nombre": "José",
                "apellido": "Torres",
                "rol": models.UserRole.ESTUDIANTE,
                "password": "estudiante123",
                "codigo": "U26010",
                "carrera": "Administración de Empresas",
                "ciclo": 4,
                "estado": "activo",
            }
        ]

        for u in usuarios:
            hashed = auth.get_password_hash(u["password"])
            nuevo_usuario = models.User(
                id=u["id"],
                email=u["email"],
                hashed_password=hashed,
                nombre=u["nombre"],
                apellido=u["apellido"],
                rol=u["rol"],
                codigo=u.get("codigo"),
                carrera=u.get("carrera"),
                ciclo=u.get("ciclo"),
                especialidad=u.get("especialidad"),
                departamento=u.get("departamento"),
                nivel_acceso=u.get("nivel_acceso"),
                estado=u["estado"]
            )
            db.add(nuevo_usuario)
        
        db.commit()
        print("Insertando cursos...")
        cursos = [
            {
                "id": "curso-1",
                "nombre": "Programación I",
                "codigo": "INF101",
                "creditos": 4,
                "docente_id": "docente-1",
                "ciclo": 1,
                "modalidad": models.ModalidadCurso.presencial,
                "carreras": "Ingeniería de Sistemas e Informática,Ingeniería de Software"
            },
            {
                "id": "curso-2",
                "nombre": "Programación II",
                "codigo": "INF202",
                "creditos": 4,
                "docente_id": "docente-1",
                "ciclo": 3,
                "modalidad": models.ModalidadCurso.presencial,
                "carreras": "Ingeniería de Sistemas e Informática,Ingeniería de Software"
            },
            {
                "id": "curso-3",
                "nombre": "Base de Datos",
                "codigo": "INF301",
                "creditos": 3,
                "docente_id": "docente-1",
                "ciclo": 5,
                "modalidad": models.ModalidadCurso.presencial,
                "carreras": "Ingeniería de Sistemas e Informática,Ingeniería de Software"
            },
            {
                "id": "curso-4",
                "nombre": "Cálculo I",
                "codigo": "MAT101",
                "creditos": 4,
                "docente_id": "docente-2",
                "ciclo": 1,
                "modalidad": models.ModalidadCurso.presencial,
                "carreras": "Ingeniería de Sistemas e Informática,Ingeniería de Software,Administración de Empresas,Contabilidad"
            },
            {
                "id": "curso-5",
                "nombre": "Inglés I",
                "codigo": "ENG101",
                "creditos": 2,
                "docente_id": "docente-3",
                "ciclo": 1,
                "modalidad": models.ModalidadCurso.presencial,
                "carreras": "Ingeniería de Sistemas e Informática,Ingeniería de Software,Administración de Empresas,Contabilidad"
            }
        ]

        for c in cursos:
            nuevo_curso = models.Curso(
                id=c["id"],
                nombre=c["nombre"],
                codigo=c["codigo"],
                creditos=c["creditos"],
                ciclo=c["ciclo"],
                modalidad=c["modalidad"],
                carreras=c["carreras"]
            )
            db.add(nuevo_curso)
            # Crear asignacion del docente
            nueva_asig = models.AsignacionDocente(
                id=str(uuid.uuid4()),
                docente_id=c["docente_id"],
                curso_id=c["id"]
            )
            db.add(nueva_asig)
        
        db.commit()

        print("Insertando matrículas...")
        matriculas = [
            { "id": "mat-1", "estudiante_id": "estudiante-1", "curso_id": "curso-3", "estado": models.EstadoMatricula.activo },
            { "id": "mat-2", "estudiante_id": "estudiante-2", "curso_id": "curso-3", "estado": models.EstadoMatricula.activo },
            { "id": "mat-3", "estudiante_id": "estudiante-3", "curso_id": "curso-3", "estado": models.EstadoMatricula.activo },
            { "id": "mat-4", "estudiante_id": "estudiante-1", "curso_id": "curso-1", "estado": models.EstadoMatricula.activo },
            { "id": "mat-5", "estudiante_id": "estudiante-2", "curso_id": "curso-1", "estado": models.EstadoMatricula.activo },
            { "id": "mat-6", "estudiante_id": "estudiante-7", "curso_id": "curso-3", "estado": models.EstadoMatricula.activo },
            { "id": "mat-7", "estudiante_id": "estudiante-9", "curso_id": "curso-3", "estado": models.EstadoMatricula.activo },
            { "id": "mat-8", "estudiante_id": "estudiante-4", "curso_id": "curso-1", "estado": models.EstadoMatricula.activo },
        ]

        for m in matriculas:
            nueva_mat = models.Matricula(
                id=m["id"],
                estudiante_id=m["estudiante_id"],
                curso_id=m["curso_id"],
                estado=m["estado"]
            )
            db.add(nueva_mat)
        
        db.commit()

        print("Insertando notas...")
        notas = [
            # Estudiante 1 - Curso 3
            { "id": "nota-1", "matricula_id": "mat-1", "tipo": "parcial", "calificacion": 15, "peso": 15 },
            { "id": "nota-2", "matricula_id": "mat-1", "tipo": "practica", "calificacion": 17, "peso": 35 },
            { "id": "nota-3", "matricula_id": "mat-1", "tipo": "final", "calificacion": 16, "peso": 50 },

            # Estudiante 2 - Curso 3
            { "id": "nota-4", "matricula_id": "mat-2", "tipo": "parcial", "calificacion": 14, "peso": 15 },
            { "id": "nota-5", "matricula_id": "mat-2", "tipo": "practica", "calificacion": 16, "peso": 35 },
            { "id": "nota-6", "matricula_id": "mat-2", "tipo": "final", "calificacion": 15, "peso": 50 },

            # Estudiante 3 - Curso 3
            { "id": "nota-7", "matricula_id": "mat-3", "tipo": "parcial", "calificacion": 18, "peso": 15 },
            { "id": "nota-8", "matricula_id": "mat-3", "tipo": "practica", "calificacion": 19, "peso": 35 },
            { "id": "nota-9", "matricula_id": "mat-3", "tipo": "final", "calificacion": 18, "peso": 50 },

            # Estudiante 1 - Curso 1
            { "id": "nota-10", "matricula_id": "mat-4", "tipo": "parcial", "calificacion": 16, "peso": 15 },
            { "id": "nota-11", "matricula_id": "mat-4", "tipo": "practica", "calificacion": 18, "peso": 35 },

            # Estudiante 2 - Curso 1
            { "id": "nota-12", "matricula_id": "mat-5", "tipo": "parcial", "calificacion": 13, "peso": 15 },
            { "id": "nota-13", "matricula_id": "mat-5", "tipo": "practica", "calificacion": 14, "peso": 35 },
        ]

        for n in notas:
            nueva_nota = models.Nota(
                id=n["id"],
                matricula_id=n["matricula_id"],
                tipo=n["tipo"],
                calificacion=float(n["calificacion"]),
                peso=float(n["peso"])
            )
            db.add(nueva_nota)
        
        db.commit()

        print("Insertando tareas...")
        tareas = [
            {
                "id": "tarea-1",
                "curso_id": "curso-3",
                "titulo": "Diseño de Base de Datos",
                "descripcion": "Diseñar un schema para un sistema de biblioteca",
                "fecha_entrega": datetime(2026, 4, 20, 23, 59),
                "puntaje_total": 10,
            },
            {
                "id": "tarea-2",
                "curso_id": "curso-3",
                "titulo": "Consultas SQL Avanzadas",
                "descripcion": "Realizar 5 consultas complejas con JOINs",
                "fecha_entrega": datetime(2026, 5, 10, 23, 59),
                "puntaje_total": 15,
            },
            {
                "id": "tarea-3",
                "curso_id": "curso-1",
                "titulo": "Programa en Python",
                "descripcion": "Crear programa que calcule el factorial",
                "fecha_entrega": datetime(2026, 5, 15, 23, 59),
                "puntaje_total": 10,
            }
        ]

        for t in tareas:
            nueva_tarea = models.Tarea(
                id=t["id"],
                curso_id=t["curso_id"],
                titulo=t["titulo"],
                descripcion=t["descripcion"],
                fecha_entrega=t["fecha_entrega"],
                puntaje_total=t["puntaje_total"]
            )
            db.add(nueva_tarea)
        
        db.commit()

        print("Insertando entregas...")
        entregas = [
            { "id": "ent-1", "tarea_id": "tarea-1", "estudiante_id": "estudiante-1", "archivo": "db_design.pdf", "calificacion": 9.0, "comentarios": "Buen diseño" },
            { "id": "ent-2", "tarea_id": "tarea-1", "estudiante_id": "estudiante-2", "archivo": "db_design_v2.pdf", "calificacion": 10.0, "comentarios": "Excelente" },
            { "id": "ent-3", "tarea_id": "tarea-2", "estudiante_id": "estudiante-1", "archivo": "sql_queries.sql", "calificacion": 14.0, "comentarios": "Falta optimización" },
        ]

        for e in entregas:
            nueva_entrega = models.Entrega(
                id=e["id"],
                tarea_id=e["tarea_id"],
                estudiante_id=e["estudiante_id"],
                archivo=e["archivo"],
                calificacion=e["calificacion"],
                comentarios=e["comentarios"]
            )
            db.add(nueva_entrega)
        
        db.commit()

        print("Insertando asistencias...")
        asistencias = [
            # Curso 3 - Abril
            { "id": "asi-1", "curso_id": "curso-3", "estudiante_id": "estudiante-1", "fecha": datetime(2026, 4, 1), "estado": "presente" },
            { "id": "asi-2", "curso_id": "curso-3", "estudiante_id": "estudiante-1", "fecha": datetime(2026, 4, 3), "estado": "presente" },
            { "id": "asi-3", "curso_id": "curso-3", "estudiante_id": "estudiante-1", "fecha": datetime(2026, 4, 5), "estado": "tardanza" },
            { "id": "asi-4", "curso_id": "curso-3", "estudiante_id": "estudiante-1", "fecha": datetime(2026, 4, 8), "estado": "ausente" },
            { "id": "asi-5", "curso_id": "curso-3", "estudiante_id": "estudiante-1", "fecha": datetime(2026, 4, 10), "estado": "presente" },

            { "id": "asi-6", "curso_id": "curso-3", "estudiante_id": "estudiante-2", "fecha": datetime(2026, 4, 1), "estado": "presente" },
            { "id": "asi-7", "curso_id": "curso-3", "estudiante_id": "estudiante-2", "fecha": datetime(2026, 4, 3), "estado": "presente" },
            { "id": "asi-8", "curso_id": "curso-3", "estudiante_id": "estudiante-2", "fecha": datetime(2026, 4, 5), "estado": "presente" },
            { "id": "asi-9", "curso_id": "curso-3", "estudiante_id": "estudiante-2", "fecha": datetime(2026, 4, 8), "estado": "presente" },
            { "id": "asi-10", "curso_id": "curso-3", "estudiante_id": "estudiante-2", "fecha": datetime(2026, 4, 10), "estado": "presente" },
        ]

        for a in asistencias:
            nueva_asistencia = models.Asistencia(
                id=a["id"],
                curso_id=a["curso_id"],
                estudiante_id=a["estudiante_id"],
                fecha=a["fecha"],
                estado=a["estado"]
            )
            db.add(nueva_asistencia)
        
        db.commit()

        print("Insertando temarios/contenidos...")
        # Agregar 18 semanas de contenido vacío por curso para que tengan el temario
        for curso_id in ["curso-1", "curso-2", "curso-3", "curso-4", "curso-5"]:
            for sem in range(1, 19):
                nuevo_cont = models.ContenidoSemana(
                    id=str(uuid.uuid4()),
                    curso_id=curso_id,
                    semana_numero=sem,
                    titulo=f"Semana {sem}: Introducción y Fundamentos",
                    descripcion=f"En esta semana se revisarán los conceptos básicos del tema de la unidad {sem}."
                )
                db.add(nuevo_cont)
        
        db.commit()
        print("¡Base de datos sembrada exitosamente!")
    except Exception as ex:
        print(f"Error sembrando base de datos: {ex}")
        db.rollback()
    finally:
        db.close()

if __name__ == "__main__":
    seed()
