from models.blog import Blog
from routes import *

main = Blueprint('blog', __name__)
Model = Blog

@main.route('/')
def index():
    b = Model.query.all()
    return render_template('view.html', b=b)

@main.route('/blog/<b_id>')
def blog(b_id):
    b = Model.query.filter_by(id=b_id).first()
    return render_template('blog.html', b=b)