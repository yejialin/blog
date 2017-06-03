from models.user import User
from routes import *
# for decorators

main = Blueprint('auth', __name__)


@main.route('/')
def index():
    return render_template('login.html')

@main.route('/login', methods=['GET'])
def view_login_get():
    return render_template('login.html')

@main.route('/login', methods=['POST'])
def view_login_post():
    form = request.form
    u = User(form)
    user = User.query.filter_by(username=u.username).first()
    if u.login_verified(user):
        session['u_id'] = user.id
        return redirect('/blog')
    flash('Wrong password')
    return redirect(url_for('.index'))

@main.route('/register', methods=['GET'])
def view_register_get():
    return render_template('register.html')

@main.route('/register', methods=['POST'])
def view_register_post():
    form = request.form
    u = User(form)
    user = User.query.filter_by(username=u.username).first()
    if u.register_verified() and user is None:
        u.save()
        flash('Register success, now you can login!')
        return redirect(url_for('.index'))
    flash('This name has been used!Change other one please!')
    return redirect(url_for('.index'))

@main.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('.index'))