import tornado.ioloop
import tornado.web
import tornado.autoreload
import datetime
from config import *
# MongoDB configuration
# Static files that are monitored by watch and used by routes
static_files = ["templates/template.html","templates/posts.html"]

class UsersHandler(tornado.web.RequestHandler):
	def get(self):
		friendos = []
		for friend in username_collection.find():
			friendos.append(friend["Screen Name"])
		self.render(static_files[0], title="Twitter Bot - Friends", items=friendos)
		x_real_ip = self.request.headers.get("X-Real-IP")
		remote_ip = x_real_ip or self.request.remote_ip
		timestamp = '{:%Y-%m-%d-%H:%M:%S}'.format(datetime.datetime.now())
		message = "{0}: Access requested to {1} from IP address (Real IP: {2} | Remote IP: {3})".format(timestamp,static_files[0],x_real_ip,remote_ip)
		print(message)
		post_data = {"Timestamp":timestamp,"Message":message}
		monitor_collection.insert_one(post_data)

class PostsHandler(tornado.web.RequestHandler):
	def get(self):
		posts = []
		for item in posts_collection.find():
			posts.append(item)
		# Render will push the static file which is a template, the arguments
		# passed onto this contain some of the information to be filled out
		self.render(static_files[1], title="Twitter Bot - Posts", items=posts)
		x_real_ip = self.request.headers.get("X-Real-IP")
		remote_ip = x_real_ip or self.request.remote_ip
		timestamp = '{:%Y-%m-%d-%H:%M:%S}'.format(datetime.datetime.now())
		message = "{0}: Access requested to {1} from IP address (Real IP: {2} | Remote IP: {3})".format(timestamp,static_files[1],x_real_ip,remote_ip)
		print(message)
		post_data = {"Timestamp":timestamp,"Message":message}
		monitor_collection.insert_one(post_data)

class MainHandler(tornado.web.RequestHandler):
	def get(self):
		# Example of a single item to be written out
		self.write("""<html><title>Twitter Bot</title>
			<center> Welcome to the Twitter Bot web interface, powered by Python and Tornado
			<p><a href='/users'>Users in MongoDB</a></p>
			<p><a href='/posts'>Posts in MongoDB</a></p>
			</center>
			</html>""")
		x_real_ip = self.request.headers.get("X-Real-IP")
		remote_ip = x_real_ip or self.request.remote_ip
		timestamp = '{:%Y-%m-%d-%H:%M:%S}'.format(datetime.datetime.now())
		message = "{0}: Access requested to {1} from IP address (Real IP: {2} | Remote IP: {3})".format(timestamp,"Main page",x_real_ip,remote_ip)
		print(message)
		post_data = {"Timestamp":timestamp,"Message":message}
		monitor_collection.insert_one(post_data)

def make_app():
    return tornado.web.Application([
        (r"/users", UsersHandler),
        (r"/posts", PostsHandler),
        (r"/", MainHandler)
    ])

if __name__ == "__main__":
	app = make_app()
	app.listen(8888)
	tornado.autoreload.start()
	for file in static_files:
		tornado.autoreload.watch(file)
	timestamp = '{:%Y-%m-%d-%H:%M:%S}'.format(datetime.datetime.now())
	post_data = {"Timestamp":timestamp,"Message":"Initiated or reloaded tornado server"}
	monitor_collection.insert_one(post_data)
	tornado.ioloop.IOLoop.current().start()