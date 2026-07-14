-- ==========================================================
-- COPIA DE SEGURIDAD (BACKUP) - NUEVASCHOOL PRODUCTION DB
-- Generado automáticamente por script de Python
-- ==========================================================

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', 'public', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

-- Limpieza de tablas existentes
DROP TABLE IF EXISTS "codigos_recuperacion_contrasena" CASCADE;
DROP TABLE IF EXISTS "asistencias" CASCADE;
DROP TABLE IF EXISTS "entregas" CASCADE;
DROP TABLE IF EXISTS "tareas" CASCADE;
DROP TABLE IF EXISTS "contenidos_semana" CASCADE;
DROP TABLE IF EXISTS "notas" CASCADE;
DROP TABLE IF EXISTS "matriculas" CASCADE;
DROP TABLE IF EXISTS "asignaciones_docente" CASCADE;
DROP TABLE IF EXISTS "cursos" CASCADE;
DROP TABLE IF EXISTS "users" CASCADE;

--
-- Estructura y datos de la tabla: "users"
--

CREATE TABLE "users" (
"id" CHARACTER VARYING NOT NULL,
"email" CHARACTER VARYING NOT NULL,
"hashed_password" CHARACTER VARYING NOT NULL,
"nombre" CHARACTER VARYING NOT NULL,
"apellido" CHARACTER VARYING NOT NULL,
"rol" VARCHAR(255) NOT NULL,
"profilePicture" CHARACTER VARYING NULL,
"createdAt" TIMESTAMP WITH TIME ZONE NULL DEFAULT now(),
"codigo" CHARACTER VARYING NULL,
"carrera" CHARACTER VARYING NULL,
"ciclo" INTEGER NULL,
"especialidad" CHARACTER VARYING NULL,
"departamento" CHARACTER VARYING NULL,
"nivel_acceso" CHARACTER VARYING NULL,
"estado" CHARACTER VARYING NULL
);

-- Insertando datos de la tabla "users"
INSERT INTO "users" ("id", "email", "hashed_password", "nombre", "apellido", "rol", "profilePicture", "createdAt", "codigo", "carrera", "ciclo", "especialidad", "departamento", "nivel_acceso", "estado") VALUES ('admin-1', 'admin@nuevaschool.pe', '$2b$12$qPQxaSw3dUx4Ij35Vqh7eOVrQcT/fUCfScMjKv7ScoqWlp9DK7TzK', 'Carlos', 'Huamán', 'ADMIN', NULL, '2026-07-02 02:15:27.135548+00:00', 'A26001', NULL, NULL, NULL, NULL, 'super', 'activo');
INSERT INTO "users" ("id", "email", "hashed_password", "nombre", "apellido", "rol", "profilePicture", "createdAt", "codigo", "carrera", "ciclo", "especialidad", "departamento", "nivel_acceso", "estado") VALUES ('docente-1', 'docente@nuevaschool.pe', '$2b$12$BwPpq/TWT/sPNQYxcv/apuiB2FS5wddFLEi9oWyDNd1ONGxYp5HsS', 'Juan', 'Pérez', 'DOCENTE', NULL, '2026-07-02 02:15:27.135548+00:00', 'D26001', NULL, NULL, 'Desarrollo de Software', 'Ingeniería', NULL, 'activo');
INSERT INTO "users" ("id", "email", "hashed_password", "nombre", "apellido", "rol", "profilePicture", "createdAt", "codigo", "carrera", "ciclo", "especialidad", "departamento", "nivel_acceso", "estado") VALUES ('docente-2', 'D26002@nuevaschool.pe', '$2b$12$jGGgBjw5ftDiBEpNyAL6eu434sfDfYCFr1Z9Ge001rQ9Sk15X1sZy', 'María', 'García', 'DOCENTE', NULL, '2026-07-02 02:15:27.135548+00:00', 'D26002', NULL, NULL, 'Matemáticas y Estadística', 'Ciencias', NULL, 'activo');
INSERT INTO "users" ("id", "email", "hashed_password", "nombre", "apellido", "rol", "profilePicture", "createdAt", "codigo", "carrera", "ciclo", "especialidad", "departamento", "nivel_acceso", "estado") VALUES ('docente-3', 'D26003@nuevaschool.pe', '$2b$12$NceEbvTfgy2vsPmGchTQ3ueLekHLmmorBWhm9Tp1d2O90jnIdF976', 'Luis', 'López', 'DOCENTE', NULL, '2026-07-02 02:15:27.135548+00:00', 'D26003', NULL, NULL, 'Idiomas', 'Humanidades', NULL, 'activo');
INSERT INTO "users" ("id", "email", "hashed_password", "nombre", "apellido", "rol", "profilePicture", "createdAt", "codigo", "carrera", "ciclo", "especialidad", "departamento", "nivel_acceso", "estado") VALUES ('estudiante-1', 'estudiante@nuevaschool.pe', '$2b$12$Dikkk/21cCn/dmnOfH6yKukrX.rWuccmojms0yZUs75AxHul2O/Aa', 'Pedro', 'Rodríguez', 'ESTUDIANTE', NULL, '2026-07-02 02:15:27.135548+00:00', 'U26001', 'Ingeniería de Sistemas e Informática', 5, NULL, NULL, NULL, 'activo');
INSERT INTO "users" ("id", "email", "hashed_password", "nombre", "apellido", "rol", "profilePicture", "createdAt", "codigo", "carrera", "ciclo", "especialidad", "departamento", "nivel_acceso", "estado") VALUES ('estudiante-2', 'U26002@nuevaschool.pe', '$2b$12$0lVN2bdKzYNbAt6yFgZPFeBNg.m0MCeqLvOGb6vh.5zcVJWoskabK', 'Ana', 'Martínez', 'ESTUDIANTE', NULL, '2026-07-02 02:15:27.135548+00:00', 'U26002', 'Ingeniería de Sistemas e Informática', 5, NULL, NULL, NULL, 'activo');
INSERT INTO "users" ("id", "email", "hashed_password", "nombre", "apellido", "rol", "profilePicture", "createdAt", "codigo", "carrera", "ciclo", "especialidad", "departamento", "nivel_acceso", "estado") VALUES ('estudiante-3', 'U26003@nuevaschool.pe', '$2b$12$ppfwY4Ptvp537zm68oiSW.xAq4Hzs3jUSrP2ToNwj4zgS8Vf/h7Ne', 'Carlos', 'López', 'ESTUDIANTE', NULL, '2026-07-02 02:15:27.135548+00:00', 'U26003', 'Ingeniería de Sistemas e Informática', 5, NULL, NULL, NULL, 'activo');
INSERT INTO "users" ("id", "email", "hashed_password", "nombre", "apellido", "rol", "profilePicture", "createdAt", "codigo", "carrera", "ciclo", "especialidad", "departamento", "nivel_acceso", "estado") VALUES ('estudiante-4', 'U26004@nuevaschool.pe', '$2b$12$yNECU5Vk25k56/K.u6Z9PubDLebC0uTUiufcmVXyqpxPzcv36R/a6', 'Diana', 'Soto', 'ESTUDIANTE', NULL, '2026-07-02 02:15:27.135548+00:00', 'U26004', 'Administración de Empresas', 3, NULL, NULL, NULL, 'activo');
INSERT INTO "users" ("id", "email", "hashed_password", "nombre", "apellido", "rol", "profilePicture", "createdAt", "codigo", "carrera", "ciclo", "especialidad", "departamento", "nivel_acceso", "estado") VALUES ('estudiante-5', 'U26005@nuevaschool.pe', '$2b$12$3TuZ9iQcYhuoPGuAKiPLYOGQw35LVVJJzr7KyifSo8XMTiB7xKAO6', 'Gabriel', 'Quispe', 'ESTUDIANTE', NULL, '2026-07-02 02:15:27.135548+00:00', 'U26005', 'Ingeniería de Sistemas e Informática', 7, NULL, NULL, NULL, 'activo');
INSERT INTO "users" ("id", "email", "hashed_password", "nombre", "apellido", "rol", "profilePicture", "createdAt", "codigo", "carrera", "ciclo", "especialidad", "departamento", "nivel_acceso", "estado") VALUES ('estudiante-6', 'U26006@nuevaschool.pe', '$2b$12$6IhcfjhyOmRUas/SbajSfud.JxZVX9CRefWgLS7M8kt.q27ze7p8y', 'Francisco', 'Flores', 'ESTUDIANTE', NULL, '2026-07-02 02:15:27.135548+00:00', 'U26006', 'Administración de Empresas', 3, NULL, NULL, NULL, 'activo');
INSERT INTO "users" ("id", "email", "hashed_password", "nombre", "apellido", "rol", "profilePicture", "createdAt", "codigo", "carrera", "ciclo", "especialidad", "departamento", "nivel_acceso", "estado") VALUES ('estudiante-7', 'U26007@nuevaschool.pe', '$2b$12$s586Rr9ONHi8mjxCKtU3BukSWd8VUdfdL.e381DZcZRfdplrcHEoy', 'Gloria', 'Ruiz', 'ESTUDIANTE', NULL, '2026-07-02 02:15:27.135548+00:00', 'U26007', 'Ingeniería de Sistemas e Informática', 5, NULL, NULL, NULL, 'activo');
INSERT INTO "users" ("id", "email", "hashed_password", "nombre", "apellido", "rol", "profilePicture", "createdAt", "codigo", "carrera", "ciclo", "especialidad", "departamento", "nivel_acceso", "estado") VALUES ('estudiante-8', 'U26008@nuevaschool.pe', '$2b$12$fxkVgGi7J6hcJMtI96KlQOIXOEggUWktVz56kEMaaZdVQghVsGBYK', 'Hernán', 'Mendoza', 'ESTUDIANTE', NULL, '2026-07-02 02:15:27.135548+00:00', 'U26008', 'Administración de Empresas', 2, NULL, NULL, NULL, 'activo');
INSERT INTO "users" ("id", "email", "hashed_password", "nombre", "apellido", "rol", "profilePicture", "createdAt", "codigo", "carrera", "ciclo", "especialidad", "departamento", "nivel_acceso", "estado") VALUES ('estudiante-9', 'U26009@nuevaschool.pe', '$2b$12$2mVpzIDxbHBTzbcM71z9hOn/x.X82n9wAM701pGcoz5X73u0mILtu', 'Iris', 'Condori', 'ESTUDIANTE', NULL, '2026-07-02 02:15:27.135548+00:00', 'U26009', 'Ingeniería de Sistemas e Informática', 5, NULL, NULL, NULL, 'activo');
INSERT INTO "users" ("id", "email", "hashed_password", "nombre", "apellido", "rol", "profilePicture", "createdAt", "codigo", "carrera", "ciclo", "especialidad", "departamento", "nivel_acceso", "estado") VALUES ('b56cdcc8-93ab-4f96-87bf-4d36c49ae394', 'u26011@nuevaschool.pe', '$2b$12$mmBK9tNubg.hxwJQcCCdjOFmwwptGDGwvROTHMBOgP7v.szNPuQDG', 'Edu', 'Morales Carlos', 'ESTUDIANTE', 'data:image/jpeg;base64,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', '2026-07-02 02:19:02.112660+00:00', 'U26011', 'Ingeniería de Software', 3, NULL, NULL, NULL, 'activo');
INSERT INTO "users" ("id", "email", "hashed_password", "nombre", "apellido", "rol", "profilePicture", "createdAt", "codigo", "carrera", "ciclo", "especialidad", "departamento", "nivel_acceso", "estado") VALUES ('estudiante-10', 'u26010@nuevaschool.pe', '$2b$12$WlChBKsXfo.l9Nl79w5y5eUE7Fhpcg4rALkBUYpogDjBJAdzUsL.K', 'José', 'Torres', 'ESTUDIANTE', NULL, '2026-07-02 02:15:27.135548+00:00', 'U26010', 'Administración de Empresas', 4, NULL, NULL, NULL, 'activo');
INSERT INTO "users" ("id", "email", "hashed_password", "nombre", "apellido", "rol", "profilePicture", "createdAt", "codigo", "carrera", "ciclo", "especialidad", "departamento", "nivel_acceso", "estado") VALUES ('f320ac55-9f14-4011-b5b7-663382bca740', 'u26012@nuevaschool.pe', '$2b$12$pR8UZmsWEyhiLzk3H5Uw7eyQ8wmLFt07ZbPqB/ts0W8pz0RQ6NqA6', 'Paco', 'Yunque', 'ESTUDIANTE', NULL, '2026-07-10 17:04:28.706445+00:00', 'U26012', 'Arquitectura', 1, NULL, NULL, NULL, 'activo');

--
-- Estructura y datos de la tabla: "cursos"
--

CREATE TABLE "cursos" (
"id" CHARACTER VARYING NOT NULL,
"nombre" CHARACTER VARYING NOT NULL,
"codigo" CHARACTER VARYING NULL,
"creditos" INTEGER NULL,
"ciclo" INTEGER NULL,
"modalidad" VARCHAR(255) NULL,
"zoom_link" CHARACTER VARYING NULL,
"createdAt" TIMESTAMP WITH TIME ZONE NULL DEFAULT now(),
"carreras" CHARACTER VARYING NULL
);

-- Insertando datos de la tabla "cursos"
INSERT INTO "cursos" ("id", "nombre", "codigo", "creditos", "ciclo", "modalidad", "zoom_link", "createdAt", "carreras") VALUES ('curso-1', 'Programación I', 'INF101', 4, 1, 'presencial', NULL, '2026-07-02 02:15:27.692409+00:00', 'Ingeniería de Sistemas e Informática,Ingeniería de Software');
INSERT INTO "cursos" ("id", "nombre", "codigo", "creditos", "ciclo", "modalidad", "zoom_link", "createdAt", "carreras") VALUES ('curso-2', 'Programación II', 'INF202', 4, 3, 'presencial', NULL, '2026-07-02 02:15:27.692409+00:00', 'Ingeniería de Sistemas e Informática,Ingeniería de Software');
INSERT INTO "cursos" ("id", "nombre", "codigo", "creditos", "ciclo", "modalidad", "zoom_link", "createdAt", "carreras") VALUES ('curso-3', 'Base de Datos', 'INF301', 3, 5, 'presencial', NULL, '2026-07-02 02:15:27.692409+00:00', 'Ingeniería de Sistemas e Informática,Ingeniería de Software');
INSERT INTO "cursos" ("id", "nombre", "codigo", "creditos", "ciclo", "modalidad", "zoom_link", "createdAt", "carreras") VALUES ('curso-4', 'Cálculo I', 'MAT101', 4, 1, 'presencial', NULL, '2026-07-02 02:15:27.692409+00:00', 'Ingeniería de Sistemas e Informática,Ingeniería de Software,Administración de Empresas,Contabilidad');
INSERT INTO "cursos" ("id", "nombre", "codigo", "creditos", "ciclo", "modalidad", "zoom_link", "createdAt", "carreras") VALUES ('curso-5', 'Inglés I', 'ENG101', 2, 1, 'presencial', NULL, '2026-07-02 02:15:27.692409+00:00', 'Ingeniería de Sistemas e Informática,Ingeniería de Software,Administración de Empresas,Contabilidad');
INSERT INTO "cursos" ("id", "nombre", "codigo", "creditos", "ciclo", "modalidad", "zoom_link", "createdAt", "carreras") VALUES ('a0b5878f-b5e1-4057-9730-cab4ffd93146', 'Herramientas de Desarrollo', 'HDE-601', 3, 6, 'presencial', NULL, '2026-07-02 02:21:10.202276+00:00', 'Ingeniería de Sistemas e Informática,Ingeniería de Software');
INSERT INTO "cursos" ("id", "nombre", "codigo", "creditos", "ciclo", "modalidad", "zoom_link", "createdAt", "carreras") VALUES ('4d01a143-9420-4a0e-9e5a-a4bd691146da', 'Algebra', 'ALG-101', 3, 1, 'presencial', NULL, '2026-07-10 17:00:36.835858+00:00', 'Ingeniería Aeronáutica,Administración Hotelera y de Turismo');
INSERT INTO "cursos" ("id", "nombre", "codigo", "creditos", "ciclo", "modalidad", "zoom_link", "createdAt", "carreras") VALUES ('14af2354-6542-49da-aee0-70e35be32d51', 'matematica 3', 'MAT-1001', 3, 10, 'presencial', NULL, '2026-07-10 17:05:42.224410+00:00', 'Educación Primaria,Ingeniería Aeronáutica,Ingeniería Ambiental');

--
-- Estructura y datos de la tabla: "asignaciones_docente"
--

CREATE TABLE "asignaciones_docente" (
"id" CHARACTER VARYING NOT NULL,
"docente_id" CHARACTER VARYING NULL,
"curso_id" CHARACTER VARYING NULL,
"fecha_asignacion" TIMESTAMP WITH TIME ZONE NULL DEFAULT now()
);

-- Insertando datos de la tabla "asignaciones_docente"
INSERT INTO "asignaciones_docente" ("id", "docente_id", "curso_id", "fecha_asignacion") VALUES ('ab9900b0-80b4-4290-8dc5-321ffc6e7378', 'docente-1', 'curso-1', '2026-07-02 02:15:27.692409+00:00');
INSERT INTO "asignaciones_docente" ("id", "docente_id", "curso_id", "fecha_asignacion") VALUES ('45e1c57e-108d-4725-8d16-7dd0146c91f6', 'docente-1', 'curso-2', '2026-07-02 02:15:27.692409+00:00');
INSERT INTO "asignaciones_docente" ("id", "docente_id", "curso_id", "fecha_asignacion") VALUES ('468c3355-8af4-4018-99f4-47a77f1beebd', 'docente-1', 'curso-3', '2026-07-02 02:15:27.692409+00:00');
INSERT INTO "asignaciones_docente" ("id", "docente_id", "curso_id", "fecha_asignacion") VALUES ('ebce5a16-245e-406d-a3f6-dad4e78732de', 'docente-2', 'curso-4', '2026-07-02 02:15:27.692409+00:00');
INSERT INTO "asignaciones_docente" ("id", "docente_id", "curso_id", "fecha_asignacion") VALUES ('638f64b1-faf9-46fc-854a-5c97da9bed38', 'docente-3', 'curso-5', '2026-07-02 02:15:27.692409+00:00');
INSERT INTO "asignaciones_docente" ("id", "docente_id", "curso_id", "fecha_asignacion") VALUES ('b1b3739f-6b72-4f5b-8493-19b68faf1502', 'docente-1', 'a0b5878f-b5e1-4057-9730-cab4ffd93146', '2026-07-02 02:21:10.573725+00:00');
INSERT INTO "asignaciones_docente" ("id", "docente_id", "curso_id", "fecha_asignacion") VALUES ('c8d3f574-5325-4c95-bcf4-54ad7668efeb', 'docente-2', '4d01a143-9420-4a0e-9e5a-a4bd691146da', '2026-07-10 17:00:37.280879+00:00');
INSERT INTO "asignaciones_docente" ("id", "docente_id", "curso_id", "fecha_asignacion") VALUES ('be491251-fa63-4ab0-a49d-67241f3b453d', 'docente-2', '14af2354-6542-49da-aee0-70e35be32d51', '2026-07-10 17:05:42.641611+00:00');

--
-- Estructura y datos de la tabla: "matriculas"
--

CREATE TABLE "matriculas" (
"id" CHARACTER VARYING NOT NULL,
"estudiante_id" CHARACTER VARYING NULL,
"curso_id" CHARACTER VARYING NULL,
"fecha_matricula" TIMESTAMP WITH TIME ZONE NULL DEFAULT now(),
"estado" VARCHAR(255) NULL
);

-- Insertando datos de la tabla "matriculas"
INSERT INTO "matriculas" ("id", "estudiante_id", "curso_id", "fecha_matricula", "estado") VALUES ('mat-1', 'estudiante-1', 'curso-3', '2026-07-02 02:15:28.435296+00:00', 'activo');
INSERT INTO "matriculas" ("id", "estudiante_id", "curso_id", "fecha_matricula", "estado") VALUES ('mat-2', 'estudiante-2', 'curso-3', '2026-07-02 02:15:28.435296+00:00', 'activo');
INSERT INTO "matriculas" ("id", "estudiante_id", "curso_id", "fecha_matricula", "estado") VALUES ('mat-3', 'estudiante-3', 'curso-3', '2026-07-02 02:15:28.435296+00:00', 'activo');
INSERT INTO "matriculas" ("id", "estudiante_id", "curso_id", "fecha_matricula", "estado") VALUES ('mat-5', 'estudiante-2', 'curso-1', '2026-07-02 02:15:28.435296+00:00', 'activo');
INSERT INTO "matriculas" ("id", "estudiante_id", "curso_id", "fecha_matricula", "estado") VALUES ('mat-6', 'estudiante-7', 'curso-3', '2026-07-02 02:15:28.435296+00:00', 'activo');
INSERT INTO "matriculas" ("id", "estudiante_id", "curso_id", "fecha_matricula", "estado") VALUES ('mat-7', 'estudiante-9', 'curso-3', '2026-07-02 02:15:28.435296+00:00', 'activo');
INSERT INTO "matriculas" ("id", "estudiante_id", "curso_id", "fecha_matricula", "estado") VALUES ('mat-8', 'estudiante-4', 'curso-1', '2026-07-02 02:15:28.435296+00:00', 'activo');
INSERT INTO "matriculas" ("id", "estudiante_id", "curso_id", "fecha_matricula", "estado") VALUES ('8b70c99b-d149-40a1-b1b1-2f1bbb61705a', 'b56cdcc8-93ab-4f96-87bf-4d36c49ae394', 'a0b5878f-b5e1-4057-9730-cab4ffd93146', '2026-07-02 02:21:21.173571+00:00', 'activo');
INSERT INTO "matriculas" ("id", "estudiante_id", "curso_id", "fecha_matricula", "estado") VALUES ('030a2b9a-71d0-4074-a415-7b0c8c2149c4', 'estudiante-1', 'curso-1', '2026-07-02 02:45:18.541119+00:00', 'activo');
INSERT INTO "matriculas" ("id", "estudiante_id", "curso_id", "fecha_matricula", "estado") VALUES ('23bdc867-6779-4340-9900-6017d736cd9d', 'b56cdcc8-93ab-4f96-87bf-4d36c49ae394', 'curso-1', '2026-07-02 05:44:58.183740+00:00', 'activo');

--
-- Estructura y datos de la tabla: "notas"
--

CREATE TABLE "notas" (
"id" CHARACTER VARYING NOT NULL,
"matricula_id" CHARACTER VARYING NULL,
"tipo" CHARACTER VARYING NULL,
"calificacion" DOUBLE PRECISION NULL,
"peso" DOUBLE PRECISION NULL,
"fecha" TIMESTAMP WITH TIME ZONE NULL DEFAULT now()
);

-- Insertando datos de la tabla "notas"
INSERT INTO "notas" ("id", "matricula_id", "tipo", "calificacion", "peso", "fecha") VALUES ('nota-1', 'mat-1', 'parcial', 15.0, 15.0, '2026-07-02 02:15:28.992744+00:00');
INSERT INTO "notas" ("id", "matricula_id", "tipo", "calificacion", "peso", "fecha") VALUES ('nota-2', 'mat-1', 'practica', 17.0, 35.0, '2026-07-02 02:15:28.992744+00:00');
INSERT INTO "notas" ("id", "matricula_id", "tipo", "calificacion", "peso", "fecha") VALUES ('nota-3', 'mat-1', 'final', 16.0, 50.0, '2026-07-02 02:15:28.992744+00:00');
INSERT INTO "notas" ("id", "matricula_id", "tipo", "calificacion", "peso", "fecha") VALUES ('nota-4', 'mat-2', 'parcial', 14.0, 15.0, '2026-07-02 02:15:28.992744+00:00');
INSERT INTO "notas" ("id", "matricula_id", "tipo", "calificacion", "peso", "fecha") VALUES ('nota-5', 'mat-2', 'practica', 16.0, 35.0, '2026-07-02 02:15:28.992744+00:00');
INSERT INTO "notas" ("id", "matricula_id", "tipo", "calificacion", "peso", "fecha") VALUES ('nota-6', 'mat-2', 'final', 15.0, 50.0, '2026-07-02 02:15:28.992744+00:00');
INSERT INTO "notas" ("id", "matricula_id", "tipo", "calificacion", "peso", "fecha") VALUES ('nota-7', 'mat-3', 'parcial', 18.0, 15.0, '2026-07-02 02:15:28.992744+00:00');
INSERT INTO "notas" ("id", "matricula_id", "tipo", "calificacion", "peso", "fecha") VALUES ('nota-8', 'mat-3', 'practica', 19.0, 35.0, '2026-07-02 02:15:28.992744+00:00');
INSERT INTO "notas" ("id", "matricula_id", "tipo", "calificacion", "peso", "fecha") VALUES ('nota-9', 'mat-3', 'final', 18.0, 50.0, '2026-07-02 02:15:28.992744+00:00');
INSERT INTO "notas" ("id", "matricula_id", "tipo", "calificacion", "peso", "fecha") VALUES ('nota-12', 'mat-5', 'parcial', 13.0, 15.0, '2026-07-02 02:15:28.992744+00:00');
INSERT INTO "notas" ("id", "matricula_id", "tipo", "calificacion", "peso", "fecha") VALUES ('nota-13', 'mat-5', 'practica', 14.0, 35.0, '2026-07-02 02:15:28.992744+00:00');
INSERT INTO "notas" ("id", "matricula_id", "tipo", "calificacion", "peso", "fecha") VALUES ('nota-10', NULL, 'parcial', 16.0, 15.0, '2026-07-02 02:15:28.992744+00:00');
INSERT INTO "notas" ("id", "matricula_id", "tipo", "calificacion", "peso", "fecha") VALUES ('nota-11', NULL, 'practica', 18.0, 35.0, '2026-07-02 02:15:28.992744+00:00');

--
-- Estructura y datos de la tabla: "contenidos_semana"
--

CREATE TABLE "contenidos_semana" (
"id" CHARACTER VARYING NOT NULL,
"curso_id" CHARACTER VARYING NULL,
"semana_numero" INTEGER NOT NULL,
"titulo" CHARACTER VARYING NOT NULL,
"descripcion" CHARACTER VARYING NULL,
"archivo_url" CHARACTER VARYING NULL,
"createdAt" TIMESTAMP WITH TIME ZONE NULL DEFAULT now()
);

-- Insertando datos de la tabla "contenidos_semana"
INSERT INTO "contenidos_semana" ("id", "curso_id", "semana_numero", "titulo", "descripcion", "archivo_url", "createdAt") VALUES ('80358c2d-82ab-4a56-a6eb-2277bf6f3a99', 'curso-1', 1, 'Semana 1: Introducción y Fundamentos', 'En esta semana se revisarán los conceptos básicos del tema de la unidad 1.', NULL, '2026-07-02 02:15:31.233358+00:00');
INSERT INTO "contenidos_semana" ("id", "curso_id", "semana_numero", "titulo", "descripcion", "archivo_url", "createdAt") VALUES ('db7f5eb6-351d-4c16-946c-1e5c4c5abd8c', 'curso-1', 2, 'Semana 2: Introducción y Fundamentos', 'En esta semana se revisarán los conceptos básicos del tema de la unidad 2.', NULL, '2026-07-02 02:15:31.233358+00:00');
INSERT INTO "contenidos_semana" ("id", "curso_id", "semana_numero", "titulo", "descripcion", "archivo_url", "createdAt") VALUES ('91a1e260-af68-45f8-afcc-5b18d49f2369', 'curso-1', 3, 'Semana 3: Introducción y Fundamentos', 'En esta semana se revisarán los conceptos básicos del tema de la unidad 3.', NULL, '2026-07-02 02:15:31.233358+00:00');
INSERT INTO "contenidos_semana" ("id", "curso_id", "semana_numero", "titulo", "descripcion", "archivo_url", "createdAt") VALUES ('856a9e28-55e6-41a7-9839-a028d0d6b8bb', 'curso-1', 4, 'Semana 4: Introducción y Fundamentos', 'En esta semana se revisarán los conceptos básicos del tema de la unidad 4.', NULL, '2026-07-02 02:15:31.233358+00:00');
INSERT INTO "contenidos_semana" ("id", "curso_id", "semana_numero", "titulo", "descripcion", "archivo_url", "createdAt") VALUES ('fad387cf-53f2-4c27-806c-5e0572bd7c48', 'curso-1', 5, 'Semana 5: Introducción y Fundamentos', 'En esta semana se revisarán los conceptos básicos del tema de la unidad 5.', NULL, '2026-07-02 02:15:31.233358+00:00');
INSERT INTO "contenidos_semana" ("id", "curso_id", "semana_numero", "titulo", "descripcion", "archivo_url", "createdAt") VALUES ('48adad0a-e654-4606-af6d-4406c299bf14', 'curso-1', 6, 'Semana 6: Introducción y Fundamentos', 'En esta semana se revisarán los conceptos básicos del tema de la unidad 6.', NULL, '2026-07-02 02:15:31.233358+00:00');
INSERT INTO "contenidos_semana" ("id", "curso_id", "semana_numero", "titulo", "descripcion", "archivo_url", "createdAt") VALUES ('cfe4f2ee-68be-4cf9-be5c-6cf68545da26', 'curso-1', 7, 'Semana 7: Introducción y Fundamentos', 'En esta semana se revisarán los conceptos básicos del tema de la unidad 7.', NULL, '2026-07-02 02:15:31.233358+00:00');
INSERT INTO "contenidos_semana" ("id", "curso_id", "semana_numero", "titulo", "descripcion", "archivo_url", "createdAt") VALUES ('ee5d45d8-0020-4205-8f9a-9bc1a0a355b4', 'curso-1', 8, 'Semana 8: Introducción y Fundamentos', 'En esta semana se revisarán los conceptos básicos del tema de la unidad 8.', NULL, '2026-07-02 02:15:31.233358+00:00');
INSERT INTO "contenidos_semana" ("id", "curso_id", "semana_numero", "titulo", "descripcion", "archivo_url", "createdAt") VALUES ('beccfd4b-98a2-49b3-8bf3-efeda879e93d', 'curso-1', 9, 'Semana 9: Introducción y Fundamentos', 'En esta semana se revisarán los conceptos básicos del tema de la unidad 9.', NULL, '2026-07-02 02:15:31.233358+00:00');
INSERT INTO "contenidos_semana" ("id", "curso_id", "semana_numero", "titulo", "descripcion", "archivo_url", "createdAt") VALUES ('c75d6d21-6880-47fd-896e-fa090c9e781f', 'curso-1', 10, 'Semana 10: Introducción y Fundamentos', 'En esta semana se revisarán los conceptos básicos del tema de la unidad 10.', NULL, '2026-07-02 02:15:31.233358+00:00');
INSERT INTO "contenidos_semana" ("id", "curso_id", "semana_numero", "titulo", "descripcion", "archivo_url", "createdAt") VALUES ('50039aa3-679a-40af-b169-cc9e99ee54d1', 'curso-1', 11, 'Semana 11: Introducción y Fundamentos', 'En esta semana se revisarán los conceptos básicos del tema de la unidad 11.', NULL, '2026-07-02 02:15:31.233358+00:00');
INSERT INTO "contenidos_semana" ("id", "curso_id", "semana_numero", "titulo", "descripcion", "archivo_url", "createdAt") VALUES ('7f1890b1-4a24-41f9-b5c0-9311cffeb114', 'curso-1', 12, 'Semana 12: Introducción y Fundamentos', 'En esta semana se revisarán los conceptos básicos del tema de la unidad 12.', NULL, '2026-07-02 02:15:31.233358+00:00');
INSERT INTO "contenidos_semana" ("id", "curso_id", "semana_numero", "titulo", "descripcion", "archivo_url", "createdAt") VALUES ('6401c059-6c79-4694-9886-bc6a6aee4410', 'curso-1', 13, 'Semana 13: Introducción y Fundamentos', 'En esta semana se revisarán los conceptos básicos del tema de la unidad 13.', NULL, '2026-07-02 02:15:31.233358+00:00');
INSERT INTO "contenidos_semana" ("id", "curso_id", "semana_numero", "titulo", "descripcion", "archivo_url", "createdAt") VALUES ('748b9ded-b53d-4026-acdc-d966bb8053f3', 'curso-1', 14, 'Semana 14: Introducción y Fundamentos', 'En esta semana se revisarán los conceptos básicos del tema de la unidad 14.', NULL, '2026-07-02 02:15:31.233358+00:00');
INSERT INTO "contenidos_semana" ("id", "curso_id", "semana_numero", "titulo", "descripcion", "archivo_url", "createdAt") VALUES ('90bcff86-ebe4-4e3f-a636-b533dedf2caa', 'curso-1', 15, 'Semana 15: Introducción y Fundamentos', 'En esta semana se revisarán los conceptos básicos del tema de la unidad 15.', NULL, '2026-07-02 02:15:31.233358+00:00');
INSERT INTO "contenidos_semana" ("id", "curso_id", "semana_numero", "titulo", "descripcion", "archivo_url", "createdAt") VALUES ('e2939521-e8a7-4853-99f1-4e030a37bbc1', 'curso-1', 16, 'Semana 16: Introducción y Fundamentos', 'En esta semana se revisarán los conceptos básicos del tema de la unidad 16.', NULL, '2026-07-02 02:15:31.233358+00:00');
INSERT INTO "contenidos_semana" ("id", "curso_id", "semana_numero", "titulo", "descripcion", "archivo_url", "createdAt") VALUES ('73c04464-b719-4028-89b5-474c31499268', 'curso-1', 17, 'Semana 17: Introducción y Fundamentos', 'En esta semana se revisarán los conceptos básicos del tema de la unidad 17.', NULL, '2026-07-02 02:15:31.233358+00:00');
INSERT INTO "contenidos_semana" ("id", "curso_id", "semana_numero", "titulo", "descripcion", "archivo_url", "createdAt") VALUES ('b86aac76-4cfe-4bd8-a833-5173be4dfbd2', 'curso-1', 18, 'Semana 18: Introducción y Fundamentos', 'En esta semana se revisarán los conceptos básicos del tema de la unidad 18.', NULL, '2026-07-02 02:15:31.233358+00:00');
INSERT INTO "contenidos_semana" ("id", "curso_id", "semana_numero", "titulo", "descripcion", "archivo_url", "createdAt") VALUES ('95d2efbb-df00-4e18-947d-783d659bc257', 'curso-2', 1, 'Semana 1: Introducción y Fundamentos', 'En esta semana se revisarán los conceptos básicos del tema de la unidad 1.', NULL, '2026-07-02 02:15:31.233358+00:00');
INSERT INTO "contenidos_semana" ("id", "curso_id", "semana_numero", "titulo", "descripcion", "archivo_url", "createdAt") VALUES ('01485f10-b5da-4747-9ff3-802759a7aec5', 'curso-2', 2, 'Semana 2: Introducción y Fundamentos', 'En esta semana se revisarán los conceptos básicos del tema de la unidad 2.', NULL, '2026-07-02 02:15:31.233358+00:00');
INSERT INTO "contenidos_semana" ("id", "curso_id", "semana_numero", "titulo", "descripcion", "archivo_url", "createdAt") VALUES ('6f1ac97c-c6b3-4654-9a27-1bd98376f7ce', 'curso-2', 3, 'Semana 3: Introducción y Fundamentos', 'En esta semana se revisarán los conceptos básicos del tema de la unidad 3.', NULL, '2026-07-02 02:15:31.233358+00:00');
INSERT INTO "contenidos_semana" ("id", "curso_id", "semana_numero", "titulo", "descripcion", "archivo_url", "createdAt") VALUES ('0fb56c8e-6ad6-4266-8c5d-c16e11665cdb', 'curso-2', 4, 'Semana 4: Introducción y Fundamentos', 'En esta semana se revisarán los conceptos básicos del tema de la unidad 4.', NULL, '2026-07-02 02:15:31.233358+00:00');
INSERT INTO "contenidos_semana" ("id", "curso_id", "semana_numero", "titulo", "descripcion", "archivo_url", "createdAt") VALUES ('b721e0e7-6f59-4bd9-8e1d-423d3bebe0e8', 'curso-2', 5, 'Semana 5: Introducción y Fundamentos', 'En esta semana se revisarán los conceptos básicos del tema de la unidad 5.', NULL, '2026-07-02 02:15:31.233358+00:00');
INSERT INTO "contenidos_semana" ("id", "curso_id", "semana_numero", "titulo", "descripcion", "archivo_url", "createdAt") VALUES ('2d028e41-90e4-4222-9565-b5f2ea650a73', 'curso-2', 6, 'Semana 6: Introducción y Fundamentos', 'En esta semana se revisarán los conceptos básicos del tema de la unidad 6.', NULL, '2026-07-02 02:15:31.233358+00:00');
INSERT INTO "contenidos_semana" ("id", "curso_id", "semana_numero", "titulo", "descripcion", "archivo_url", "createdAt") VALUES ('bcc4b393-5b84-40e6-afcd-0bd8e145d215', 'curso-2', 7, 'Semana 7: Introducción y Fundamentos', 'En esta semana se revisarán los conceptos básicos del tema de la unidad 7.', NULL, '2026-07-02 02:15:31.233358+00:00');
INSERT INTO "contenidos_semana" ("id", "curso_id", "semana_numero", "titulo", "descripcion", "archivo_url", "createdAt") VALUES ('f43c44ed-aca8-4cc4-bf52-2dca4c553bd8', 'curso-2', 8, 'Semana 8: Introducción y Fundamentos', 'En esta semana se revisarán los conceptos básicos del tema de la unidad 8.', NULL, '2026-07-02 02:15:31.233358+00:00');
INSERT INTO "contenidos_semana" ("id", "curso_id", "semana_numero", "titulo", "descripcion", "archivo_url", "createdAt") VALUES ('5132da98-b849-4bde-a2b5-659512935175', 'curso-2', 9, 'Semana 9: Introducción y Fundamentos', 'En esta semana se revisarán los conceptos básicos del tema de la unidad 9.', NULL, '2026-07-02 02:15:31.233358+00:00');
INSERT INTO "contenidos_semana" ("id", "curso_id", "semana_numero", "titulo", "descripcion", "archivo_url", "createdAt") VALUES ('b4e1373e-5910-45c3-90c8-07758af76953', 'curso-2', 10, 'Semana 10: Introducción y Fundamentos', 'En esta semana se revisarán los conceptos básicos del tema de la unidad 10.', NULL, '2026-07-02 02:15:31.233358+00:00');
INSERT INTO "contenidos_semana" ("id", "curso_id", "semana_numero", "titulo", "descripcion", "archivo_url", "createdAt") VALUES ('d8735a0c-3587-4733-b4e8-e37ed07a451e', 'curso-2', 11, 'Semana 11: Introducción y Fundamentos', 'En esta semana se revisarán los conceptos básicos del tema de la unidad 11.', NULL, '2026-07-02 02:15:31.233358+00:00');
INSERT INTO "contenidos_semana" ("id", "curso_id", "semana_numero", "titulo", "descripcion", "archivo_url", "createdAt") VALUES ('635c1e60-7765-4aa8-9a33-ad0f0350b344', 'curso-2', 12, 'Semana 12: Introducción y Fundamentos', 'En esta semana se revisarán los conceptos básicos del tema de la unidad 12.', NULL, '2026-07-02 02:15:31.233358+00:00');
INSERT INTO "contenidos_semana" ("id", "curso_id", "semana_numero", "titulo", "descripcion", "archivo_url", "createdAt") VALUES ('a985981b-e481-4b92-a613-1e6d3bd4ee7f', 'curso-2', 13, 'Semana 13: Introducción y Fundamentos', 'En esta semana se revisarán los conceptos básicos del tema de la unidad 13.', NULL, '2026-07-02 02:15:31.233358+00:00');
INSERT INTO "contenidos_semana" ("id", "curso_id", "semana_numero", "titulo", "descripcion", "archivo_url", "createdAt") VALUES ('b91f3f95-ab2b-4962-97ca-b5385b102f2c', 'curso-2', 14, 'Semana 14: Introducción y Fundamentos', 'En esta semana se revisarán los conceptos básicos del tema de la unidad 14.', NULL, '2026-07-02 02:15:31.233358+00:00');
INSERT INTO "contenidos_semana" ("id", "curso_id", "semana_numero", "titulo", "descripcion", "archivo_url", "createdAt") VALUES ('794b5cc1-3fa2-47ad-b6f5-9876c63a08cc', 'curso-2', 15, 'Semana 15: Introducción y Fundamentos', 'En esta semana se revisarán los conceptos básicos del tema de la unidad 15.', NULL, '2026-07-02 02:15:31.233358+00:00');
INSERT INTO "contenidos_semana" ("id", "curso_id", "semana_numero", "titulo", "descripcion", "archivo_url", "createdAt") VALUES ('0f2d6430-9c6f-455c-84e1-5e842b01ce5e', 'curso-2', 16, 'Semana 16: Introducción y Fundamentos', 'En esta semana se revisarán los conceptos básicos del tema de la unidad 16.', NULL, '2026-07-02 02:15:31.233358+00:00');
INSERT INTO "contenidos_semana" ("id", "curso_id", "semana_numero", "titulo", "descripcion", "archivo_url", "createdAt") VALUES ('f548b180-e681-4631-8bad-fe3eaa8261f7', 'curso-2', 17, 'Semana 17: Introducción y Fundamentos', 'En esta semana se revisarán los conceptos básicos del tema de la unidad 17.', NULL, '2026-07-02 02:15:31.233358+00:00');
INSERT INTO "contenidos_semana" ("id", "curso_id", "semana_numero", "titulo", "descripcion", "archivo_url", "createdAt") VALUES ('858cca12-0e49-45ab-89d8-85edc7495d76', 'curso-2', 18, 'Semana 18: Introducción y Fundamentos', 'En esta semana se revisarán los conceptos básicos del tema de la unidad 18.', NULL, '2026-07-02 02:15:31.233358+00:00');
INSERT INTO "contenidos_semana" ("id", "curso_id", "semana_numero", "titulo", "descripcion", "archivo_url", "createdAt") VALUES ('d6d5a9e0-6405-4ab7-a666-f781900b4af5', 'curso-3', 1, 'Semana 1: Introducción y Fundamentos', 'En esta semana se revisarán los conceptos básicos del tema de la unidad 1.', NULL, '2026-07-02 02:15:31.233358+00:00');
INSERT INTO "contenidos_semana" ("id", "curso_id", "semana_numero", "titulo", "descripcion", "archivo_url", "createdAt") VALUES ('9ca1ee54-e773-4085-9544-bd863f74e142', 'curso-3', 2, 'Semana 2: Introducción y Fundamentos', 'En esta semana se revisarán los conceptos básicos del tema de la unidad 2.', NULL, '2026-07-02 02:15:31.233358+00:00');
INSERT INTO "contenidos_semana" ("id", "curso_id", "semana_numero", "titulo", "descripcion", "archivo_url", "createdAt") VALUES ('dc8bb78e-2696-4334-b4d5-a0f41a27e0eb', 'curso-3', 3, 'Semana 3: Introducción y Fundamentos', 'En esta semana se revisarán los conceptos básicos del tema de la unidad 3.', NULL, '2026-07-02 02:15:31.233358+00:00');
INSERT INTO "contenidos_semana" ("id", "curso_id", "semana_numero", "titulo", "descripcion", "archivo_url", "createdAt") VALUES ('5312b12d-831f-4044-bcc6-513631f2c250', 'curso-3', 4, 'Semana 4: Introducción y Fundamentos', 'En esta semana se revisarán los conceptos básicos del tema de la unidad 4.', NULL, '2026-07-02 02:15:31.233358+00:00');
INSERT INTO "contenidos_semana" ("id", "curso_id", "semana_numero", "titulo", "descripcion", "archivo_url", "createdAt") VALUES ('0a857867-863e-4e27-87a5-9e3de7b9a120', 'curso-3', 5, 'Semana 5: Introducción y Fundamentos', 'En esta semana se revisarán los conceptos básicos del tema de la unidad 5.', NULL, '2026-07-02 02:15:31.233358+00:00');
INSERT INTO "contenidos_semana" ("id", "curso_id", "semana_numero", "titulo", "descripcion", "archivo_url", "createdAt") VALUES ('0f8cfd21-27eb-4f7c-b834-f87a4f8c25f4', 'curso-3', 6, 'Semana 6: Introducción y Fundamentos', 'En esta semana se revisarán los conceptos básicos del tema de la unidad 6.', NULL, '2026-07-02 02:15:31.233358+00:00');
INSERT INTO "contenidos_semana" ("id", "curso_id", "semana_numero", "titulo", "descripcion", "archivo_url", "createdAt") VALUES ('204fc014-617a-45d2-809c-6633a63d2f43', 'curso-3', 7, 'Semana 7: Introducción y Fundamentos', 'En esta semana se revisarán los conceptos básicos del tema de la unidad 7.', NULL, '2026-07-02 02:15:31.233358+00:00');
INSERT INTO "contenidos_semana" ("id", "curso_id", "semana_numero", "titulo", "descripcion", "archivo_url", "createdAt") VALUES ('014d381e-16fb-490f-bf01-5f34ecda465b', 'curso-3', 8, 'Semana 8: Introducción y Fundamentos', 'En esta semana se revisarán los conceptos básicos del tema de la unidad 8.', NULL, '2026-07-02 02:15:31.233358+00:00');
INSERT INTO "contenidos_semana" ("id", "curso_id", "semana_numero", "titulo", "descripcion", "archivo_url", "createdAt") VALUES ('bff8e319-5fdc-4eaa-922e-97230f3412f0', 'curso-3', 9, 'Semana 9: Introducción y Fundamentos', 'En esta semana se revisarán los conceptos básicos del tema de la unidad 9.', NULL, '2026-07-02 02:15:31.233358+00:00');
INSERT INTO "contenidos_semana" ("id", "curso_id", "semana_numero", "titulo", "descripcion", "archivo_url", "createdAt") VALUES ('25ce2e0c-e146-41cd-8c1e-6c91a35b5532', 'curso-3', 10, 'Semana 10: Introducción y Fundamentos', 'En esta semana se revisarán los conceptos básicos del tema de la unidad 10.', NULL, '2026-07-02 02:15:31.233358+00:00');
INSERT INTO "contenidos_semana" ("id", "curso_id", "semana_numero", "titulo", "descripcion", "archivo_url", "createdAt") VALUES ('3f503287-ee0d-4c8f-a6f9-484724786118', 'curso-3', 11, 'Semana 11: Introducción y Fundamentos', 'En esta semana se revisarán los conceptos básicos del tema de la unidad 11.', NULL, '2026-07-02 02:15:31.233358+00:00');
INSERT INTO "contenidos_semana" ("id", "curso_id", "semana_numero", "titulo", "descripcion", "archivo_url", "createdAt") VALUES ('a8123b61-e94e-4829-9364-988ce2da7456', 'curso-3', 12, 'Semana 12: Introducción y Fundamentos', 'En esta semana se revisarán los conceptos básicos del tema de la unidad 12.', NULL, '2026-07-02 02:15:31.233358+00:00');
INSERT INTO "contenidos_semana" ("id", "curso_id", "semana_numero", "titulo", "descripcion", "archivo_url", "createdAt") VALUES ('5130d44e-0feb-4223-81d6-355cd75264e8', 'curso-3', 13, 'Semana 13: Introducción y Fundamentos', 'En esta semana se revisarán los conceptos básicos del tema de la unidad 13.', NULL, '2026-07-02 02:15:31.233358+00:00');
INSERT INTO "contenidos_semana" ("id", "curso_id", "semana_numero", "titulo", "descripcion", "archivo_url", "createdAt") VALUES ('7aea6cd6-3492-46c4-ac76-3a287737a50c', 'curso-3', 14, 'Semana 14: Introducción y Fundamentos', 'En esta semana se revisarán los conceptos básicos del tema de la unidad 14.', NULL, '2026-07-02 02:15:31.233358+00:00');
INSERT INTO "contenidos_semana" ("id", "curso_id", "semana_numero", "titulo", "descripcion", "archivo_url", "createdAt") VALUES ('6a129d92-aa9f-4df3-b41a-6f055f7ebfd7', 'curso-3', 15, 'Semana 15: Introducción y Fundamentos', 'En esta semana se revisarán los conceptos básicos del tema de la unidad 15.', NULL, '2026-07-02 02:15:31.233358+00:00');
INSERT INTO "contenidos_semana" ("id", "curso_id", "semana_numero", "titulo", "descripcion", "archivo_url", "createdAt") VALUES ('4ee5026c-3038-4d69-ab75-d30419def499', 'curso-3', 16, 'Semana 16: Introducción y Fundamentos', 'En esta semana se revisarán los conceptos básicos del tema de la unidad 16.', NULL, '2026-07-02 02:15:31.233358+00:00');
INSERT INTO "contenidos_semana" ("id", "curso_id", "semana_numero", "titulo", "descripcion", "archivo_url", "createdAt") VALUES ('94d2e76b-b2d9-4b70-b659-fbffb86e27f9', 'curso-3', 17, 'Semana 17: Introducción y Fundamentos', 'En esta semana se revisarán los conceptos básicos del tema de la unidad 17.', NULL, '2026-07-02 02:15:31.233358+00:00');
INSERT INTO "contenidos_semana" ("id", "curso_id", "semana_numero", "titulo", "descripcion", "archivo_url", "createdAt") VALUES ('415c6cd7-55f1-4b66-951f-f3bb488225a7', 'curso-3', 18, 'Semana 18: Introducción y Fundamentos', 'En esta semana se revisarán los conceptos básicos del tema de la unidad 18.', NULL, '2026-07-02 02:15:31.233358+00:00');
INSERT INTO "contenidos_semana" ("id", "curso_id", "semana_numero", "titulo", "descripcion", "archivo_url", "createdAt") VALUES ('b1290e27-733c-4798-afc7-388771eb0419', 'curso-4', 1, 'Semana 1: Introducción y Fundamentos', 'En esta semana se revisarán los conceptos básicos del tema de la unidad 1.', NULL, '2026-07-02 02:15:31.233358+00:00');
INSERT INTO "contenidos_semana" ("id", "curso_id", "semana_numero", "titulo", "descripcion", "archivo_url", "createdAt") VALUES ('b377cf37-9c6f-47de-bf9b-1ad5da844952', 'curso-4', 2, 'Semana 2: Introducción y Fundamentos', 'En esta semana se revisarán los conceptos básicos del tema de la unidad 2.', NULL, '2026-07-02 02:15:31.233358+00:00');
INSERT INTO "contenidos_semana" ("id", "curso_id", "semana_numero", "titulo", "descripcion", "archivo_url", "createdAt") VALUES ('72b2aaae-74b8-479c-9768-a1d2a0fd04e3', 'curso-4', 3, 'Semana 3: Introducción y Fundamentos', 'En esta semana se revisarán los conceptos básicos del tema de la unidad 3.', NULL, '2026-07-02 02:15:31.233358+00:00');
INSERT INTO "contenidos_semana" ("id", "curso_id", "semana_numero", "titulo", "descripcion", "archivo_url", "createdAt") VALUES ('ab2e5b88-344e-4d91-a72e-01fbf4876572', 'curso-4', 4, 'Semana 4: Introducción y Fundamentos', 'En esta semana se revisarán los conceptos básicos del tema de la unidad 4.', NULL, '2026-07-02 02:15:31.233358+00:00');
INSERT INTO "contenidos_semana" ("id", "curso_id", "semana_numero", "titulo", "descripcion", "archivo_url", "createdAt") VALUES ('4a1f5702-1fce-407a-b2b7-5fbde35c63d0', 'curso-4', 5, 'Semana 5: Introducción y Fundamentos', 'En esta semana se revisarán los conceptos básicos del tema de la unidad 5.', NULL, '2026-07-02 02:15:31.233358+00:00');
INSERT INTO "contenidos_semana" ("id", "curso_id", "semana_numero", "titulo", "descripcion", "archivo_url", "createdAt") VALUES ('5bb708ec-ae85-469e-9bfd-e5af1b9bdeaf', 'curso-4', 6, 'Semana 6: Introducción y Fundamentos', 'En esta semana se revisarán los conceptos básicos del tema de la unidad 6.', NULL, '2026-07-02 02:15:31.233358+00:00');
INSERT INTO "contenidos_semana" ("id", "curso_id", "semana_numero", "titulo", "descripcion", "archivo_url", "createdAt") VALUES ('f7c27c8f-54e5-4fbc-a6af-cdf45383d47f', 'curso-4', 7, 'Semana 7: Introducción y Fundamentos', 'En esta semana se revisarán los conceptos básicos del tema de la unidad 7.', NULL, '2026-07-02 02:15:31.233358+00:00');
INSERT INTO "contenidos_semana" ("id", "curso_id", "semana_numero", "titulo", "descripcion", "archivo_url", "createdAt") VALUES ('5b2c6318-05f7-45b4-9738-519c0ccc5a91', 'curso-4', 8, 'Semana 8: Introducción y Fundamentos', 'En esta semana se revisarán los conceptos básicos del tema de la unidad 8.', NULL, '2026-07-02 02:15:31.233358+00:00');
INSERT INTO "contenidos_semana" ("id", "curso_id", "semana_numero", "titulo", "descripcion", "archivo_url", "createdAt") VALUES ('4b3ac3e9-5a8b-42f5-a774-18f1c18a90ee', 'curso-4', 9, 'Semana 9: Introducción y Fundamentos', 'En esta semana se revisarán los conceptos básicos del tema de la unidad 9.', NULL, '2026-07-02 02:15:31.233358+00:00');
INSERT INTO "contenidos_semana" ("id", "curso_id", "semana_numero", "titulo", "descripcion", "archivo_url", "createdAt") VALUES ('855c0cff-ba2a-4b20-9254-c5abe82e96b2', 'curso-4', 10, 'Semana 10: Introducción y Fundamentos', 'En esta semana se revisarán los conceptos básicos del tema de la unidad 10.', NULL, '2026-07-02 02:15:31.233358+00:00');
INSERT INTO "contenidos_semana" ("id", "curso_id", "semana_numero", "titulo", "descripcion", "archivo_url", "createdAt") VALUES ('fc0fe530-24ce-4759-964d-02dd4b3f27bb', 'curso-4', 11, 'Semana 11: Introducción y Fundamentos', 'En esta semana se revisarán los conceptos básicos del tema de la unidad 11.', NULL, '2026-07-02 02:15:31.233358+00:00');
INSERT INTO "contenidos_semana" ("id", "curso_id", "semana_numero", "titulo", "descripcion", "archivo_url", "createdAt") VALUES ('f740581c-fdd9-4d39-a980-202d2041dc3d', 'curso-4', 12, 'Semana 12: Introducción y Fundamentos', 'En esta semana se revisarán los conceptos básicos del tema de la unidad 12.', NULL, '2026-07-02 02:15:31.233358+00:00');
INSERT INTO "contenidos_semana" ("id", "curso_id", "semana_numero", "titulo", "descripcion", "archivo_url", "createdAt") VALUES ('136b254e-467c-477e-86d7-baf7c3f586a1', 'curso-4', 13, 'Semana 13: Introducción y Fundamentos', 'En esta semana se revisarán los conceptos básicos del tema de la unidad 13.', NULL, '2026-07-02 02:15:31.233358+00:00');
INSERT INTO "contenidos_semana" ("id", "curso_id", "semana_numero", "titulo", "descripcion", "archivo_url", "createdAt") VALUES ('f63efb2a-266b-4157-b3c8-40fbae366884', 'curso-4', 14, 'Semana 14: Introducción y Fundamentos', 'En esta semana se revisarán los conceptos básicos del tema de la unidad 14.', NULL, '2026-07-02 02:15:31.233358+00:00');
INSERT INTO "contenidos_semana" ("id", "curso_id", "semana_numero", "titulo", "descripcion", "archivo_url", "createdAt") VALUES ('a099e9d8-2dd6-4db0-83ff-bbf8e04e590f', 'curso-4', 15, 'Semana 15: Introducción y Fundamentos', 'En esta semana se revisarán los conceptos básicos del tema de la unidad 15.', NULL, '2026-07-02 02:15:31.233358+00:00');
INSERT INTO "contenidos_semana" ("id", "curso_id", "semana_numero", "titulo", "descripcion", "archivo_url", "createdAt") VALUES ('9ddbb0a2-61fe-412a-be6d-5cb9e6b4e27a', 'curso-4', 16, 'Semana 16: Introducción y Fundamentos', 'En esta semana se revisarán los conceptos básicos del tema de la unidad 16.', NULL, '2026-07-02 02:15:31.233358+00:00');
INSERT INTO "contenidos_semana" ("id", "curso_id", "semana_numero", "titulo", "descripcion", "archivo_url", "createdAt") VALUES ('52e2befe-8ccb-4b0c-8154-607715f4dce5', 'curso-4', 17, 'Semana 17: Introducción y Fundamentos', 'En esta semana se revisarán los conceptos básicos del tema de la unidad 17.', NULL, '2026-07-02 02:15:31.233358+00:00');
INSERT INTO "contenidos_semana" ("id", "curso_id", "semana_numero", "titulo", "descripcion", "archivo_url", "createdAt") VALUES ('66c593fd-6256-40bb-b076-e0ad9acb67a4', 'curso-4', 18, 'Semana 18: Introducción y Fundamentos', 'En esta semana se revisarán los conceptos básicos del tema de la unidad 18.', NULL, '2026-07-02 02:15:31.233358+00:00');
INSERT INTO "contenidos_semana" ("id", "curso_id", "semana_numero", "titulo", "descripcion", "archivo_url", "createdAt") VALUES ('ecd0bd19-7062-4b6f-b93a-e9c5230800ab', 'curso-5', 1, 'Semana 1: Introducción y Fundamentos', 'En esta semana se revisarán los conceptos básicos del tema de la unidad 1.', NULL, '2026-07-02 02:15:31.233358+00:00');
INSERT INTO "contenidos_semana" ("id", "curso_id", "semana_numero", "titulo", "descripcion", "archivo_url", "createdAt") VALUES ('99fb47d7-dcea-48cf-b4a0-3b9c7903b697', 'curso-5', 2, 'Semana 2: Introducción y Fundamentos', 'En esta semana se revisarán los conceptos básicos del tema de la unidad 2.', NULL, '2026-07-02 02:15:31.233358+00:00');
INSERT INTO "contenidos_semana" ("id", "curso_id", "semana_numero", "titulo", "descripcion", "archivo_url", "createdAt") VALUES ('c894b62b-ccb1-43ce-9d16-a9fabc7973d9', 'curso-5', 3, 'Semana 3: Introducción y Fundamentos', 'En esta semana se revisarán los conceptos básicos del tema de la unidad 3.', NULL, '2026-07-02 02:15:31.233358+00:00');
INSERT INTO "contenidos_semana" ("id", "curso_id", "semana_numero", "titulo", "descripcion", "archivo_url", "createdAt") VALUES ('e09221b4-cf47-4a5c-bde6-ed178d3602be', 'curso-5', 4, 'Semana 4: Introducción y Fundamentos', 'En esta semana se revisarán los conceptos básicos del tema de la unidad 4.', NULL, '2026-07-02 02:15:31.233358+00:00');
INSERT INTO "contenidos_semana" ("id", "curso_id", "semana_numero", "titulo", "descripcion", "archivo_url", "createdAt") VALUES ('c26a2ef9-5544-4a3e-be79-1c0dcdf90216', 'curso-5', 5, 'Semana 5: Introducción y Fundamentos', 'En esta semana se revisarán los conceptos básicos del tema de la unidad 5.', NULL, '2026-07-02 02:15:31.233358+00:00');
INSERT INTO "contenidos_semana" ("id", "curso_id", "semana_numero", "titulo", "descripcion", "archivo_url", "createdAt") VALUES ('51685e3a-0fd3-4444-8959-345a70866e9d', 'curso-5', 6, 'Semana 6: Introducción y Fundamentos', 'En esta semana se revisarán los conceptos básicos del tema de la unidad 6.', NULL, '2026-07-02 02:15:31.233358+00:00');
INSERT INTO "contenidos_semana" ("id", "curso_id", "semana_numero", "titulo", "descripcion", "archivo_url", "createdAt") VALUES ('277afb98-9bd0-4ee8-a812-91af744e09ea', 'curso-5', 7, 'Semana 7: Introducción y Fundamentos', 'En esta semana se revisarán los conceptos básicos del tema de la unidad 7.', NULL, '2026-07-02 02:15:31.233358+00:00');
INSERT INTO "contenidos_semana" ("id", "curso_id", "semana_numero", "titulo", "descripcion", "archivo_url", "createdAt") VALUES ('4fcadbae-4d9f-48d8-a6fb-6fb7950481a6', 'curso-5', 8, 'Semana 8: Introducción y Fundamentos', 'En esta semana se revisarán los conceptos básicos del tema de la unidad 8.', NULL, '2026-07-02 02:15:31.233358+00:00');
INSERT INTO "contenidos_semana" ("id", "curso_id", "semana_numero", "titulo", "descripcion", "archivo_url", "createdAt") VALUES ('90ecdbc6-df9c-4817-94ea-83f5b9833ec6', 'curso-5', 9, 'Semana 9: Introducción y Fundamentos', 'En esta semana se revisarán los conceptos básicos del tema de la unidad 9.', NULL, '2026-07-02 02:15:31.233358+00:00');
INSERT INTO "contenidos_semana" ("id", "curso_id", "semana_numero", "titulo", "descripcion", "archivo_url", "createdAt") VALUES ('1138e844-320b-4cd0-aa9a-ed85a8a630b0', 'curso-5', 10, 'Semana 10: Introducción y Fundamentos', 'En esta semana se revisarán los conceptos básicos del tema de la unidad 10.', NULL, '2026-07-02 02:15:31.233358+00:00');
INSERT INTO "contenidos_semana" ("id", "curso_id", "semana_numero", "titulo", "descripcion", "archivo_url", "createdAt") VALUES ('e640145b-54cf-422e-829f-2b78db4034e9', 'curso-5', 11, 'Semana 11: Introducción y Fundamentos', 'En esta semana se revisarán los conceptos básicos del tema de la unidad 11.', NULL, '2026-07-02 02:15:31.233358+00:00');
INSERT INTO "contenidos_semana" ("id", "curso_id", "semana_numero", "titulo", "descripcion", "archivo_url", "createdAt") VALUES ('8a8015b3-415b-4ac0-a0e8-b566613a6ae7', 'curso-5', 12, 'Semana 12: Introducción y Fundamentos', 'En esta semana se revisarán los conceptos básicos del tema de la unidad 12.', NULL, '2026-07-02 02:15:31.233358+00:00');
INSERT INTO "contenidos_semana" ("id", "curso_id", "semana_numero", "titulo", "descripcion", "archivo_url", "createdAt") VALUES ('df0fa90b-1604-42ff-822e-5782b18e2a97', 'curso-5', 13, 'Semana 13: Introducción y Fundamentos', 'En esta semana se revisarán los conceptos básicos del tema de la unidad 13.', NULL, '2026-07-02 02:15:31.233358+00:00');
INSERT INTO "contenidos_semana" ("id", "curso_id", "semana_numero", "titulo", "descripcion", "archivo_url", "createdAt") VALUES ('da055211-1412-4fa1-92e8-1f1a131f615b', 'curso-5', 14, 'Semana 14: Introducción y Fundamentos', 'En esta semana se revisarán los conceptos básicos del tema de la unidad 14.', NULL, '2026-07-02 02:15:31.233358+00:00');
INSERT INTO "contenidos_semana" ("id", "curso_id", "semana_numero", "titulo", "descripcion", "archivo_url", "createdAt") VALUES ('e6e71cb7-6de1-4799-b3b0-e567142f60fc', 'curso-5', 15, 'Semana 15: Introducción y Fundamentos', 'En esta semana se revisarán los conceptos básicos del tema de la unidad 15.', NULL, '2026-07-02 02:15:31.233358+00:00');
INSERT INTO "contenidos_semana" ("id", "curso_id", "semana_numero", "titulo", "descripcion", "archivo_url", "createdAt") VALUES ('b6dbb3df-4602-42d7-9fc3-447cdd1ef751', 'curso-5', 16, 'Semana 16: Introducción y Fundamentos', 'En esta semana se revisarán los conceptos básicos del tema de la unidad 16.', NULL, '2026-07-02 02:15:31.233358+00:00');
INSERT INTO "contenidos_semana" ("id", "curso_id", "semana_numero", "titulo", "descripcion", "archivo_url", "createdAt") VALUES ('e9981dda-9e4c-4a01-abf5-a59146083196', 'curso-5', 17, 'Semana 17: Introducción y Fundamentos', 'En esta semana se revisarán los conceptos básicos del tema de la unidad 17.', NULL, '2026-07-02 02:15:31.233358+00:00');
INSERT INTO "contenidos_semana" ("id", "curso_id", "semana_numero", "titulo", "descripcion", "archivo_url", "createdAt") VALUES ('83d135eb-7a1c-4d38-967b-db4af3c7d7fd', 'curso-5', 18, 'Semana 18: Introducción y Fundamentos', 'En esta semana se revisarán los conceptos básicos del tema de la unidad 18.', NULL, '2026-07-02 02:15:31.233358+00:00');

--
-- Estructura y datos de la tabla: "tareas"
--

CREATE TABLE "tareas" (
"id" CHARACTER VARYING NOT NULL,
"curso_id" CHARACTER VARYING NULL,
"titulo" CHARACTER VARYING NOT NULL,
"descripcion" CHARACTER VARYING NULL,
"fecha_entrega" TIMESTAMP WITH TIME ZONE NULL,
"puntaje_total" INTEGER NULL,
"archivo_referencia" CHARACTER VARYING NULL,
"createdAt" TIMESTAMP WITH TIME ZONE NULL DEFAULT now()
);

-- Insertando datos de la tabla "tareas"
INSERT INTO "tareas" ("id", "curso_id", "titulo", "descripcion", "fecha_entrega", "puntaje_total", "archivo_referencia", "createdAt") VALUES ('tarea-1', 'curso-3', 'Diseño de Base de Datos', 'Diseñar un schema para un sistema de biblioteca', '2026-04-20 23:59:00+00:00', 10, NULL, '2026-07-02 02:15:29.545152+00:00');
INSERT INTO "tareas" ("id", "curso_id", "titulo", "descripcion", "fecha_entrega", "puntaje_total", "archivo_referencia", "createdAt") VALUES ('tarea-2', 'curso-3', 'Consultas SQL Avanzadas', 'Realizar 5 consultas complejas con JOINs', '2026-05-10 23:59:00+00:00', 15, NULL, '2026-07-02 02:15:29.545152+00:00');
INSERT INTO "tareas" ("id", "curso_id", "titulo", "descripcion", "fecha_entrega", "puntaje_total", "archivo_referencia", "createdAt") VALUES ('tarea-3', 'curso-1', 'Programa en Python', 'Crear programa que calcule el factorial', '2026-05-15 23:59:00+00:00', 10, NULL, '2026-07-02 02:15:29.545152+00:00');

--
-- Estructura y datos de la tabla: "entregas"
--

CREATE TABLE "entregas" (
"id" CHARACTER VARYING NOT NULL,
"tarea_id" CHARACTER VARYING NULL,
"estudiante_id" CHARACTER VARYING NULL,
"archivo" CHARACTER VARYING NULL,
"fecha_entrega" TIMESTAMP WITH TIME ZONE NULL DEFAULT now(),
"calificacion" DOUBLE PRECISION NULL,
"comentarios" CHARACTER VARYING NULL
);

-- Insertando datos de la tabla "entregas"
INSERT INTO "entregas" ("id", "tarea_id", "estudiante_id", "archivo", "fecha_entrega", "calificacion", "comentarios") VALUES ('ent-1', 'tarea-1', 'estudiante-1', 'db_design.pdf', '2026-07-02 02:15:30.096541+00:00', 9.0, 'Buen diseño');
INSERT INTO "entregas" ("id", "tarea_id", "estudiante_id", "archivo", "fecha_entrega", "calificacion", "comentarios") VALUES ('ent-2', 'tarea-1', 'estudiante-2', 'db_design_v2.pdf', '2026-07-02 02:15:30.096541+00:00', 10.0, 'Excelente');
INSERT INTO "entregas" ("id", "tarea_id", "estudiante_id", "archivo", "fecha_entrega", "calificacion", "comentarios") VALUES ('ent-3', 'tarea-2', 'estudiante-1', 'sql_queries.sql', '2026-07-02 02:15:30.096541+00:00', 14.0, 'Falta optimización');

--
-- Estructura y datos de la tabla: "asistencias"
--

CREATE TABLE "asistencias" (
"id" CHARACTER VARYING NOT NULL,
"curso_id" CHARACTER VARYING NULL,
"estudiante_id" CHARACTER VARYING NULL,
"fecha" TIMESTAMP WITH TIME ZONE NULL,
"estado" CHARACTER VARYING NULL
);

-- Insertando datos de la tabla "asistencias"
INSERT INTO "asistencias" ("id", "curso_id", "estudiante_id", "fecha", "estado") VALUES ('asi-1', 'curso-3', 'estudiante-1', '2026-04-01 00:00:00+00:00', 'presente');
INSERT INTO "asistencias" ("id", "curso_id", "estudiante_id", "fecha", "estado") VALUES ('asi-2', 'curso-3', 'estudiante-1', '2026-04-03 00:00:00+00:00', 'presente');
INSERT INTO "asistencias" ("id", "curso_id", "estudiante_id", "fecha", "estado") VALUES ('asi-3', 'curso-3', 'estudiante-1', '2026-04-05 00:00:00+00:00', 'tardanza');
INSERT INTO "asistencias" ("id", "curso_id", "estudiante_id", "fecha", "estado") VALUES ('asi-4', 'curso-3', 'estudiante-1', '2026-04-08 00:00:00+00:00', 'ausente');
INSERT INTO "asistencias" ("id", "curso_id", "estudiante_id", "fecha", "estado") VALUES ('asi-5', 'curso-3', 'estudiante-1', '2026-04-10 00:00:00+00:00', 'presente');
INSERT INTO "asistencias" ("id", "curso_id", "estudiante_id", "fecha", "estado") VALUES ('asi-6', 'curso-3', 'estudiante-2', '2026-04-01 00:00:00+00:00', 'presente');
INSERT INTO "asistencias" ("id", "curso_id", "estudiante_id", "fecha", "estado") VALUES ('asi-7', 'curso-3', 'estudiante-2', '2026-04-03 00:00:00+00:00', 'presente');
INSERT INTO "asistencias" ("id", "curso_id", "estudiante_id", "fecha", "estado") VALUES ('asi-8', 'curso-3', 'estudiante-2', '2026-04-05 00:00:00+00:00', 'presente');
INSERT INTO "asistencias" ("id", "curso_id", "estudiante_id", "fecha", "estado") VALUES ('asi-9', 'curso-3', 'estudiante-2', '2026-04-08 00:00:00+00:00', 'presente');
INSERT INTO "asistencias" ("id", "curso_id", "estudiante_id", "fecha", "estado") VALUES ('asi-10', 'curso-3', 'estudiante-2', '2026-04-10 00:00:00+00:00', 'presente');

--
-- Estructura y datos de la tabla: "codigos_recuperacion_contrasena"
--

CREATE TABLE "codigos_recuperacion_contrasena" (
"id" CHARACTER VARYING NOT NULL,
"usuario_id" CHARACTER VARYING NOT NULL,
"codigo_hash" CHARACTER VARYING NOT NULL,
"estado" CHARACTER VARYING NOT NULL,
"fecha_expiracion" TIMESTAMP WITH TIME ZONE NOT NULL,
"fecha_uso" TIMESTAMP WITH TIME ZONE NULL,
"fecha_creacion" TIMESTAMP WITH TIME ZONE NULL DEFAULT now()
);

-- (Sin registros para la tabla "codigos_recuperacion_contrasena")

