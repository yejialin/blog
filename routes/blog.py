from models.blog import Blog
from models.comment import Comment
from routes import *

main = Blueprint('blog', __name__)


@main.route('/')
def index():
    b = Blog.query.all()
    return render_template('view.html', b=b)

@main.route('/blog/<b_id>', methods=['GET'])
def view_blog_get(b_id):
    b = Blog.query.filter_by(id=b_id).first()
    uname = get_username(b.author_id)
    session['b_id'] = b.id
    c = Comment.query.filter_by(blog_id=b_id).all()
    hc = comments_handler(c)
    return render_template('blog.html', b=b, un=uname, c=hc)

@main.route('/blog/<b_id>', methods=['POST'])
@login_required
def view_blog_post(b_id):
    form = request.form
    c = Comment(form, session['b_id'], session['u_id'])
    if c.add_verified():
        c.save()
        return redirect(url_for('.view_blog_get', b_id=session['b_id']))

@main.route('/add', methods=['GET'])
@login_required
def add_blog_get():
    return render_template('add_blog.html')

@main.route('/add', methods=['POST'])
@login_required
def add_blog_post():
    form = request.form
    b = Blog(form, session['u_id'])
    if b.add_verified():
        b.save()
        return redirect(url_for('.index'))

@main.route('/blog/<b_id>/delete')
@login_required
def delete_blog(b_id):
    b = Blog.query.filter_by(id=b_id).first()
    if b is None:
        return redirect(url_for('error.error_handler', err='This blog is not existed.'))
    elif blog_delete_verified(b):
        b.delete()
        return redirect(url_for('.index'))
    else:
        return redirect(url_for('error.error_handler', err='Permission deny'))

@main.route('/blog/<b_id>/<c_id>/delete')
@login_required
def delete_comment(b_id, c_id):
    c = Comment.query.filter_by(id=c_id).first()
    b = Blog.query.filter_by(id=b_id).first()
    if c is None:
        return redirect(url_for('error.error_handler', err='This comment is not existed.'))
    elif comment_delete_verifyied(b, c):
        c.delete()
        return redirect(url_for('.view_blog_get', b_id=session['b_id']))
    else:
        return redirect(url_for('error.error_handler', err='Permission deny'))
