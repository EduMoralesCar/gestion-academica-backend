# Recuperacion de password

La recuperacion de password usa codigos temporales enviados por correo SMTP.

## Tabla requerida

La base de datos debe tener la tabla `codigos_recuperacion_contrasena`.

Campos principales:

- `usuario_id`: referencia a `users.id`.
- `codigo_hash`: codigo temporal hasheado.
- `estado`: `ACTIVO`, `INVALIDADO`, `USADO`, `EXPIRADO` o `ERROR_ENVIO`.
- `fecha_expiracion`: fecha y hora en que vence el codigo.
- `fecha_uso`: fecha y hora en que fue usado.

## Endpoints

Solicitar codigo:

```http
POST /api/auth/forgot-password
```

Body:

```json
{
  "email": "estudiante@nuevaschool.pe"
}
```

Restablecer password:

```http
POST /api/auth/reset-password
```

Body:

```json
{
  "email": "estudiante@nuevaschool.pe",
  "codigo": "123456",
  "nueva_contrasenia": "nuevaClave123"
}
```

## Variables SMTP

```env
SMTP_HOST=smtp.gmail.com
SMTP_PORT=587
SMTP_USER=tu_correo@gmail.com
SMTP_PASSWORD=tu_app_password_de_google
SMTP_FROM_NAME="Soporte de Nueva School"
SMTP_FROM_EMAIL=tu_correo@gmail.com
RESET_CODE_EXPIRE_MINUTES=10
```

`SMTP_PASSWORD` debe ser una App Password de Google, no la password normal de Gmail.
