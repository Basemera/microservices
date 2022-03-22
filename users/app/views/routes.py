from time import sleep
from flask import jsonify, request
from app import db
from ..models import User
from . import users_api_blueprint

is_maintenance_mode = False


@users_api_blueprint.before_request
def check_for_maintenance():
    if is_maintenance_mode: 
        return 'Sorry, off for maintenance!', 503



@users_api_blueprint.route('/', methods=['GET'])
def home():
  return jsonify(
      {
          "hello": "world users"
      }
  )

@users_api_blueprint.route('/users/<id>', methods=['GET'])
def get_user(id):
  sleep(10)
  user = User.query.get(id)
  del user.__dict__['_sa_instance_state']
  return jsonify(user.__dict__)

@users_api_blueprint.route('/users', methods=['GET'])
def get_users():
  users = []
  for user in db.session.query(User).all():
    del user.__dict__['_sa_instance_state']
    users.append(user.__dict__)
  return jsonify(users)

@users_api_blueprint.route('/users', methods=['POST'])
def create_user():
  body = request.get_json()
  db.session.add(User(body['first_name'], body['last_name']))
  db.session.commit()
  return "user created"

@users_api_blueprint.route('/users/<id>', methods=['PUT'])
def update_item(id):
  body = request.get_json()
  db.session.query(User).filter_by(id=id).update(
    dict(first_name=body['first_name'], last_name=body['last_name']))
  db.session.commit()
  return "user updated"

@users_api_blueprint.route('/users/<id>', methods=['DELETE'])
def delete_user(id):
  db.session.query(User).filter_by(id=id).delete()
  db.session.commit()
  return "user deleted"
