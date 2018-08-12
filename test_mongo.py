from pymongo import MongoClient
from time import sleep
client = MongoClient('192.168.1.56',27017)
db = client.information
posts_collection = db.posts
print(posts_collection.count())
print("Initial 1000 items: ")
for item in posts_collection.find().limit(1000):
	print(item)
print("Chill after 1000 items")
sleep(10)
skip = 1000
while True:
	try:
		print("*"*50)
		for item in posts_collection.find().skip(skip).limit(1000):
			if item == None:
				print("Nada, my friendo")
			else:
				print(item)
		query = input("More? Y/N: ")
		if query.lower() == "n":
			break
		elif query.lower() == "y":
			skip += 1000
	except:
		print("The end probably")
		break