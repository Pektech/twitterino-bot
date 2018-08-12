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

# Import arguments
import argparse
parser = argparse.ArgumentParser()
# -t TWEET
parser.add_argument("-t","--tweet",help="Status update on account tied to keys")
args = parser.parse_args()
query = args.tweet
print(query)

if query == None:
	query = input("What to tweet: ")
timestamp = '{:%Y-%m-%d-%H:%M:%S}'.format(datetime.datetime.now())
fileName = "logs/"+timestamp+"-tweets.txt"
# We open a new file to save our info
f = open(fileName,"w")
try:
	api.update_status(status=query)
	print("Tweeted to our account: ",query)
except tweepy.TweepError as e:
	print (e.reason)
	f.write(e.reason)
f.close()