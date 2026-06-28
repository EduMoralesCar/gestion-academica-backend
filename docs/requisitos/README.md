# Especificación de Requerimientos - NuevaSchool

Este documento detalla los requerimientos del proyecto de Sistema de Gestión Académica NuevaSchool. Se incluye el catálogo de Requerimientos Funcionales (RF), Requerimientos No Funcionales (RNF) y la Matriz de Trazabilidad contra el código fuente del proyecto.

---

## 1. Requerimientos Funcionales (RF)

| ID | Requerimiento Funcional | Descripción Detallada | Prioridad |
| :--- | :--- | :--- | :---: |
| **RF-01** | Autenticación de Usuarios | Permite el inicio de sesión para Administradores, Docentes y Estudiantes mediante credenciales seguras (correo y contraseña). | Alta |
| **RF-02** | Recuperación de Contraseña | Permite restablecer contraseñas olvidadas a través de un código temporal de 6 dígitos enviado al correo institucional. | Media |
| **RF-03** | Cambio de Contraseña en Perfil | Permite a cualquier usuario autenticado actualizar su contraseña actual desde su panel de perfil personal. | Media |
| **RF-04** | Registro y Gestión de Usuarios | Permite al Administrador dar de alta, listar y editar usuarios detallando sus perfiles (especialidad, ciclo, rol). | Alta |
| **RF-05** | Creación y Gestión de Cursos | Permite al Administrador registrar nuevos cursos con créditos, ciclo, código único, modalidad y enlaces de Zoom. | Alta |
| **RF-06** | Asignación Docente | Permite al Administrador vincular a un docente registrado con uno o varios cursos académicos. | Alta |
| **RF-07** | Matrícula de Estudiantes | Permite inscribir a los estudiantes en sus respectivos cursos para habilitar su acceso a contenidos y tareas. | Alta |
| **RF-08** | Publicación de Temario y Contenidos | Permite a los docentes publicar la planificación semanal, temas de estudio y descripciones de las clases por cada curso. | Alta |
| **RF-09** | Gestión de Tareas (Docente) | Permite al docente crear, editar y eliminar asignaciones/tareas con fechas límite para que los alumnos entreguen. | Alta |
| **RF-10** | Entrega de Tareas (Estudiante) | Permite al estudiante visualizar tareas pendientes y subir sus archivos adjuntos como entregas resueltas. | Alta |
| **RF-11** | Calificación y Registro de Notas | Permite al docente calificar las tareas entregadas por los alumnos y asignarle notas numéricas que actualizan el promedio. | Alta |
| **RF-12** | Registro y Toma de Asistencia | Permite al docente registrar de forma diaria el estado de asistencia (Presente, Ausente, Tardanza) de los alumnos de un curso. | Alta |
| **RF-13** | Visualización Académica | Permite al estudiante ver su progreso en tiempo real: sus notas por tarea, su promedio final del curso y porcentaje de asistencia. | Alta |

---

## 2. Requerimientos No Funcionales (RNF)

| ID | Requerimiento No Funcional | Atributo de Calidad | Especificación Técnica |
| :--- | :--- | :--- | :--- |
| **RNF-01** | Seguridad en Contraseñas | Confidencialidad | Las contraseñas se almacenan cifradas en la base de datos utilizando el algoritmo de hash unidireccional **bcrypt** en el backend. |
| **RNF-02** | Control de Acceso basado en Roles (RBAC) | Autorización | Los endpoints y las vistas del frontend están estrictamente protegidos mediante tokens **JWT (JSON Web Tokens)** con validación de roles en cada petición. |
| **RNF-03** | Escalabilidad de la Arquitectura | Arquitectura | Arquitectura desacoplada en dos capas independientes: Frontend en **Next.js (React)** y Backend en **FastAPI (Python)** interactuando mediante API RESTful. |
| **RNF-04** | Integridad y Consistencia de Datos | Fiabilidad | Uso de un ORM (**SQLAlchemy**) con control de transacciones y restricciones a nivel de base de datos relacional PostgreSQL en **Supabase**. |
| **RNF-05** | Tiempo de Respuesta Eficiente | Rendimiento | Consultas de base de datos optimizadas con soporte asíncrono y uso de un pool de conexiones optimizado en Supabase. |
| **RNF-06** | Resiliencia de Despliegue | Disponibilidad | Implementación de creación automática de base de datos (`Base.metadata.create_all`) que auto-recupera la estructura de tablas ante caídas o migraciones en Render/Vercel. |
| **RNF-07** | Interfaz Adaptativa (Responsive) | Usabilidad | Diseño optimizado para dispositivos móviles, tabletas y computadoras de escritorio mediante Tailwind CSS y componentes Shadcn UI. |
| **RNF-08** | Seguridad de Comunicaciones | Seguridad | Toda transferencia de información entre el cliente, el servidor backend y la base de datos se realiza bajo protocolo cifrado **HTTPS/SSL** obligado. |

---

## 🗺️ Matriz de Trazabilidad (Requisitos vs. Código)

| ID | Requerimiento Funcional | Componente Backend (Modelos / Rutas) | Componente Frontend (Vistas / Componentes) |
| :--- | :--- | :--- | :--- |
| **RF-01** | Autenticación de Usuarios (Roles) | `app/routers/auth.py` / `UserRole` | `components/auth/LoginForm.tsx` / `AuthContext.tsx` |
| **RF-02/03** | Recuperación y Cambio de Clave | `app/routers/auth.py` | `/perfil` (Cambio de clave) / Vista de recuperación en Login |
| **RF-04** | Gestión de Usuarios (Admin) | `app/routers/usuarios.py` | `components/dashboards/AdminDashboard.tsx` / `/admin/usuarios` |
| **RF-05/06** | Creación y Asignación de Cursos | `app/routers/cursos.py` / `app/routers/asignaciones.py` | `/admin/cursos` |
| **RF-07** | Matrícula de Estudiantes | `app/routers/matriculas.py` | `/admin/reportes` / Gestión de Matrícula |
| **RF-08** | Publicación de Temarios | `app/routers/contenidos.py` | `/docente/cursos/[id]` (Temarios y semanas) |
| **RF-09/10** | Tareas y Entregas de Alumnos | `app/routers/tareas.py` / `app/routers/entregas.py` | `/docente/tareas` (Creación) / `/estudiante/tareas` (Subida) |
| **RF-11/13** | Calificación y Vista de Notas | `app/routers/notas.py` | `/docente/calificar` (Docente) / `/estudiante/notas` (Vista de alumno) |
| **RF-12** | Control de Asistencias | `app/routers/asistencias.py` | `/docente/asistencia` / `/estudiante/asistencia` |
