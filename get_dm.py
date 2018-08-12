# This file will do a quick search on the last 200 items
# for a specific hashtag and will automatically add new
# users to the account
# Start of Twitter Bot
import tweepy
import datetime
from time import sleep
# Config file is config.py and contains all the keys and
# secrets, a config.py file with your own version can be
# created here
from config import *
ln = "*"*50
try:
	x = api.direct_messages(full_text=True)
	for item in x:
		print("Sender: {0}, Message: {1} \n{2}\n".format(item.sender_screen_name,item.text,ln))
except tweepy.TweepError as error:
	print (error.reason)