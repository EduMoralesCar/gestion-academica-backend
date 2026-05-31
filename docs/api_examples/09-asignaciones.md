# Pruebas de Asignaciones Docente (`/api/asignaciones`)

---

### GET `/api/asignaciones/`
*Requiere Cabecera: `Authorization: Bearer <access_token>`*

**Respuesta Exitosa (200 OK):**
```json
[
  {
    "id": "783f9c8d-39c8-47e2-8951-e374d9e761df",
    "docente_id": "fec47d3e-6ec2-4e09-af17-41193dd93fa0",
    "curso_id": "16319232-488c-499a-9c45-6731bc3511af",
    "fecha_asignacion": "2026-05-31T15:15:00Z"
  }
]
```

---

### POST `/api/asignaciones/`
*Requiere Cabecera: `Authorization: Bearer <token_admin>`*

**Cuerpo de la Petición (Request JSON):**
```json
{
  "docente_id": "fec47d3e-6ec2-4e09-af17-41193dd93fa0",
  "curso_id": "16319232-488c-499a-9c45-6731bc3511af"
}
```

**Respuesta Exitosa (200 OK / 201 Created):**
```json
{
  "id": "783f9c8d-39c8-47e2-8951-e374d9e761df",
  "docente_id": "fec47d3e-6ec2-4e09-af17-41193dd93fa0",
  "curso_id": "16319232-488c-499a-9c45-6731bc3511af",
  "fecha_asignacion": "2026-05-31T15:15:00Z"
}
```

---

### PUT `/api/asignaciones/783f9c8d-39c8-47e2-8951-e374d9e761df`
*Requiere Cabecera: `Authorization: Bearer <token_admin>`*

**Cuerpo de la Petición (Request JSON):**
```json
{
  "docente_id": "54eadef2-7f40-4edb-bebe-e8a6ff406af1",
  "curso_id": "16319232-488c-499a-9c45-6731bc3511af"
}
```

**Respuesta Exitosa (200 OK):**
```json
{
  "id": "783f9c8d-39c8-47e2-8951-e374d9e761df",
  "docente_id": "54eadef2-7f40-4edb-bebe-e8a6ff406af1",
  "curso_id": "16319232-488c-499a-9c45-6731bc3511af",
  "fecha_asignacion": "2026-05-31T15:15:00Z"
}
```
