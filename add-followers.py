# Start of Twitter Bot
import tweepy
import time
# Config file is config.py and contains all the keys and
# secrets, a config.py file with your own version can be
# created here
from config import *

for follower in tweepy.Cursor(api.followers).items():
	try:
		follower.follow()
		print(x,follower.screen_name)
	except tweepy.TweepError as e:
		print(x,e)
		pass