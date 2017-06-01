from models.user import User
from routes import *
# for decorators
from functools import wraps

main = Blueprint('auth', __name__)
Model = User

@main.route('/')
def index():
    return render_template('login.html')

@main.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'POST':
        form = request.form
        u = User(form)
        user = User.query.filter_by(username=u.username).first()
        if u.login_verified(user):
            return redirect('/blog')
        flash('Wrong password')
        return redirect(url_for('.index'))
    return render_template('login.html')


@main.route('/register', methods=['GET','POST'])
def register():
    if request.method == 'POST':
        form = request.form
        u = User(form)
        user = User.query.filter_by(username=u.username).first()
        if u.register_verified() and user is None:
            u.save()
            flash('Register success, now you can login!')
            return redirect(url_for('.index'))
        flash('This name has been used!Change other one please!')
        return redirect(url_for('.index'))
    return render_template('register.html')
