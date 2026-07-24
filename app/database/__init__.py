"""
Instancia unica de SQLAlchemy usada por toda la aplicacion.
Se define aqui, separada de app/__init__.py, para evitar
importaciones circulares entre models, repositories y la app factory.
"""

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
