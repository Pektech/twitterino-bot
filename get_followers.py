# This script will look for all followers and build
# us a nice list, 
# Start of Twitter Bot
import tweepy, os, datetime
from time import sleep
# Config file contains everything
from config import *
timestamp = '{:%Y-%m-%d-%H:%M:%S}'.format(datetime.datetime.now())
f = open('logs/'+timestamp+'-get-followers.log','w')
friendos = []
for follower in tweepy.Cursor(api.followers).items():
	try:
		friendos.append(follower.screen_name)
		timestamp = '{:%Y-%m-%d-%H:%M:%S}'.format(datetime.datetime.now())
		f.write(timestamp+" | "+follower.screen_name)
		print(follower.screen_name)
		sleep(9)
	except tweepy.TweepError as e:
		print (e.reason)