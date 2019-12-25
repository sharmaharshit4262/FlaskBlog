from flask import Blueprint, request, render_template
from flaskblog.models import Post

main = Blueprint('main', __name__)


@main.route("/")
@main.route("/home/")
def index():
    page = request.args.get('page', default=1, type=int)
    posts = Post.query.order_by(Post.date_posted.desc())\
        .paginate(per_page=5, page=page)
    return render_template('index.html', posts=posts)


@main.route("/about/")
def about():
    return render_template('about.html', title='About')


