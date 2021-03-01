from flask import Blueprint

qr = Blueprint('qr', __name__, url_prefix='/qr', template_folder='templates')

from . import views