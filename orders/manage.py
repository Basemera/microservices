# from . import app
from app import app
from flask import jsonify


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=80)