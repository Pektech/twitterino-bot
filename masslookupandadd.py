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
auth = tweepy.OAuthHandler ( consumer_key, consumer_secret )
auth.set_access_token ( access_token, access_token_secret )
# api has to be called for all functions
# All variables and functions defined
api = tweepy.API(auth, wait_on_rate_limit=True)
timestamp = '{:%Y-%m-%d-%H:%M:%S}'.format(datetime.datetime.now())
query = input("Hashtag o item para busqueda: ")
fileName = "logs/"+timestamp+"-"+query.strip("#")+"-nuevos_usuario-tweepy.txt"
friendos = []
# We open a new file to save our info
f = open(fileName,"w")
opening = "Vamos a agregar usuarios y generar una lista"
print(opening)
f.write("===============\n" + opening + "\n")

# Create a the usernames that follow us
for follower in tweepy.Cursor(api.followers).items():
	try:
		friendos.append(follower.screen_name)
	except tweepy.TweepError as e:
		print (e.reason)

for tweet in tweepy.Cursor(api.search,q=query).items(200):
	try:
		friendo = tweet.user.screen_name
		# Si el usuario ya es nuestro amigo no lo agregamos
		if friendo in friendos:
			print("El usuario @" + friendo + " ya es nuestro amigo!")
			f.write("Se encontro un usuario que ya nos sigue y seguimos: " + friendo + "\n")
			sleep(5)
		else:
			# Vamos a ver quien hizo un Tweet
			print("Agregando al usuario @" + friendo + " | " + tweet.text)
			# Vamos a seguir al usuario
			tweet.user.follow()
			# Vamos a calmar el tren que va muy rapido
			f.write("Se agrego al usuario: " + friendo + " | " + tweet.text + "\n")
			friendos.append(friendo)
			sleep(5)
	except tweepy.TweepError as e:
		print (e.reason)
		f.write("Tuvimos un error con el usuario " + friendo + "\n")
		f.write(e.reason)
		sleep(5)
		pass
f.close()