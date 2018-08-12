# Import
import datetime, sys
# Use directly
from pprint import pprint
from time import sleep
# Config file is config.py and contains all the keys and
# secrets, a config.py file with your own version can be
# created here
from config import *
# Log file
timestamp = '{:%Y-%m-%d-%H-%M-%S}'.format(datetime.datetime.now())
file_name = "logs/"+timestamp+"-mongodump-friends-tweepy.txt"
friendos = []
new_friendos = []
# MongoDB configuration, keeping it simple at the time
log_file = open(file_name,"w")

def on_error(error,log_file):
	log_file.write("Tuvimos un error ({0}): {1}\n".format(error.api_code,error.args[0][0]['message']))
	if error.api_code == 161:
		print("Error Code 161: "+error.args[0][0]['message']+"\nTerminating script.")
		sys.exit()
	else:
		print("Tuvimos un error ({0}): {1}\n".format(error.api_code,error.args[0][0]['message']))

print("Fetching info of all possible new friends we have in MongoDB...")
y = 0
# Getting usernames from MongoDB, also adding them to list
for post in posts_collection.find():
	new = post['Screen Name']
	# Avoiding duplicates with this
	if new not in new_friendos:
		new_friendos.append(new)
		y += 1

z = 0
print("Fetching info of all current friends we have in MongoDB...")
# Getting usernames from MongoDB, also adding them to list
for post in username_collection.find():
	current = post['Screen Name']
	friendos.append(current)
	z += 1

print("Figuring out if we have new friends to follow...")
# Add potential new friendos!
x=0
for friendo in new_friendos:
	if friendo not in friendos:
		try:
			print("Agregando al usuario @" + friendo)
			api.create_friendship(screen_name=friendo)
			log_file.write("Se agrego al usuario: @" + friendo + " \n")
			friendos.append(friendo)
			x += 1
			sleep(5)
		except tweepy.TweepError as error:
			on_error(error,log_file)

	else:
		try:
			print("El usuario @" + friendo + " ya nos sigue!")
			log_file.write("Se encontro un usuario que ya nos sigue: @" + friendo + "\n")
		except tweepy.TweepError as error:
			on_error(error,log_file)

print("Read through {0} unique posts, we have {1} friends and we added {2} friends".format(y,z,x))