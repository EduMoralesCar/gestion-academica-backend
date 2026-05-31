# Pruebas de Cursos (`/api/cursos`)

---

### GET `/api/cursos/`
*Requiere Cabecera: `Authorization: Bearer <access_token>`*

**Respuesta Exitosa (200 OK):**
```json
[
  {
    "id": "23f47aa9-1f95-444f-b6a0-7ade33149d65",
    "nombre": "Lenguajes de Programación",
    "codigo": "PROG-101",
    "creditos": 4,
    "ciclo": 1,
    "modalidad": "virtual",
    "zoom_link": "https://zoom.us/j/1234567890",
    "createdAt": "2026-05-31T12:00:00Z"
  },
  {
    "id": "16319232-488c-499a-9c45-6731bc3511af",
    "nombre": "Herramientas de Desarrollo",
    "codigo": "HD-203",
    "creditos": 4,
    "ciclo": 1,
    "modalidad": "virtual",
    "zoom_link": null,
    "createdAt": "2026-05-31T12:05:00Z"
  }
]
```

---

### POST `/api/cursos/`
*Requiere Cabecera: `Authorization: Bearer <token_admin>`*

**Cuerpo de la Petición (Request JSON):**
```json
{
  "nombre": "Arquitectura de Software",
  "codigo": "ARQ-301",
  "creditos": 4,
  "ciclo": 5,
  "modalidad": "virtual",
  "zoom_link": "https://zoom.us/j/9876543210"
}
```

**Respuesta Exitosa (200 OK):**
```json
{
  "id": "d09f6c8d-39c8-47e2-8951-e374d9e761df",
  "nombre": "Arquitectura de Software",
  "codigo": "ARQ-301",
  "creditos": 4,
  "ciclo": 5,
  "modalidad": "virtual",
  "zoom_link": "https://zoom.us/j/9876543210",
  "createdAt": "2026-05-31T15:24:00Z"
}
```

---

### PUT `/api/cursos/23f47aa9-1f95-444f-b6a0-7ade33149d65`
*Requiere Cabecera: `Authorization: Bearer <token_admin>`*

**Cuerpo de la Petición (Request JSON):**
```json
{
  "nombre": "Lenguajes de Programación Avanzados",
  "codigo": "PROG-101",
  "creditos": 5,
  "ciclo": 1,
  "modalidad": "virtual",
  "zoom_link": "https://zoom.us/j/1111222233"
}
```

**Respuesta Exitosa (200 OK):**
```json
{
  "id": "23f47aa9-1f95-444f-b6a0-7ade33149d65",
  "nombre": "Lenguajes de Programación Avanzados",
  "codigo": "PROG-101",
  "creditos": 5,
  "ciclo": 1,
  "modalidad": "virtual",
  "zoom_link": "https://zoom.us/j/1111222233",
  "createdAt": "2026-05-31T12:00:00Z"
}
```

---

### DELETE `/api/cursos/23f47aa9-1f95-444f-b6a0-7ade33149d65`
*Requiere Cabecera: `Authorization: Bearer <token_admin>`*

**Respuesta Exitosa (204 No Content):**
*(Cuerpo de respuesta vacío)*
