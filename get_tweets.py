# This script gets the full tweet of a user
import tweepy
import time
# Config file is config.py and contains all the keys and
# secrets, a config.py file with your own version can be
# created here
from config import *
# tid = "1023428296669712385"
tid = "1024516606641295360"
x = api.get_status(tid)
# print(x)
print(x)
# print("Screen Name: "+x._json['user']['screen_name']+"\nLocation: "+x._json['user']['location']+"\nTweet (Full): "+x._json['full_text'])