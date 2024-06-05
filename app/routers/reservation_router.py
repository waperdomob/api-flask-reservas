from flask import Blueprint
from flask_restful import Api
from app.views.reserva_view import ReservasList, Reserva

reserva_routes = Blueprint('reserva', __name__)
api = Api(reserva_routes)

api.add_resource(ReservasList, '/reservas')
api.add_resource(Reserva, '/reservas/<int:id>')