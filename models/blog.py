from . import db
from . import ModelMixin
from . import get_cur_time

class Blog(db.Model, ModelMixin):
    __tablename__ = 'blogs'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String)
    content = db.Column(db.String)
    create_time = db.Column(db.String)
    author_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    def __init__(self, form, id):
        self.title = form.get('t', '')
        self.content = form.get('c', '')
        self.author_id = id
        self.create_time = get_cur_time()

    def add_verified(self):
        return True

