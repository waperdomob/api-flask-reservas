from flask import request
from flask_restful import Resource
from app.services.reserva import list_all_reservations, create_reservation, retrieve_reservation, update_reservation, delete_reservation

class ReservasList(Resource):
    def get(self):
        return list_all_reservations()

    def post(self):
        data = request.get_json()
        return create_reservation(data)

class Reserva(Resource):
    def get(self, id):
        reservation = retrieve_reservation(id)
        return reservation

    def put(self, id):
        data = request.get_json()
        return update_reservation(id, data)

    def delete(self, id):
        return delete_reservation(id)
