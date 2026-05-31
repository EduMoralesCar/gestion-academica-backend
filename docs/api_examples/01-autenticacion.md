# Pruebas de Autenticación (`/api/auth`)

---

### POST `/api/auth/registro`
**Cuerpo de la Petición (Request JSON):**
```json
{
  "email": "estudiante_nuevo@nuevaschool.pe",
  "password": "clave_segura_123",
  "nombre": "Carlos",
  "apellido": "Gonzales Ruiz",
  "rol": "ESTUDIANTE",
  "codigo": "EST-202601",
  "carrera": "Ingeniería de Software",
  "ciclo": 3,
  "especialidad": null,
  "departamento": null,
  "nivel_acceso": null
}
```

**Respuesta Exitosa (200 OK / 201 Created):**
```json
{
  "id": "ae62b10c-fe43-4912-8d61-5ddc258cef20",
  "email": "estudiante_nuevo@nuevaschool.pe",
  "nombre": "Carlos",
  "apellido": "Gonzales Ruiz",
  "rol": "ESTUDIANTE",
  "codigo": "EST-202601",
  "carrera": "Ingeniería de Software",
  "ciclo": 3,
  "especialidad": null,
  "departamento": null,
  "nivel_acceso": null,
  "profilePicture": null,
  "createdAt": "2026-05-31T15:00:00Z"
}
```

---

### POST `/api/auth/login`
*Nota: Se envía como `x-www-form-urlencoded` o `multipart/form-data`.*

**Cuerpo de la Petición (Request Form-Data):**
```ini
username = estudiante@nuevaschool.pe
password = clave_segura_123
```

**Respuesta Exitosa (200 OK):**
```json
{
  "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
  "token_type": "bearer",
  "user": {
    "id": "ae62b10c-fe43-4912-8d61-5ddc258cef20",
    "email": "estudiante@nuevaschool.pe",
    "nombre": "Carlos",
    "apellido": "Gonzales Ruiz",
    "rol": "ESTUDIANTE",
    "codigo": "EST-202601",
    "carrera": "Ingeniería de Software",
    "ciclo": 3,
    "especialidad": null,
    "departamento": null,
    "nivel_acceso": null,
    "profilePicture": null,
    "createdAt": "2026-05-31T15:00:00Z"
  }
}
```

---

### GET `/api/auth/me`
*Requiere Cabecera: `Authorization: Bearer <access_token>`*

**Respuesta Exitosa (200 OK):**
```json
{
  "id": "ae62b10c-fe43-4912-8d61-5ddc258cef20",
  "email": "estudiante@nuevaschool.pe",
  "nombre": "Carlos",
  "apellido": "Gonzales Ruiz",
  "rol": "ESTUDIANTE",
  "codigo": "EST-202601",
  "carrera": "Ingeniería de Software",
  "ciclo": 3,
  "especialidad": null,
  "departamento": null,
  "nivel_acceso": null,
  "profilePicture": null,
  "createdAt": "2026-05-31T15:00:00Z"
}
```

---

### PUT `/api/auth/change-password`
*Requiere Cabecera: `Authorization: Bearer <access_token>`*

**Cuerpo de la Petición (Request JSON):**
```json
{
  "contrasenia_actual": "clave_segura_123",
  "nueva_contrasenia": "nueva_clave_secreta_456"
}
```

**Respuesta Exitosa (200 OK):**
```json
{
  "message": "Contrasena actualizada correctamente"
}
```

---

### POST `/api/auth/forgot-password`
**Cuerpo de la Petición (Request JSON):**
```json
{
  "email": "estudiante@nuevaschool.pe"
}
```

**Respuesta Exitosa (200 OK):**
```json
{
  "message": "Si el correo existe, enviaremos un codigo de recuperacion"
}
```

---

### POST `/api/auth/reset-password`
**Cuerpo de la Petición (Request JSON):**
```json
{
  "email": "estudiante@nuevaschool.pe",
  "codigo": "054157",
  "nueva_contrasenia": "nuevaClaveSuperSegura123"
}
```

**Respuesta Exitosa (200 OK):**
```json
{
  "message": "Contrasena actualizada correctamente"
}
```
