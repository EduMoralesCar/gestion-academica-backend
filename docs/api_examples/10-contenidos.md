# Pruebas de Contenidos Semana (`/api/contenidos`)

---

### GET `/api/contenidos/`
*Requiere Cabecera: `Authorization: Bearer <access_token>`*

**Respuesta Exitosa (200 OK):**
```json
[
  {
    "id": "593f6c8d-29c8-47e2-8951-e374d9e761df",
    "curso_id": "16319232-488c-499a-9c45-6731bc3511af",
    "semana_numero": 2,
    "titulo": "Conceptos Fundamentales de Git",
    "descripcion": "En esta clase aprenderemos sobre repositorios locales, áreas de trabajo y comandos básicos.",
    "archivo_url": "https://storage.nuevaschool.pe/contenidos/semana2_introduccion_git.pdf",
    "createdAt": "2026-05-31T15:20:00Z"
  }
]
```

---

### POST `/api/contenidos/`
*Requiere Cabecera: `Authorization: Bearer <token_docente_o_admin>`*

**Cuerpo de la Petición (Request JSON):**
```json
{
  "curso_id": "16319232-488c-499a-9c45-6731bc3511af",
  "semana_numero": 2,
  "titulo": "Conceptos Fundamentales de Git",
  "descripcion": "En esta clase aprenderemos sobre repositorios locales, áreas de trabajo y comandos básicos.",
  "archivo_url": "https://storage.nuevaschool.pe/contenidos/semana2_introduccion_git.pdf"
}
```

**Respuesta Exitosa (200 OK / 201 Created):**
```json
{
  "id": "593f6c8d-29c8-47e2-8951-e374d9e761df",
  "curso_id": "16319232-488c-499a-9c45-6731bc3511af",
  "semana_numero": 2,
  "titulo": "Conceptos Fundamentales de Git",
  "descripcion": "En esta clase aprenderemos sobre repositorios locales, áreas de trabajo y comandos básicos.",
  "archivo_url": "https://storage.nuevaschool.pe/contenidos/semana2_introduccion_git.pdf",
  "createdAt": "2026-05-31T15:20:00Z"
}
```

---

### PUT `/api/contenidos/593f6c8d-29c8-47e2-8951-e374d9e761df`
*Requiere Cabecera: `Authorization: Bearer <token_docente_o_admin>`*

**Cuerpo de la Petición (Request JSON):**
```json
{
  "semana_numero": 2,
  "titulo": "Conceptos Fundamentales de Git y GitHub",
  "descripcion": "En esta clase aprenderemos sobre repositorios locales, áreas de trabajo, comandos básicos y repositorios remotos en GitHub.",
  "archivo_url": "https://storage.nuevaschool.pe/contenidos/semana2_introduccion_git_v2.pdf"
}
```

**Respuesta Exitosa (200 OK):**
```json
{
  "id": "593f6c8d-29c8-47e2-8951-e374d9e761df",
  "curso_id": "16319232-488c-499a-9c45-6731bc3511af",
  "semana_numero": 2,
  "titulo": "Conceptos Fundamentales de Git y GitHub",
  "descripcion": "En esta clase aprenderemos sobre repositorios locales, áreas de trabajo, comandos básicos y repositorios remotos en GitHub.",
  "archivo_url": "https://storage.nuevaschool.pe/contenidos/semana2_introduccion_git_v2.pdf",
  "createdAt": "2026-05-31T15:20:00Z"
}
```

---

### DELETE `/api/contenidos/593f6c8d-29c8-47e2-8951-e374d9e761df`
*Requiere Cabecera: `Authorization: Bearer <token_docente_o_admin>`*

**Respuesta Exitosa (204 No Content):**
*(Cuerpo de respuesta vacío)*
