from routes import *

main = Blueprint('error', __name__)


@main.route('/<err>')
def error_handler(err):
    return render_template('error.html', e=err)

