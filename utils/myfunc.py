import copy

from flask import abort
from flask import session
from flask import redirect
from flask import url_for
from flask import flash
from functools import wraps
from models.user import User

def login_required(f):
    @wraps(f)
    def function(*arg, **kwargs):
        # Check login
        if session.get('u_id') is None:
            flash('Please login')
            return redirect(url_for('auth.index'))
        return f(*arg, **kwargs)
    return function

def get_username(u_id):
    user = User.query.filter_by(id=u_id).first()
    return user.username

def comments_handler(l):
    list = copy.deepcopy(l)
    for i in list:
        i.author_id = get_username(i.author_id)
    return list

def blog_delete_verified(b):
    u_id = session['u_id']
    user = User.query.filter_by(id=u_id).first()
    if (user.role == 0 or
        u_id == b.author_id):
        return True
    return False

def comment_delete_verifyied(b,c):
    cur_user_id = session['u_id']
    user = User.query.filter_by(id=cur_user_id).first()
    blog_user_id = b.author_id
    comm_user_id = c.author_id
    if (user.role == 0 or
        cur_user_id == blog_user_id or
        cur_user_id == comm_user_id):
        return True
    return False