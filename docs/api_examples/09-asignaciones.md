# Pruebas de Asignaciones Docente (`/api/asignaciones`)

---

### GET `/api/asignaciones/`
*Requiere Cabecera: `Authorization: Bearer <access_token>`*

**Notas:**
- Los estudiantes no pueden consultar esta ruta.
- Los docentes ven solo sus propias asignaciones.
- Los administradores ven todas las asignaciones.

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

**Errores posibles:**
- `403 Forbidden` si el usuario autenticado no es administrador.
- `404 Not Found` si `docente_id` o `curso_id` no existen.
- `400 Bad Request` si el `docente_id` corresponde a un usuario que no es docente.

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
