"""Rutas generales del sitio (pagina principal, buscador con HTMX)."""

from flask import Blueprint, render_template

main_bp = Blueprint("main", __name__)


@main_bp.route("/")
def index():
    return render_template("index.html")


@main_bp.route("/buscador")
def buscador():
    """Pagina que consume la API JSON usando HTMX, sin recargar la pagina."""
    return render_template("buscador.html")
