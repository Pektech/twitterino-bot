# Import
from time import sleep
# Config file is config.py and contains all the keys and
# secrets, a config.py file with your own version can be
# created here
from config import *
# Log file
timestamp = '{:%Y-%m-%d-%H-%M-%S}'.format(datetime.datetime.now())
fileName = "logs/"+timestamp+"-friend-fetcher.txt"
friendos_list = []
# MongoDB configuration, keeping it simple at the time
client = MongoClient('127.0.0.1', 27017)
db = client.information
collection = db.posts
friendos = db.friendos
# Starting process
file_log = open(filename.format(timestamp,"friend-fetcher.txt"),"w")
file_log.write("Started process...")
fetch_from_mongo = "Fetching current info from MongoDB to avoid duplication..."
print(fetch_from_mongo)
file_log.write(fetch_from_mongo)

# Getting usernames from MongoDB, also adding them to list
for post in friendos.find():
	new = post['Screen Name']
	# Avoiding duplicates with this
	if new not in friendos_list:
		friendos_list.append(new)
fetch_from_twitter = "Fetching info from Twitter..."
print(fetch_from_twitter)
file_log.write(fetch_from_twitter)

# Get the list of friends off from Twitter
for follower in tweepy.Cursor(api.followers).items():
	try:
		if follower.screen_name not in friendos_list:
			post_data = {"Screen Name":follower.screen_name,"Name":follower.name,"Language":follower.lang,"Location":follower.location,"Follower":"Yes"}
			result = friendos.insert_one(post_data)
			inserted_user = 'Inserted {1} with ID: {0}'.format(result.inserted_id,follower.screen_name)
			print(inserted_user)
			file_log.write(inserted_user)
		else:
			already_in_db = "Screen name already in database"
			print(already_in_db)
			file_log.write(already_in_db)
		sleep(9)
	except tweepy.TweepError as error:
		print (error.reason)
		f.write("There was an error while trying to fetch information from Twitter, reason is:",error.reason)