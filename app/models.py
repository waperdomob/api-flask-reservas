from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import inspect
from datetime import datetime
from sqlalchemy.orm import validates, Mapped, mapped_column

from .database import db

class Usuarios(db.Model):
    __tablename__ = 'Usuarios'

    id: Mapped[int] = mapped_column(db.Integer, primary_key=True, nullable=False, unique=True)
    email: Mapped[str] = mapped_column(db.String(100), nullable=False, unique=True)
    username: Mapped[str] = mapped_column(db.String(255), unique=True, nullable=False)
    password: Mapped[str] = mapped_column(db.String(255), nullable=False)
    created: Mapped[datetime] = mapped_column(db.DateTime(timezone=True), default=datetime.now)                           
    updated:Mapped[datetime] = mapped_column(db.DateTime(timezone=True), default=datetime.now, onupdate=datetime.now)   

    @validates('username')
    def empty_string_to_null(self, key, value):
        if isinstance(value, str) and value == '': return None
        else: return value

    def toDict(self):
        return { c.key: getattr(self, c.key) for c in inspect(self).mapper.column_attrs }

    def __repr__(self):
        return "<%r>" % self.email

class Reservas(db.Model):
    __tablename__ = 'Reservas'

    id: Mapped[int] = mapped_column(db.Integer, primary_key=True, nullable=False, unique=True)
    observaciones: Mapped[str] = mapped_column(db.String(255), nullable=False)
    fecha = mapped_column(db.Date, nullable=False)
    hora = mapped_column(db.Time, nullable=False)
    personas: Mapped[int] = mapped_column(db.Integer, nullable=False)

    def __repr__(self):
        return f"<Reserva {self.id}>: {self.nombre} - {self.fecha} {self.hora}"
    
    def to_dict(self):
        """
        Converts this Reserva object into a dictionary representation.

        Returns:
            dict: A dictionary containing the key-value pairs of the Reserva object's attributes.
        """
        return {
            "id": self.id,
            "observaciones" : self.observaciones,
            "fecha": self.fecha.strftime("%Y-%m-%d"),
            "hora": self.hora.isoformat(),
            "personas": self.personas,
        }