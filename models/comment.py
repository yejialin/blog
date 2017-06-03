from . import db
from . import ModelMixin
from . import get_cur_time

class Comment(db.Model, ModelMixin):
    __tablename__ = 'comments'
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String)
    create_time = db.Column(db.String)
    blog_id = db.Column(db.Integer, db.ForeignKey('blogs.id'))
    author_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    def __init__(self, form, b_id, u_id):
        self.content = form.get('c', '')
        self.blog_id = b_id
        self.author_id = u_id
        self.create_time = get_cur_time()

    def add_verified(self):
        return True