# API Specification

## POST /generate_ad_copy
Generate advertisement copy from product information.

Request JSON:
```json
{
  "name": "Widget",
  "description": "A useful widget"
}
```

Response JSON:
```json
{
  "ad_copy": "string"
}
```

## POST /register
Create a new user account.

Request JSON:
```json
{
  "username": "alice",
  "password": "secret"
}
```

Responses:
- `201 Created` on success
- `400 Bad Request` if the user exists

## POST /login
Authenticate a user.

Request JSON:
```json
{
  "username": "alice",
  "password": "secret"
}
```

Responses:
- `200 OK` with `{ "status": "ok" }`
- `401 Unauthorized` if credentials are invalid
