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
import re

mined_friends = []
f = open("logs/monitoring.txt",'r')
for item in f:
	z = re.findall('\s*Screen Name: (\S*)',item)
	try:
		if z[0] not in mined_friends:
			mined_friends.append(z[0])
		else:
			pass
	except:
		pass

# Open file and designate list for friendos
fileName = "logs/"+timestamp+"-regex-nuevos_usuario-tweepy.txt"
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

# Time to check if we have new friends to follow!
for item in mined_friends:
	try:
		# Si el usuario ya es nuestro amigo no lo agregamos
		if item in friendos:
			print("El usuario @" + item + " ya es nuestro amigo!")
			f.write("Se encontro un usuario que ya nos sigue y seguimos: " + item + "\n")
		else:
			# Vamos a ver quien hizo un Tweet
			print("Agregando al usuario @" + item + "\n")
			# Vamos a seguir al usuario
			api.create_friendship(screen_name=item)
			# Vamos a calmar el tren que va muy rapido
			f.write("Se agrego al usuario: " + item + "\n")
			friendos.append(friendo)
			sleep(5)
	except:
		f.write("Tuvimos un error en esta linea\n")
		pass
f.close()