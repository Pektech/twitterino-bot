# Import
import datetime
# Use directly
from pprint import pprint
from pymongo import MongoClient
from time import sleep
# Config file is config.py and contains all the keys and
# secrets, a config.py file with your own version can be
# created here
from config import *
# Log file
timestamp = '{:%Y-%m-%d-%H-%M-%S}'.format(datetime.datetime.now())
fileName = "logs/"+timestamp+"-mongodump-nuevos_usuario-tweepy.txt"
friendos = []
newFriendos = []
# MongoDB configuration, keeping it simple at the time
client = MongoClient('127.0.0.1', 27017)
db = client.information
collection = db.posts
f = open(fileName,"w")

print("Fetching info from MongoDB...")
# Getting usernames from MongoDB, also adding them to list
for post in collection.find():
	new = post['Screen Name']
	# Avoiding duplicates with this
	if new not in newFriendos:
		newFriendos.append(new)

print("Fetching info from Twitter...")
# Get the list of friends off from Twitter
for follower in tweepy.Cursor(api.followers).items():
	try:
		friendos.append(follower.screen_name)
		sleep(9)
	except tweepy.TweepError as e:
		print (e.reason)

print("Figuring out if we have new friends to follow...")
# Add potential new friendos!
for friendo in newFriendos:
	if friendo not in friendos:
		try:
			print("Agregando al usuario @" + friendo + "\n")
			api.create_friendship(screen_name=friendo)
			f.write("Se agrego al usuario: @" + friendo + " \n")
			friendos.append(friendo)
			sleep(5)
		except tweepy.TweepError as e:
			print(e.reason)
			f.write("Tuvimos un error: "+e.reason+"\n")
	else:
		try:
			print("El usuario @" + friendo + " ya nos sigue!")
			f.write("Se encontro un usuario que ya nos sigue: @" + friendo + "\n")
			sleep(5)
		except tweepy.TweepError as e:
			print(e.reason)
			f.write("Tuvimos un error: "+e.reason+"\n")