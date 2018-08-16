from flask_app.app import db
from .models import User, Tweets
from flask import request, flash
from functools import wraps
import csv
import datetime

#helper functions

def csv_names(csv_file):
    with open(csv_file) as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            user = User()
            user.screen_name = row['screen_name']
            db.session.add(user)
            db.session.commit()




def csv_tweets(csv_file):
    with open(csv_file) as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            tweet = Tweets()
            tweet.user_id = row['user_id']
            tweet.twt_text = row['twt_text']
            tweet.twt_date = datetime.datetime.strptime(row['twt_date'], '%m/%d/%Y')
            tweet.twt_hash = row['twt_hash']
            db.session.add(tweet)
            db.session.commit()


def ip_logging(func):
    @wraps(func)
    def decorated_function(*args, **kwargs):
        x_real_ip = request.environ.get('HTTP_X_Real_IP')
        remote_ip = x_real_ip or request.remote_addr
        timestamp = '{:%Y-%m-%d-%H:%M:%S}'.format(datetime.datetime.now())
        message = "{0}: Access requested to {1} from IP address (Real IP: {2} " \
                  "| Remote IP: {3})".format(
            timestamp, "Users", x_real_ip, remote_ip)
        flash(message)

        return func(*args, **kwargs)
    return decorated_function