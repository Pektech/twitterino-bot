# Start of Twitter Bot
# This script allows us to follow users back
# from the list of users we currently follow
# this may or not be required but is always
# a nice feature.
import tweepy
import time
import json
# Config file is config.py and contains all the keys and
# secrets, a config.py file with your own version can be
# created here
from config import *
auth = tweepy.OAuthHandler ( consumer_key, consumer_secret )
auth.set_access_token ( access_token, access_token_secret )
# api has to be called for all functions
api = tweepy.API(auth, wait_on_rate_limit=True)
me = api.me()

x=1
for follower in tweepy.Cursor(api.followers).items():
	try:
		source_user = follower.screen_name
		target_user = me.screen_name
		# The way it is setup lets us know if we are following
		# the account which is currently following us
		areWeFriends = api.show_friendship(source_screen_name=source_user,target_screen_name=target_user)
		# areWeFriends 0 indicates the follower, areWeFriends 1 indicates us
		following = areWeFriends[0].followed_by
		if following == True:
			print("We are already following "+source_user)
		else:
			print("We are not following "+source_user+", but we can always follow them back! :)")
			api.create_friendship(screen_name=source_user)
	except tweepy.TweepError as e:
		print(x,e)
		pass
	x+=1