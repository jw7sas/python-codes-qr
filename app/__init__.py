from flask import Flask
from .config import Config
from .qr import qr

def create_app():
    """ Método de creación de la app de Flask. """
    app = Flask(__name__)

    app.config.from_object(Config)
    app.register_blueprint(qr)

    return app