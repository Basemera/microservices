from email.policy import default
from . import db


class Item(db.Model):
    __tablename__ = 'items'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, default=1)
    title = db.Column(db.String(80), unique=True, nullable=False)
    content = db.Column(db.String(120), unique=True, nullable=False)

    def __init__(self, title, content, user_id):
        self.title = title
        self.content = content
        self.user_id = user_id

    @staticmethod
    def get_item(id):
        item = Item.query.get(id)
        if item:
            del item.__dict__['_sa_instance_state']

            return item.__dict__
        else:
            return []

    @staticmethod
    def get_user_items(id):
        items = []
        res = Item.query.filter_by(user_id=id).all()
        print(res)
        for item in res:
            del item.__dict__['_sa_instance_state']
            items.append(item)
            return items

    def save(self):
        item = db.session.add(self)
        db.session.commit()
