import json
from flask import jsonify, abort, make_response
from datetime import datetime

from app.models import db, Reservas


def list_all_reservations():
    reservations = Reservas.query.all()
    response = [reservation.to_dict() for reservation in reservations]
    return jsonify(response)

def create_reservation(data):
    try:
        nueva_reserva = Reservas(
            observaciones=data['observaciones'],
            fecha=datetime.strptime(data['fecha'], '%Y-%m-%d').date(),
            hora=datetime.strptime(data['hora'], '%H:%M:%S').time(),
            personas=data['personas']
        )
        db.session.add(nueva_reserva)
        db.session.commit()
        reserva = Reservas.query.get(nueva_reserva.id).to_dict()
        return make_response(jsonify({"message": "Reserva creada!", "reserva": reserva}), 201)

    except Exception as e:
        db.session.rollback()
        abort(400, description=str(e))

def retrieve_reservation(reservation_id):
    reservation = Reservas.query.get(reservation_id)
    if reservation is None:
        return {'error': 'Reserva no encontrada'}, 404
    return jsonify(reservation.to_dict())


def update_reservation(reservation_id, data):
    reserva = Reservas.query.get_or_404(reservation_id)
    try:
        reserva.observaciones = data.get('observaciones', reserva.observaciones)
        reserva.fecha = datetime.strptime(data.get('fecha', reserva.fecha.isoformat()), '%Y-%m-%d').date()
        reserva.hora = datetime.strptime(data.get('hora', reserva.hora.isoformat()), '%H:%M:%S').time()
        reserva.personas = data.get('personas', reserva.personas)
        db.session.commit()
        response = Reservas.query.get(reservation_id).to_dict()
        return jsonify(response)
    except Exception as e:
        db.session.rollback()
        abort(400, description=str(e))

def delete_reservation(id):
    reserva = Reservas.query.get_or_404(id)
    try:
        db.session.delete(reserva)
        db.session.commit()
        return jsonify({"message": "Reserva eliminada!"})
    except Exception as e:
        db.session.rollback()
        abort(400, description=str(e))