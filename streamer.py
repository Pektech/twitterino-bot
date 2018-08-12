# Start of Twitter Bot
# If troubleshooting is required then add the flags
# -l "1" -v "1" which will provide all the information
# being sent to the storage
import time, argparse, re, json
# Config file is config.py and contains all the keys and
# secrets, a config.py file with your own version can be
# created here
from config import *
# Start mongo stuff
# Start flags
parser = argparse.ArgumentParser()
# -q QUERY -l LISTENER -v VERBOSE
parser.add_argument("-q","--query",help="Hashtag or subject to look up")
parser.add_argument("-l","--listener",help="Print results to screen")
parser.add_argument("-v","--verbose",help="Setup level of verbose for troubleshooting")
args = parser.parse_args()
linebreak = "+"*50
# file_log requires that the timestamp and file name 
# are pushed into it
file_log = open(filename.format(timestamp,"streamer.txt"),"w")

class MyStreamListener(tweepy.StreamListener):

    def on_status(self, status):
        try:
            media_url = entities['media'][0]['media_url']
        except:
            media_url = "N/A"
            pass
        if 'retweeted_status' in status._json:
            try:
                tweet_text = status._json['retweeted_status']['extended_tweet']['full_text']
            except:
                if debug == 1:
                    print("There is no retweeted key here")
                    print(status._json)
                tweet_text = status._json['text']
        elif 'retweeted_status' not in status._json:
            try:
                tweet_text = status._json['extended_tweet']['full_text']
            except:
                if debug == 1:
                    print("This is not a normal tweet?")
                    print(status._json)
                tweet_text = status._json['text']
        else:
            print(status._json)
            file_log.write("Possible error found in stream, pushing info into log:\n")
            file_log.write(status._json)
        if debug == 1:
            chars_tweet = len(tweet_text)
            print("XXX\nTweet Text Characters:"+str(chars_tweet)+"\nXXX")
        hashtags = re.findall(r'(#\S*)', tweet_text, re.MULTILINE)
        full_tweet = "{0}\nCreation: {1} | Screen Name: {2} | Tweet: {3} | Tweet ID: {4} | Location: {5} | Language: {6} | Media: {7} | Hashtags: {8}\n{0}\n".format(linebreak,status.created_at,status.user.screen_name,tweet_text,status.id,status.user.location,status.user.lang,media_url,hashtags)
        if listen == 1:
            print(full_tweet)
        file_log.write(full_tweet)
        post_data = {'Timestamp':status.created_at,'Screen Name':status.user.screen_name,'Tweet':tweet_text,'Tweet ID':status.id,'Location':status.user.location,'Language':status.user.lang,'Media':media_url,'Hashtags':hashtags}
        result = posts_collection.insert_one(post_data)
        print('Post inserted with ID: {0}'.format(result.inserted_id))

    def on_error(self, status_code):
    	if status_code == 420:
    		#returning False in on_error disconnects the stream
    		#returning non-False values reconnects the stream
            file_log.write("Error with status code 420 found during stream\n")
            return True

if args.query != None:
	user_query = args.query
else:
	user_query = input("Type hashtag or subject to ride from: ")
if args.verbose == "1":
    debug = 1
elif args.verbose == "0":
    debug = 0
else:
    print("Invalid option, verbose not enabled")
    debug = 0
if args.listener == "1":
    listen = 1
elif args.listener == "0":
    listen = 0
else:
    print("Invalid option, printing to screen will not be enabled")
    listen = 0
print("Starting stream listener...")
file_log.write("{0}: Started stream with query {1}".format(timestamp,user_query))
myStreamListener = MyStreamListener()
myStream = tweepy.Stream(auth = api.auth, listener=myStreamListener, tweet_mode='extended')
myStream.filter(track=[user_query])