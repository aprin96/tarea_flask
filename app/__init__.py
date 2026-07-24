"""
Application factory.
Aqui se crea y configura la instancia de Flask, se inicializan
las extensiones y se registran los blueprints (rutas).
"""

from flask import Flask

from app.config import Config
from app.database import db


def create_app(config_class: type = Config) -> Flask:
    app = Flask(__name__)
    app.config.from_object(config_class)

    db.init_app(app)

    from app.routes.api import api_bp
    from app.routes.main import main_bp
    from app.routes.users import users_bp

    app.register_blueprint(main_bp)
    app.register_blueprint(users_bp)
    app.register_blueprint(api_bp)

    with app.app_context():
        # Importar los modelos aqui asegura que SQLAlchemy los conozca
        # antes de crear las tablas.
        from app.models.user import User  # noqa: F401

        db.create_all()

    return app
