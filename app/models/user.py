"""
Modelo de datos User.
Representa la tabla 'users' en la base de datos.
"""

from datetime import datetime, timezone

from app.database import db


class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    dni = db.Column(db.String(20), unique=True, nullable=False)
    given_name = db.Column(db.String(100), nullable=False)
    family_name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    phone_number = db.Column(db.String(20), nullable=True)
    address = db.Column(db.String(200), nullable=True)
    created_at = db.Column(db.DateTime, default=lambda: datetime.now(timezone.utc))
    updated_at = db.Column(
        db.DateTime,
        default=lambda: datetime.now(timezone.utc),
        onupdate=lambda: datetime.now(timezone.utc),
    )

    def to_dict(self):
        """Convierte el modelo a un diccionario serializable a JSON."""
        return {
            "id": self.id,
            "dni": self.dni,
            "given_name": self.given_name,
            "family_name": self.family_name,
            "email": self.email,
            "phone_number": self.phone_number,
            "address": self.address,
            "created_at": self.created_at.isoformat() if self.created_at else None,
            "updated_at": self.updated_at.isoformat() if self.updated_at else None,
        }
