"""
Rutas del CRUD de usuarios (HTML / formularios tradicionales).
GET  /users/new       -> formulario de creacion
POST /users           -> crea el usuario
GET  /users           -> lista usuarios
GET  /users/<id>      -> detalle de un usuario
GET  /users/<id>/edit -> formulario de edicion
POST /users/<id>      -> actualiza el usuario
POST /users/<id>/delete -> elimina el usuario
"""

from flask import Blueprint, flash, redirect, render_template, request, url_for

from app.services import user_service
from app.services.user_service import UserValidationError

users_bp = Blueprint("users", __name__, url_prefix="/users")


def _form_to_dict(form) -> dict:
    return {
        "dni": form.get("dni", "").strip(),
        "given_name": form.get("given_name", "").strip(),
        "family_name": form.get("family_name", "").strip(),
        "email": form.get("email", "").strip(),
        "phone_number": form.get("phone_number", "").strip(),
        "address": form.get("address", "").strip(),
    }


@users_bp.route("/")
def list_users():
    users = user_service.list_users()
    return render_template("users/list.html", users=users)


@users_bp.route("/new")
def new_user_form():
    return render_template(
        "users/form.html", user=None, errors=[], is_edit=False, user_id=None
    )


@users_bp.route("/", methods=["POST"])
def create_user():
    data = _form_to_dict(request.form)
    try:
        user_service.register_user(data)
    except UserValidationError as exc:
        return render_template(
            "users/form.html", user=data, errors=exc.errors, is_edit=False, user_id=None
        )

    flash("Usuario creado correctamente.", "success")
    return redirect(url_for("users.list_users"))


@users_bp.route("/<int:user_id>")
def user_detail(user_id):
    user = user_service.get_user(user_id)
    if user is None:
        flash("Usuario no encontrado.", "error")
        return redirect(url_for("users.list_users"))
    return render_template("users/detail.html", user=user)


@users_bp.route("/<int:user_id>/edit")
def edit_user_form(user_id):
    user = user_service.get_user(user_id)
    if user is None:
        flash("Usuario no encontrado.", "error")
        return redirect(url_for("users.list_users"))
    return render_template(
        "users/form.html", user=user, errors=[], is_edit=True, user_id=user_id
    )


@users_bp.route("/<int:user_id>", methods=["POST"])
def update_user(user_id):
    data = _form_to_dict(request.form)
    try:
        user = user_service.edit_user(user_id, data)
    except UserValidationError as exc:
        return render_template(
            "users/form.html", user=data, errors=exc.errors, is_edit=True, user_id=user_id
        )

    if user is None:
        flash("Usuario no encontrado.", "error")
        return redirect(url_for("users.list_users"))

    flash("Usuario actualizado correctamente.", "success")
    return redirect(url_for("users.user_detail", user_id=user_id))


@users_bp.route("/<int:user_id>/delete", methods=["POST"])
def delete_user(user_id):
    deleted = user_service.remove_user(user_id)
    if deleted:
        flash("Usuario eliminado correctamente.", "success")
    else:
        flash("Usuario no encontrado.", "error")
    return redirect(url_for("users.list_users"))
