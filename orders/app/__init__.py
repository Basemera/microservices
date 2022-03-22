from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import os

db = SQLAlchemy()

app = Flask(__name__)
from .views import order_api_blueprint

app.register_blueprint(order_api_blueprint)

app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL')
db.init_app(app)
Migrate(app, db)
