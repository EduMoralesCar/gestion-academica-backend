# Pruebas de Entregas (`/api/entregas`)

---

### GET `/api/entregas/`
*Requiere Cabecera: `Authorization: Bearer <access_token>`*

**Respuesta Exitosa (200 OK):**
```json
[
  {
    "id": "673f412d-90c8-47e2-8951-e374d9e761df",
    "tarea_id": "f156c360-8b51-4750-918f-eef2c7a4293d",
    "estudiante_id": "ae62b10c-fe43-4912-8d61-5ddc258cef20",
    "archivo": "https://storage.nuevaschool.pe/entregas/carlos_gonzales_pc1.pdf",
    "fecha_entrega": "2026-05-31T15:00:00Z",
    "calificacion": null,
    "comentarios": null
  }
]
```

---

### POST `/api/entregas/`
*Requiere Cabecera: `Authorization: Bearer <token_estudiante>`*

**Cuerpo de la Petición (Request JSON):**
```json
{
  "tarea_id": "f156c360-8b51-4750-918f-eef2c7a4293d",
  "archivo": "https://storage.nuevaschool.pe/entregas/carlos_gonzales_pc1.pdf"
}
```

**Respuesta Exitosa (200 OK / 201 Created):**
*Nota: La API asocia automáticamente la entrega al `id` del estudiante autenticado.*
```json
{
  "id": "673f412d-90c8-47e2-8951-e374d9e761df",
  "tarea_id": "f156c360-8b51-4750-918f-eef2c7a4293d",
  "estudiante_id": "ae62b10c-fe43-4912-8d61-5ddc258cef20",
  "archivo": "https://storage.nuevaschool.pe/entregas/carlos_gonzales_pc1.pdf",
  "fecha_entrega": "2026-05-31T15:00:00Z",
  "calificacion": null,
  "comentarios": null
}
```

---

### PUT `/api/entregas/673f412d-90c8-47e2-8951-e374d9e761df`
*Requiere Cabecera: `Authorization: Bearer <token_estudiante_dueno_de_la_entrega>`*

**Cuerpo de la Petición (Request JSON):**
```json
{
  "tarea_id": "f156c360-8b51-4750-918f-eef2c7a4293d",
  "archivo": "https://storage.nuevaschool.pe/entregas/carlos_gonzales_pc1_nueva_version.pdf"
}
```

**Respuesta Exitosa (200 OK):**
```json
{
  "id": "673f412d-90c8-47e2-8951-e374d9e761df",
  "tarea_id": "f156c360-8b51-4750-918f-eef2c7a4293d",
  "estudiante_id": "ae62b10c-fe43-4912-8d61-5ddc258cef20",
  "archivo": "https://storage.nuevaschool.pe/entregas/carlos_gonzales_pc1_nueva_version.pdf",
  "fecha_entrega": "2026-05-31T15:00:00Z",
  "calificacion": null,
  "comentarios": null
}
```
