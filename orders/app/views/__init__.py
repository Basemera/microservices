from flask import Blueprint

order_api_blueprint = Blueprint('views', __name__)

from . import routes
