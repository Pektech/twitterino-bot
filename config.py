import tweepy, datetime
from pymongo import MongoClient
# Keys, there have been hardcoded here but these keys
# are to be setup by an installation script
consumer_key = 'XXX'
consumer_secret = 'XXX'
access_token = 'XXX'
access_token_secret = 'XXX'
# These are used everywhere for tweepy auth
auth = tweepy.OAuthHandler ( consumer_key, consumer_secret )
auth.set_access_token ( access_token, access_token_secret )
api = tweepy.API(auth, wait_on_rate_limit=True)
# MongoDB info
client = MongoClient('127.0.0.1', 27017)
db = client.information
username_collection = db.friendos
posts_collection = db.posts
monitor_collection = db.monitor
# Log files
timestamp = '{:%Y-%m-%d-%H-%M-%S}'.format(datetime.datetime.now())
filename = "logs/{0}-{1}"
