from app import app, db
from flask import render_template, request,flash, session
from .models import User, Tweets
from .utils import ip_logging

import datetime

@app.route('/')
def index():
    x_real_ip = request.environ.get('HTTP_X_Real_IP')
    remote_ip = x_real_ip or request.remote_addr
    timestamp = '{:%Y-%m-%d-%H:%M:%S}'.format(datetime.datetime.now())
    message = "{0}: Access requested to {1} from IP address (Real IP: {2} | " \
              "Remote IP: {3})".format(
        timestamp, "Main page", x_real_ip, remote_ip)
    flash(message)
    return render_template('index.html', title="Twitter Bot")


@app.route('/users')
def users():
    users = User.query.all()
    x_real_ip = request.environ.get('HTTP_X_Real_IP')
    remote_ip = x_real_ip or request.remote_addr
    timestamp = '{:%Y-%m-%d-%H:%M:%S}'.format(datetime.datetime.now())
    message = "{0}: Access requested to {1} from IP address (Real IP: {2} | " \
              "Remote IP: {3})".format(
        timestamp, "Users", x_real_ip, remote_ip)
    flash(message)
    return render_template('users.html', title="Users", users=users)


@app.route('/posts')
@ip_logging
def posts():
    posts  = User.query.all()


    return render_template('posts.html', title="Posts", posts=posts)
