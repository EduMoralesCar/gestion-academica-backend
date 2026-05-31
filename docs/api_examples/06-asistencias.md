# Pruebas de Asistencias (`/api/asistencias`)

---

### GET `/api/asistencias/`
*Requiere Cabecera: `Authorization: Bearer <access_token>`*

**Respuesta Exitosa (200 OK):**
```json
[
  {
    "id": "e93f6c8d-29c8-47e2-8951-e374d9e761df",
    "curso_id": "16319232-488c-499a-9c45-6731bc3511af",
    "estudiante_id": "8d9f082f-d652-4b22-a9bf-0ef5c5593209",
    "fecha": "2026-05-31T10:00:00Z",
    "estado": "presente"
  }
]
```

---

### POST `/api/asistencias/`
*Requiere Cabecera: `Authorization: Bearer <token_docente_o_admin>`*

**Cuerpo de la Petición (Request JSON):**
```json
{
  "curso_id": "16319232-488c-499a-9c45-6731bc3511af",
  "estudiante_id": "8d9f082f-d652-4b22-a9bf-0ef5c5593209",
  "fecha": "2026-05-31T10:00:00Z",
  "estado": "presente"
}
```

**Respuesta Exitosa (200 OK / 201 Created):**
```json
{
  "id": "e93f6c8d-29c8-47e2-8951-e374d9e761df",
  "curso_id": "16319232-488c-499a-9c45-6731bc3511af",
  "estudiante_id": "8d9f082f-d652-4b22-a9bf-0ef5c5593209",
  "fecha": "2026-05-31T10:00:00Z",
  "estado": "presente"
}
```
