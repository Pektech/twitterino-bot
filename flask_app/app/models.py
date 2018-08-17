from flask_app.app import db

from datetime import datetime


class User(db.Model):
    id =  db.Column(db.Integer, primary_key=True)
    screen_name = db.Column(db.String(100), index=True, nullable=False, unique=True)
    tweets = db.relationship('Tweets', backref='user', lazy=True)

    def __repr__(self):
        return '<Screen name :  {}>'.format(self.screen_name)




class Tweets(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    twt_text = db.Column(db.Text(280), index=True)
    twt_date = db.Column(db.Date)
    twt_hash = db.Column(db.String(100),index=True)


class Monitor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    message = db.Column(db.Text(300))
