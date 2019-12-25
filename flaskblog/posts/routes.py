from flask import Blueprint, flash, url_for, render_template, request, abort, redirect
from flask_login import current_user, login_required
from flaskblog import db
from flaskblog.models import Post, User
from flaskblog.posts.forms import NewPostForm

posts = Blueprint('posts', __name__)


@posts.route("/posts/new", methods=['GET', 'POST'])
@login_required
def new_post():
    form = NewPostForm()
    if form.validate_on_submit():
        new_post_object = Post(author=current_user, title=form.title.data, content=form.content.data)
        db.session.add(new_post_object)
        db.session.commit()
        flash('You have sucessfully created a post!', 'success')
        return redirect(url_for('main.index'))

    return render_template('newpost.html', title='New Post', form=form, legend='New post')


@posts.route("/posts/<int:post_id>")
def post(post_id):
    post = Post.query.get_or_404(post_id)
    return render_template('post.html', title=post.title, post=post)


@posts.route("/posts/<int:post_id>/update", methods=['GET', 'POST'])
@login_required
def update_post(post_id):
    post = Post.query.get_or_404(post_id)
    if post.author != current_user:
        abort(403)
    form = NewPostForm()
    if form.validate_on_submit():
        post.title = form.title.data
        post.content = form.content.data
        db.session.commit()
        flash('Your post was updated sucessfully!', 'success')
        return redirect(url_for('posts.post', post_id=post.id))
    elif request.method == 'GET':
        form.title.data = post.title
        form.content.data = post.content
    return render_template('newpost.html', title="Update post", legend="Update Post", form=form)


@posts.route("/posts/<int:post_id>/delete", methods=['POST'])
@login_required
def delete_post(post_id):
    post = Post.query.get_or_404(post_id)
    if post.author != current_user:
        abort(403)
    db.session.delete(post)
    db.session.commit()
    flash('Your post has been Deleted', 'success')
    return redirect(url_for('main.index'))


