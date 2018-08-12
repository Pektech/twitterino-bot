# This was originally takenm from GitHub from user vickyqian
import tweepy
import csv
from time import sleep
#import pandas as pd
from config import *

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth,wait_on_rate_limit=True)
#####United Airlines
# Open/Create a file to append data
csvFile = open('queleer.csv', 'w', encoding="utf-8")
#Use csv Writer
csvWriter = csv.writer(csvFile)
x=0
# The below code with look only for items in the English language
#for tweet in tweepy.Cursor(api.search,q="#queleer",count=100,
#                           lang="en",
#                           since="2018-01-01").items():
for tweet in tweepy.Cursor(api.search,q="#queleer",count=100,
                           since="2018-01-01").items(1000):
	print("(%s)|%s: %s" % (tweet.created_at, tweet.text, tweet.user._json["screen_name"]))
	csvWriter.writerow([tweet.created_at, tweet.text, tweet.user._json["screen_name"]])
	x+=1
	sleep(1)

print("Mined %s tweets, be-bop!" % x)