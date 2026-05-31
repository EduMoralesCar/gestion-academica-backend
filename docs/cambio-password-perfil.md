# Cambio de password desde perfil

Este flujo permite que un usuario autenticado cambie su password desde su perfil.

## Endpoint

```http
PUT /api/auth/change-password
```

Requiere token JWT en el boton `Authorize` de Swagger.

## Body

```json
{
  "contrasenia_actual": "claveActual123",
  "nueva_contrasenia": "nuevaClave123"
}
```

## Validaciones

- El usuario debe estar autenticado.
- `contrasenia_actual` debe coincidir con el password actual.
- `nueva_contrasenia` debe ser diferente al password actual.
- La nueva contrasenia se guarda hasheada en `users.hashed_password`.

## Prueba en Swagger

1. Iniciar sesion en `POST /api/auth/login`.
2. Copiar el `access_token`.
3. Pegar el token en `Authorize` con formato `Bearer TOKEN`.
4. Ejecutar `PUT /api/auth/change-password`.
5. Cerrar sesion o probar login usando la nueva contrasenia.
