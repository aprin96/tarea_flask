"""
Capa de acceso a datos (Repository) para User.
Aisla las consultas a la base de datos del resto de la aplicacion.
"""

from app.database import db
from app.models.user import User


def get_all_users() -> list[User]:
    return User.query.order_by(User.id).all()


def get_user_by_id(user_id: int) -> User | None:
    return User.query.get(user_id)


def search_users_by_given_name(given_name: str) -> list[User]:
    return User.query.filter(User.given_name.ilike(f"%{given_name}%")).all()


def create_user(data: dict) -> User:
    user = User(
        dni=data["dni"],
        given_name=data["given_name"],
        family_name=data["family_name"],
        email=data["email"],
        phone_number=data.get("phone_number"),
        address=data.get("address"),
    )
    db.session.add(user)
    db.session.commit()
    return user


def update_user(user: User, data: dict) -> User:
    user.dni = data.get("dni", user.dni)
    user.given_name = data.get("given_name", user.given_name)
    user.family_name = data.get("family_name", user.family_name)
    user.email = data.get("email", user.email)
    user.phone_number = data.get("phone_number", user.phone_number)
    user.address = data.get("address", user.address)
    db.session.commit()
    return user


def delete_user(user: User) -> None:
    db.session.delete(user)
    db.session.commit()
