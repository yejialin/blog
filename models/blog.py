from . import db
from . import ModelMixin

class Blog(db.Model, ModelMixin):
    __tablename__ = 'blogs'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String)
    content = db.Column(db.String)
    create_time = db.Column(db.String)
    author_id = db.Column(db.Integer, db.ForeignKey('users.id'))
