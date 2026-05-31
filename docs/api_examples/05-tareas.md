# Pruebas de Tareas (`/api/tareas`)

---

### GET `/api/tareas/`
*Requiere Cabecera: `Authorization: Bearer <access_token>`*

**Respuesta Exitosa (200 OK):**
```json
[
  {
    "id": "f156c360-8b51-4750-918f-eef2c7a4293d",
    "curso_id": "16319232-488c-499a-9c45-6731bc3511af",
    "titulo": "Github",
    "descripcion": "Subir el enlace del perfil personal de GitHub para validación de acceso.",
    "fecha_entrega": "2026-06-05T23:59:59Z",
    "puntaje_total": 20,
    "archivo_referencia": null,
    "createdAt": "2026-05-31T12:10:00Z"
  },
  {
    "id": "fa69f11f-d88a-4012-b93b-c904e92aed96",
    "curso_id": "16319232-488c-499a-9c45-6731bc3511af",
    "titulo": "Version de Controles (GIT)",
    "descripcion": "Crear un flujo de trabajo de Git con tres ramas.",
    "fecha_entrega": "2026-06-12T23:59:59Z",
    "puntaje_total": 20,
    "archivo_referencia": "https://storage.nuevaschool.pe/tareas/guia_trabajo_git.pdf",
    "createdAt": "2026-05-31T12:15:00Z"
  }
]
```

---

### POST `/api/tareas/`
*Requiere Cabecera: `Authorization: Bearer <token_docente_o_admin>`*

**Cuerpo de la Petición (Request JSON):**
```json
{
  "curso_id": "16319232-488c-499a-9c45-6731bc3511af",
  "titulo": "Práctica Calificada 1: Control de Versiones con Git",
  "descripcion": "Crear un repositorio en GitHub, realizar commits y subir el enlace en PDF.",
  "fecha_entrega": "2026-06-15T23:59:59Z",
  "puntaje_total": 20,
  "archivo_referencia": "https://storage.nuevaschool.pe/tareas/guia_git_pc1.pdf"
}
```

**Respuesta Exitosa (200 OK):**
```json
{
  "id": "f156c360-8b51-4750-918f-eef2c7a4293d",
  "curso_id": "16319232-488c-499a-9c45-6731bc3511af",
  "titulo": "Práctica Calificada 1: Control de Versiones con Git",
  "descripcion": "Crear un repositorio en GitHub, realizar commits y subir el enlace en PDF.",
  "fecha_entrega": "2026-06-15T23:59:59Z",
  "puntaje_total": 20,
  "archivo_referencia": "https://storage.nuevaschool.pe/tareas/guia_git_pc1.pdf",
  "createdAt": "2026-05-31T15:28:00Z"
}
```

---

### PUT `/api/tareas/f156c360-8b51-4750-918f-eef2c7a4293d`
*Requiere Cabecera: `Authorization: Bearer <token_docente_o_admin>`*

**Cuerpo de la Petición (Request JSON):**
```json
{
  "curso_id": "16319232-488c-499a-9c45-6731bc3511af",
  "titulo": "Github (Modificado)",
  "descripcion": "Subir el enlace del perfil personal de GitHub obligatorio.",
  "fecha_entrega": "2026-06-08T23:59:59Z",
  "puntaje_total": 20,
  "archivo_referencia": null
}
```

**Respuesta Exitosa (200 OK):**
```json
{
  "id": "f156c360-8b51-4750-918f-eef2c7a4293d",
  "curso_id": "16319232-488c-499a-9c45-6731bc3511af",
  "titulo": "Github (Modificado)",
  "descripcion": "Subir el enlace del perfil personal de GitHub obligatorio.",
  "fecha_entrega": "2026-06-08T23:59:59Z",
  "puntaje_total": 20,
  "archivo_referencia": null,
  "createdAt": "2026-05-31T12:10:00Z"
}
```

---

### DELETE `/api/tareas/f156c360-8b51-4750-918f-eef2c7a4293d`
*Requiere Cabecera: `Authorization: Bearer <token_docente_o_admin>`*

**Respuesta Exitosa (204 No Content):**
*(Cuerpo de respuesta vacío)*
