from pyrebase import pyrebase
from flask import Flask
from flask_cors import CORS, cross_origin
import json

app = Flask(__name__, static_folder="../build", static_url_path='/')
CORS(app)

db_config = {
    "apiKey": "AIzaSyBtnDvZYWimGywQYQ-vvFpU5bVz2o3dmBg",
    "authDomain": "allergenius-84e72.firebaseapp.com",
    "databaseURL": "https://allergenius-84e72-default-rtdb.europe-west1.firebasedatabase.app",
    "projectId": "allergenius-84e72",
    "storageBucket": "allergenius-84e72.appspot.com",
    "messagingSenderId": "652605483025",
    "appId": "1:652605483025:web:320cce73e5a10fb33869b0",
    "measurementId": "G-4GL14PE1B4"
}

firebase = pyrebase.initialize_app(db_config)
db = firebase.database()


# default restaurants
restaurantA = {
        "name": "Restaurant A",
        "location": "location coordinates",
        "city" : "London",
        "menu" : ["peperroni pizza", "hotdog", "burger", "soup"],
        "ratings": ["5"],
        "allergens" : {"cereals" : ["hotdog", "burger", "peperroni pizza"], "soybeans" : ["soup"]}
    }

restaurantB = {
        "name": "Restaurant B",
        "location": "location coordinates",
        "city" : "London",
        "menu": ["salad", "sandwich"],
        "ratings": ["4"],
        "allergens" : {"celery" : ["salad"], "cereals" : ["sandwich"], "sesame" : ["salad"]}
    }

restaurantC = {
        "name": "Restaurant C",
        "location": "location coordinates",
        "city" : "London",
        "menu": ["fries", "burger", "garlic bread"],
        "ratings": ["3"],
        "allergens" : {"cereals" : ["burger", "garlic bread"], "sesame" : ["fries"]}
    }



def add_user(data):
    db.child("user").push(data)


def add_restaurant(data):
    db.child("restaurant").push(data)


def get_values(ref, limit=10):
    res = []
    for record in ref.get().each():
        res.append(record.val())
    return res


def delete_values(ref):
    for record in ref.get().each():
        key = record.key()
        ref.child(key).remove()


@app.route('/')
def index():
    return app.send_static_file('index.html')

@app.errorhandler(404)
def not_found(e):
    return app.send_static_file('index.html')
    

@app.route('/getRestaurantData', methods=["GET"])
@cross_origin()
def get_restaurant():
    return json.dumps(get_values(db.child("restaurant")))

@app.route('/collectData', methods=["GET"])
def foo():
    return db.child("user").get().val()
    
@app.route('/data')
def example():
    add_user({"firstName": "Brett", "lastName": "Conway", "Age": 20})
    add_user({"firstName": "Brett", "lastName": "Conroute", "Age": 20})
    add_user({"firstName": "Brett", "lastName": "Connection", "Age": 20})
    return json.dumps(get_values(db.child("user")))

if __name__ == '__main__':
    app.run(debug=True)

