from flask import Flask 
from pymongo import MongoClient
 
app = Flask(__name__) 
client = MongoClient('127.0.0.1', 27017)
db = client.information
collection = db.posts
 
@app.route('/') 

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify( { 'error': 'Notfound' } ), 404)

def pymongo_data_display():
    my_data = collection.find_one()
    # add defensive programming at this point in case my_data is None
    return my_data
 
if __name__ == '__main__': 
        app.run()