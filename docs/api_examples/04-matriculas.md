# Pruebas de Matrículas (`/api/matriculas`)

---

### GET `/api/matriculas/`
*Requiere Cabecera: `Authorization: Bearer <access_token>`*

**Respuesta Exitosa (200 OK):**
```json
[
  {
    "id": "e006c2ef-bc11-46ea-96b1-97b2c5f1888b",
    "estudiante_id": "8d9f082f-d652-4b22-a9bf-0ef5c5593209",
    "curso_id": "16319232-488c-499a-9c45-6731bc3511af",
    "fecha_matricula": "2026-05-31T12:05:00Z",
    "estado": "activo"
  },
  {
    "id": "f4fb24b6-395c-4cbf-92c1-810549301305",
    "estudiante_id": "8d9f082f-d652-4b22-a9bf-0ef5c5593209",
    "curso_id": "23f47aa9-1f95-444f-b6a0-7ade33149d65",
    "fecha_matricula": "2026-05-31T12:10:00Z",
    "estado": "activo"
  }
]
```

---

### POST `/api/matriculas/`
*Requiere Cabecera: `Authorization: Bearer <token_admin>`*

**Cuerpo de la Petición (Request JSON):**
```json
{
  "estudiante_id": "8d9f082f-d652-4b22-a9bf-0ef5c5593209",
  "curso_id": "16319232-488c-499a-9c45-6731bc3511af"
}
```

**Respuesta Exitosa (200 OK):**
```json
{
  "id": "e006c2ef-bc11-46ea-96b1-97b2c5f1888b",
  "estudiante_id": "8d9f082f-d652-4b22-a9bf-0ef5c5593209",
  "curso_id": "16319232-488c-499a-9c45-6731bc3511af",
  "fecha_matricula": "2026-05-31T12:05:00Z",
  "estado": "activo"
}
```

---

### GET `/api/matriculas/curso/16319232-488c-499a-9c45-6731bc3511af/estudiantes`
*Requiere Cabecera: `Authorization: Bearer <access_token>`*

**Respuesta Exitosa (200 OK):**
```json
{
  "curso": {
    "id": "16319232-488c-499a-9c45-6731bc3511af",
    "nombre": "Herramientas de Desarrollo",
    "codigo": "HD-203",
    "creditos": 4,
    "ciclo": 1,
    "modalidad": "virtual",
    "zoom_link": null,
    "createdAt": "2026-05-31T12:05:00Z"
  },
  "estudiantes": [
    {
      "id": "8d9f082f-d652-4b22-a9bf-0ef5c5593209",
      "email": "edu@nuevaschool.edu",
      "nombre": "Edu",
      "apellido": "Morales Carlos",
      "rol": "ESTUDIANTE",
      "codigo": "EST-0104",
      "carrera": "Ciencia de la Computación",
      "ciclo": 2,
      "especialidad": null,
      "departamento": null,
      "nivel_acceso": null,
      "createdAt": "2026-05-30T12:00:00Z",
      "profilePicture": null,
      "matricula_id": "e006c2ef-bc11-46ea-96b1-97b2c5f1888b",
      "fecha_matricula": "2026-05-31T12:05:00Z",
      "estado_matricula": "activo"
    }
  ],
  "total": 1
}
```

---

### PUT `/api/matriculas/e006c2ef-bc11-46ea-96b1-97b2c5f1888b`
*Requiere Cabecera: `Authorization: Bearer <token_admin>`*

**Cuerpo de la Petición (Request JSON):**
```json
{
  "estudiante_id": "8d9f082f-d652-4b22-a9bf-0ef5c5593209",
  "curso_id": "23f47aa9-1f95-444f-b6a0-7ade33149d65"
}
```

**Respuesta Exitosa (200 OK):**
```json
{
  "id": "e006c2ef-bc11-46ea-96b1-97b2c5f1888b",
  "estudiante_id": "8d9f082f-d652-4b22-a9bf-0ef5c5593209",
  "curso_id": "23f47aa9-1f95-444f-b6a0-7ade33149d65",
  "fecha_matricula": "2026-05-31T12:05:00Z",
  "estado": "activo"
}
```

---

### DELETE `/api/matriculas/curso/16319232-488c-499a-9c45-6731bc3511af/estudiantes/8d9f082f-d652-4b22-a9bf-0ef5c5593209`
*Requiere Cabecera: `Authorization: Bearer <token_admin>`*

**Respuesta Exitosa (200 OK):**
```json
{
  "id": "e006c2ef-bc11-46ea-96b1-97b2c5f1888b",
  "estudiante_id": "8d9f082f-d652-4b22-a9bf-0ef5c5593209",
  "curso_id": "16319232-488c-499a-9c45-6731bc3511af",
  "fecha_matricula": "2026-05-31T12:05:00Z",
  "estado": "retirado"
}
```
