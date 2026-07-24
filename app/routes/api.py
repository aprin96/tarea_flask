"""
Endpoints tipo API que retornan JSON.
GET /api/users               -> lista todos los usuarios
GET /api/users/<id>          -> retorna un usuario
GET /api/users/search?given_name=Juan -> busca por nombre
"""

from flask import Blueprint, jsonify, request

from app.services import user_service

api_bp = Blueprint("api", __name__, url_prefix="/api/users")


@api_bp.route("/")
def api_list_users():
    users = user_service.list_users()
    return jsonify([user.to_dict() for user in users])


@api_bp.route("/search")
def api_search_users():
    given_name = request.args.get("given_name", "")
    users = user_service.search_users(given_name)
    return jsonify([user.to_dict() for user in users])


@api_bp.route("/<int:user_id>")
def api_get_user(user_id):
    user = user_service.get_user(user_id)
    if user is None:
        return jsonify({"error": "Usuario no encontrado"}), 404
    return jsonify(user.to_dict())
