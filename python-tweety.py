# Start of Twitter Bot
import tweepy
import time
# Config file is config.py and contains all the keys and
# secrets, a config.py file with your own version can be
# created here
from config import *
auth = tweepy.OAuthHandler ( consumer_key, consumer_secret )
auth.set_access_token ( access_token, access_token_secret )
# api has to be called for all functions
api = tweepy.API(auth, wait_on_rate_limit=True)

x=1
for item in sn:
	print("%s) %s | %s" % (x,item._json['screen_name'],item._json['location']))
	x+=1

sn = []
for page in tweepy.Cursor(api.followers, screen_name="rvfuturoayerhoy").pages():
    sn.extend(page)
    time.sleep(30)

print len(sn)