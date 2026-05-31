# Pruebas de Usuarios (`/api/usuarios`)

---

### GET `/api/usuarios/`
*Requiere Cabecera: `Authorization: Bearer <token_docente_o_admin>`*

**Respuesta Exitosa (200 OK):**
```json
[
  {
    "id": "fb1b2fe9-7beb-4937-89e5-150df8f5096a",
    "email": "miguel@nuevaschool.edu",
    "nombre": "Miguel",
    "apellido": "Gomez",
    "rol": "ADMIN",
    "codigo": null,
    "carrera": null,
    "ciclo": null,
    "especialidad": null,
    "departamento": null,
    "nivel_acceso": "SUPERADMIN",
    "profilePicture": null,
    "createdAt": "2026-05-30T10:00:00Z"
  },
  {
    "id": "fec47d3e-6ec2-4e09-af17-41193dd93fa0",
    "email": "aldo@nuevaschool.edu",
    "nombre": "Aldo",
    "apellido": "Morales Carlos",
    "rol": "DOCENTE",
    "codigo": null,
    "carrera": null,
    "ciclo": null,
    "especialidad": "Desarrollo Full Stack",
    "departamento": "Ciencia de la Computación",
    "nivel_acceso": null,
    "profilePicture": null,
    "createdAt": "2026-05-30T11:00:00Z"
  },
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
]
```

---

### PUT `/api/usuarios/fec47d3e-6ec2-4e09-af17-41193dd93fa0`
*Requiere Cabecera: `Authorization: Bearer <token_admin>`*

**Cuerpo de la Petición (Request JSON):**
```json
{
  "email": "aldo_nuevo@nuevaschool.edu",
  "nombre": "Aldo",
  "apellido": "Morales Carlos Modificado",
  "rol": "DOCENTE",
  "codigo": null,
  "carrera": null,
  "ciclo": null,
  "especialidad": "Arquitectura Cloud e IA",
  "departamento": "Ciencias de la Computación y Sistemas",
  "nivel_acceso": null
}
```

**Respuesta Exitosa (200 OK):**
```json
{
  "id": "fec47d3e-6ec2-4e09-af17-41193dd93fa0",
  "email": "aldo_nuevo@nuevaschool.edu",
  "nombre": "Aldo",
  "apellido": "Morales Carlos Modificado",
  "rol": "DOCENTE",
  "codigo": null,
  "carrera": null,
  "ciclo": null,
  "especialidad": "Arquitectura Cloud e IA",
  "departamento": "Ciencias de la Computación y Sistemas",
  "nivel_acceso": null,
  "profilePicture": null,
  "createdAt": "2026-05-30T11:00:00Z"
}
```

---

### DELETE `/api/usuarios/fec47d3e-6ec2-4e09-af17-41193dd93fa0`
*Requiere Cabecera: `Authorization: Bearer <token_admin>`*

**Respuesta Exitosa (204 No Content):**
*(Cuerpo de respuesta vacío)*
