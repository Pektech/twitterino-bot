from flask_app.app import app
from flask import render_template, request,flash, session, url_for
from .models import User
from .utils import ip_logging

import datetime

@app.route('/')
@ip_logging()
def index():

    return render_template('index.html', title="Twitter Bot")


@app.route('/users')
@ip_logging('Users')
def users():
    users = User.query.all()

    return render_template('users.html', title="Users", users=users)


@app.route('/posts')
@ip_logging('Posts')

def posts():
    page = request.args.get('page', 1, type=int)
    posts  = User.query.order_by(User.id.desc()).paginate(page,
                                    app.config['POSTS_PER_PAGE'],False)
    next_url = url_for('posts', page=posts.next_num) \
        if posts.has_next else None

    prev_url = url_for('posts', page=posts.prev_num) \
        if posts.has_prev else None


    return render_template('posts.html', title="Posts", posts=posts.items,
                           next_url=next_url, prev_url=prev_url)
