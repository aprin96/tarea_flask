"""
Validacion simple de los datos de entrada para User.
No usamos una libreria externa de schemas: son validaciones
manuales para mantener el ejemplo simple y explicito.
"""


def validate_user_data(data: dict) -> list[str]:
    """
    Valida los datos de un usuario.
    Retorna una lista de mensajes de error. Lista vacia = datos validos.
    """
    errors = []

    required_fields = ["dni", "given_name", "family_name", "email"]
    for field in required_fields:
        if not data.get(field, "").strip():
            errors.append(f"El campo '{field}' es obligatorio.")

    email = data.get("email", "")
    if email and "@" not in email:
        errors.append("El email no tiene un formato valido.")

    return errors
