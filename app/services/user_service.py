"""
Capa de servicios (logica de negocio) para User.
Las rutas (routes) llaman a estas funciones en vez de hablar
directamente con el repositorio o la base de datos.
"""

from app.models.user import User
from app.repositories import user_repository
from app.schemas.user_schema import validate_user_data


class UserValidationError(Exception):
    """Se lanza cuando los datos de un usuario no son validos."""

    def __init__(self, errors: list[str]):
        self.errors = errors
        super().__init__("; ".join(errors))


def list_users() -> list[User]:
    return user_repository.get_all_users()


def get_user(user_id: int) -> User | None:
    return user_repository.get_user_by_id(user_id)


def search_users(given_name: str) -> list[User]:
    return user_repository.search_users_by_given_name(given_name)


def register_user(data: dict) -> User:
    errors = validate_user_data(data)
    if errors:
        raise UserValidationError(errors)
    return user_repository.create_user(data)


def edit_user(user_id: int, data: dict) -> User | None:
    user = user_repository.get_user_by_id(user_id)
    if user is None:
        return None

    errors = validate_user_data(data)
    if errors:
        raise UserValidationError(errors)

    return user_repository.update_user(user, data)


def remove_user(user_id: int) -> bool:
    user = user_repository.get_user_by_id(user_id)
    if user is None:
        return False
    user_repository.delete_user(user)
    return True
