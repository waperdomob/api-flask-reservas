from flask import Flask
from flask_migrate import Migrate

from .database import db
from .routers.reservation_router import reserva_routes
from .config import config

migrate = Migrate()

def create_app():
    app = Flask(__name__)
    app.config.from_object(config["development"])

    db.init_app(app)
    migrate.init_app(app, db)

    app.register_blueprint(reserva_routes, url_prefix='/api')
    
    return app