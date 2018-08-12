import tweepy, time, sys, random, pickle, pprint, os
from config import *
# argfile = str(sys.argv[1])
auth = tweepy.OAuthHandler ( consumer_key, consumer_secret )
auth.set_access_token ( access_token, access_token_secret )

api = tweepy.API(auth)
data = api.rate_limit_status()
pid = os.getpid()
print(pid)
#print(data['resources'])
print(data['resources']['followers']['/followers/list']['remaining'])
#print(data['resources']['statuses']['/statuses/home_timeline'])
#print(data['resources']['users']['/users/lookup'])
print(data['resources']['followers'])
