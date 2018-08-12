# Import
import datetime
# Use directly
from pprint import pprint
from pymongo import MongoClient
from time import sleep
from config import *
# Log file
timestamp = '{:%Y-%m-%d-%H:%M:%S}'.format(datetime.datetime.now())
fileName = "logs/"+timestamp+"-build-friend-database.txt"
friendos = []
new_friendos = []
# MongoDB configuration, keeping it simple at the time
client = MongoClient('127.0.0.1', 27017)
db = client.information
posts_collection = db.posts
username_collection = db.username
f = open(fileName,"w")
x = 0

print("Fetching info to build username database in MongoDB...")
# Getting usernames from MongoDB, also adding them to list
for item in posts_collection.find():
	friendo = item['Screen Name']
	# Avoiding duplicates with this
	if friendo not in friendos:
		new_friendos.append(friendo)
		f.write(friendo+"\n")

for item in username_collection.find():
	username = item["Screen Name"]
	friendos.append(username)

for item in new_friendos:
	if item not in friendos:
		post_data = {"Screen Name":item}
		username_collection.insert_one(post_data)
		f.write("Inserted new friend into list: "+item+"\n")
		print("Added new possible friend to database :)")
		x += 1
	else:
		print("We already have "+item+" in our database, perhaps we could be friends!")
		f.write("Already have "+item+" in database\n")

print("Inserted "+str(x)+" new usernames to database")