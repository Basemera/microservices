from flask import jsonify, request, make_response
from ..models import Item
from . import order_api_blueprint
from .clients.user_client import get_user

@order_api_blueprint.route('/home', methods=['GET'])
def home():
  return jsonify(
      {
          "hello": "world"
      }
  )

@order_api_blueprint.route('/items/<id>', methods=['GET'])
def get_item(id):  
  return jsonify(Item.get_item(id))

# @order_api_blueprint.route('/items', methods=['GET'])
# def get_items():
#   items = []
#   for item in db.session.query(Item).all():
#     del item.__dict__['_sa_instance_state']
#     items.append(item.__dict__)
#   return jsonify(items)

@order_api_blueprint.route('/items', methods=['POST'])
def create_item():
  body = request.get_json()
  # get user
  try:
    user = get_user(body['user_id'])
  except Exception as exc:
    return make_response({
      'error': "Exception",
      'exception': str(TimeoutError)
    }, 500)
  if user['status'] != 200:
    return make_response({
      'error': "user note found"
    }, 404)
  

  item = Item(title=body['title'], content=body['content'])
  item.save()
  return make_response({
    'id': item.id,
    'name': item.title
  })

# @order_api_blueprint.route('/items/<id>', methods=['PUT'])
# def update_item(id):
#   body = request.get_json()
#   db.session.query(Item).filter_by(id=id).update(
#     dict(title=body['title'], content=body['content']))
#   db.session.commit()
#   return "item updated"

# @order_api_blueprint.route('/items/<id>', methods=['DELETE'])
# def delete_item(id):
#   db.session.query(Item).filter_by(id=id).delete()
#   db.session.commit()
#   return "item deleted"
