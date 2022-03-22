from flask import Blueprint

users_api_blueprint = Blueprint('views', __name__)

from . import routes
