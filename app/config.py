"""
Configuración de la aplicación.
Toda la configuración se obtiene desde variables de entorno (.env),
nunca se escriben valores sensibles directamente en el código.
"""

import os

from dotenv import load_dotenv

load_dotenv()

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def _resolve_database_url() -> str:
    """
    Si DATABASE_URL es una ruta sqlite relativa, la convierte en absoluta
    tomando como base la raiz del proyecto. Esto evita que Flask-SQLAlchemy
    la resuelva relativa a la carpeta 'instance/'.
    """
    url = os.getenv("DATABASE_URL", "")
    prefix = "sqlite:///"
    if url.startswith(prefix) and not url.startswith("sqlite:////"):
        relative_path = url[len(prefix):]
        absolute_path = os.path.join(BASE_DIR, relative_path)
        os.makedirs(os.path.dirname(absolute_path), exist_ok=True)
        return f"sqlite:///{absolute_path}"
    return url


class Config:
    SECRET_KEY = os.getenv("SECRET_KEY")
    FLASK_ENV = os.getenv("FLASK_ENV", "production")
    SQLALCHEMY_DATABASE_URI = _resolve_database_url()
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    DEBUG = FLASK_ENV == "development"
