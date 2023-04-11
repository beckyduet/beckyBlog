from flask import render_template, redirect, url_for, abort, flash, request, \
    current_app
from flask_login import login_required, current_user

from . import main
from .forms import PostForm
from .. import db
from ..models import Post


@main.route('/', methods=['GET', 'POST'])
def index():
    page = request.args.get('page', 1, type=int)
    category = request.args.get('category', None, type=str)
    if category is not None:
        query = Post.query.filter_by(category=category)
    else:
        query = Post.query
    pagination = query.order_by(Post.timestamp.desc()).paginate(
        page=page, per_page=current_app.config['FLASKY_POSTS_PER_PAGE'],
        error_out=False)
    posts = pagination.items
    return render_template('index.html', posts=posts, pagination=pagination)


@main.route('/post/<int:id>', methods=['GET', 'POST'])
def post(id):
    post = Post.query.get_or_404(id)
    # print(post.body)
    return render_template('post.html', posts=post)


@main.route('/admin', methods=['GET', 'POST'])
@login_required
def admin():
    form = PostForm()
    if form.validate_on_submit():
        body_html = request.form.get("editormd-html-code")
        post = Post(title=form.title.data, description=form.description.data, body=form.body.data, body_html=body_html,
                    category=form.category.data, img_url=form.img_url.data, author_id=current_user.id)
        db.session.add(post)
        db.session.commit()
        return redirect(url_for('.index'))
    return render_template("admin.html", form=form)


@main.route('/learn-sql', methods=['GET', 'POST'])
def learn_sql():
    return render_template('learn_sql.html')


@main.route('/resume', methods=['GET', 'POST'])
def resume():
    return render_template("resume.html")


@main.route('/admin/edit/<int:post_id>', methods=['GET', 'POST'])
@login_required
def edit(post_id):
    post = Post.query.get_or_404(post_id)
    if post.author_id != current_user.id:
        abort(403)
    form = PostForm()

    if form.validate_on_submit():
        post.id = post_id
        post.title = form.title.data
        post.description = form.description.data
        post.img_url = form.img_url.data
        post.category = form.category.data
        post.body = form.body.data
        db.session.add(post)
        db.session.commit()
        flash('The post has been updated.')
        return redirect(url_for('.post', id=post.id))

    form.title.data = post.title
    form.description.data = post.description
    form.img_url.data = post.img_url
    form.category.data = post.category
    form.body.data = post.body
    return render_template('edit.html',form=form,post_id=post_id)
