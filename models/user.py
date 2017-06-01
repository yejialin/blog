from . import db
from . import ModelMixin

class User(db.Model, ModelMixin):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, unique=True)
    password = db.Column(db.String)
    role = db.Column(db.Integer)

    def __init__(self, form):
        self.username = form.get('u', '')
        self.password = form.get('p', '')
        self.role= 1

    def login_verified(self, user):
        if user is not None:
            if (self.username == user.username
                and self.password ==user.password):
                return True
        return False


    def register_verified(self):
        pass
        return True
