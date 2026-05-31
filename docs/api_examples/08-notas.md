# Pruebas de Notas (`/api/notas`)

---

### GET `/api/notas/`
*Requiere Cabecera: `Authorization: Bearer <access_token>`*

**Respuesta Exitosa (200 OK):**
```json
[
  {
    "id": "ba7e9c8d-39c8-47e2-8951-e374d9e761df",
    "matricula_id": "f4fb24b6-395c-4cbf-92c1-810549301305",
    "tipo": "PC1",
    "calificacion": 17.5,
    "peso": 0.15,
    "fecha": "2026-05-31T15:10:00Z"
  }
]
```

---

### POST `/api/notas/`
*Requiere Cabecera: `Authorization: Bearer <token_docente_o_admin>`*

**Cuerpo de la Petición (Request JSON):**
```json
{
  "matricula_id": "f4fb24b6-395c-4cbf-92c1-810549301305",
  "tipo": "PC1",
  "calificacion": 17.5,
  "peso": 0.15
}
```

**Respuesta Exitosa (200 OK / 201 Created):**
```json
{
  "id": "ba7e9c8d-39c8-47e2-8951-e374d9e761df",
  "matricula_id": "f4fb24b6-395c-4cbf-92c1-810549301305",
  "tipo": "PC1",
  "calificacion": 17.5,
  "peso": 0.15,
  "fecha": "2026-05-31T15:10:00Z"
}
```

---

### PUT `/api/notas/ba7e9c8d-39c8-47e2-8951-e374d9e761df`
*Requiere Cabecera: `Authorization: Bearer <token_docente_o_admin>`*

**Cuerpo de la Petición (Request JSON):**
```json
{
  "matricula_id": "f4fb24b6-395c-4cbf-92c1-810549301305",
  "tipo": "PC1",
  "calificacion": 19.0,
  "peso": 0.15
}
```

**Respuesta Exitosa (200 OK):**
```json
{
  "id": "ba7e9c8d-39c8-47e2-8951-e374d9e761df",
  "matricula_id": "f4fb24b6-395c-4cbf-92c1-810549301305",
  "tipo": "PC1",
  "calificacion": 19.0,
  "peso": 0.15,
  "fecha": "2026-05-31T15:10:00Z"
}
```
