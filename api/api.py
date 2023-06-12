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

chopstix = {
    "name": "Chopstix",
    "location": "location coordinates", 
    "city": "London",
    "menu": ["Egg Fried Rice", "Seasoned Rice", "Vegetable Noodles" ,"Skinny Rice", "Red Thai Chicken Curry", "Chinese Chicken Curry", "Massaman Chicken Curry", "Teriyaki Beef", "Plant Based Beef Stirfry TRIAL", "Pumpkin Katsu Curry", "Salt & Pepper Potatoes", "Mini Vegetable Spring Rolls", "Churros Sticks (without sauce)", "Wedges & Curry Sauce", "Noodle Bowl with Spring Rolls & Katsu Sauce", "Caramel Drizzle Chicken", "Salt 'n' Pepper Chicken", "Sweet & Sour Chicken", "BBQ Chicken", "Lemon Chicken TRIAL", "Katsu Chicken Curry", "Sweet Chilli Prawns", "Salt N Pepper Spicy Wings", "Prawn Crackers", "Duck Spring Rolls", "Chicken Balls - large & mini", "Noodle Bowl with Spicy Chicken Wings & Katsu Sauce", "Sweet Chilli Sauce POT", "Katsu Sauce", "Chocolate Sauce (Churros)", "Caramel Sauce (Churros)"], 
    "ratings": ["3.6"],
    "allergens": {
        "celery": ["Red Thai Chicken Curry", "Plant Based Beef Stirfry TRIAL", "Pumpkin Katsu Curry", "Plant Based Beef Stirfry TRIAL", "Pumpkin Katsu Curry", "Salt & Pepper Potatoes", "Mini Vegetable Spring Rolls", "Churros Sticks (without sauce)", "Wedges & Curry Sauce", "Noodle Bowl with Spring Rolls & Katsu Sauce", "Caramel Drizzle Chicken", "Salt 'n' Pepper Chicken", "Sweet & Sour Chicken", "BBQ Chicken", "Lemon Chicken TRIAL", "Katsu Chicken Curry", "Sweet Chilli Prawns", "Salt N Pepper Spicy Wings", "Prawn Crackers", "Duck Spring Rolls", "Chicken Balls - large & mini", "Noodle Bowl with Spicy Chicken Wings & Katsu Sauce"], 
        "cereals": ["Egg Fried Rice", "Seasoned Rice", "Vegetable Noodles" ,"Skinny Rice", "Red Thai Chicken Curry", "Chinese Chicken Curry", "Massaman Chicken Curry", "Teriyaki Beef", "Plant Based Beef Stirfry TRIAL", "Pumpkin Katsu Curry", "Salt & Pepper Potatoes", "Mini Vegetable Spring Rolls", "Churros Sticks (without sauce)", "Wedges & Curry Sauce", "Noodle Bowl with Spring Rolls & Katsu Sauce", "Caramel Drizzle Chicken", "Salt 'n' Pepper Chicken", "Sweet & Sour Chicken", "BBQ Chicken", "Lemon Chicken TRIAL", "Katsu Chicken Curry", "Sweet Chilli Prawns", "Salt N Pepper Spicy Wings", "Prawn Crackers", "Duck Spring Rolls", "Chicken Balls - large & mini", "Noodle Bowl with Spicy Chicken Wings & Katsu Sauce", "Katsu Sauce"],
        "crustaceans": ["Massaman Chicken Curry", "Teriyaki Beef", "Pumpkin Katsu Curry", "Salt & Pepper Potatoes", "Mini Vegetable Spring Rolls", "Churros Sticks (without sauce)", "Wedges & Curry Sauce", "Noodle Bowl with Spring Rolls & Katsu Sauce", "Caramel Drizzle Chicken", "Salt 'n' Pepper Chicken", "Sweet & Sour Chicken", "BBQ Chicken", "Lemon Chicken TRIAL", "Katsu Chicken Curry", "Sweet Chilli Prawns", "Salt N Pepper Spicy Wings", "Prawn Crackers", "Duck Spring Rolls", "Chicken Balls - large & mini", "Noodle Bowl with Spicy Chicken Wings & Katsu Sauce"],
        "eggs": ["Egg Fried Rice", "Vegetable Noodles", "Pumpkin Katsu Curry", "Salt & Pepper Potatoes", "Mini Vegetable Spring Rolls", "Churros Sticks (without sauce)", "Wedges & Curry Sauce", "Noodle Bowl with Spring Rolls & Katsu Sauce", "Caramel Drizzle Chicken", "Salt 'n' Pepper Chicken", "Sweet & Sour Chicken", "BBQ Chicken", "Lemon Chicken TRIAL", "Katsu Chicken Curry", "Sweet Chilli Prawns", "Salt N Pepper Spicy Wings", "Prawn Crackers", "Duck Spring Rolls", "Chicken Balls - large & mini", "Noodle Bowl with Spicy Chicken Wings & Katsu Sauce"], 
        "fish": ["Massaman Chicken Curry", "Pumpkin Katsu Curry", "Salt & Pepper Potatoes", "Mini Vegetable Spring Rolls", "Churros Sticks (without sauce)", "Wedges & Curry Sauce", "Noodle Bowl with Spring Rolls & Katsu Sauce", "Caramel Drizzle Chicken", "Salt 'n' Pepper Chicken", "Sweet & Sour Chicken", "BBQ Chicken", "Lemon Chicken TRIAL", "Katsu Chicken Curry", "Sweet Chilli Prawns", "Salt N Pepper Spicy Wings", "Prawn Crackers", "Duck Spring Rolls", "Chicken Balls - large & mini", "Noodle Bowl with Spicy Chicken Wings & Katsu Sauce"], 
        "lupin": [], 
        "milk": ["Vegetable Noodles", "Plant Based Beef Stirfry TRIAL", "Pumpkin Katsu Curry", "Salt & Pepper Potatoes", "Mini Vegetable Spring Rolls", "Churros Sticks (without sauce)", "Wedges & Curry Sauce", "Noodle Bowl with Spring Rolls & Katsu Sauce", "Caramel Drizzle Chicken", "Salt 'n' Pepper Chicken", "Sweet & Sour Chicken", "BBQ Chicken", "Lemon Chicken TRIAL", "Katsu Chicken Curry", "Sweet Chilli Prawns", "Salt N Pepper Spicy Wings", "Prawn Crackers", "Duck Spring Rolls", "Chicken Balls - large & mini", "Noodle Bowl with Spicy Chicken Wings & Katsu Sauce", "Caramel Sauce"], 
        "molluscs": ["Pumpkin Katsu Curry", "Salt & Pepper Potatoes", "Mini Vegetable Spring Rolls", "Churros Sticks (without sauce)", "Wedges & Curry Sauce", "Noodle Bowl with Spring Rolls & Katsu Sauce", "Caramel Drizzle Chicken", "Salt 'n' Pepper Chicken", "Sweet & Sour Chicken", "BBQ Chicken", "Lemon Chicken TRIAL", "Katsu Chicken Curry", "Sweet Chilli Prawns", "Salt N Pepper Spicy Wings", "Prawn Crackers", "Duck Spring Rolls", "Chicken Balls - large & mini", "Noodle Bowl with Spicy Chicken Wings & Katsu Sauce"], 
        "mustard": ["Red Thai Chicken Curry", "Chinese Chicken Curry", "Massaman Chicken Curry", "Plant Based Beef Stirfry TRIAL", "Pumpkin Katsu Curry", "Salt & Pepper Potatoes", "Mini Vegetable Spring Rolls", "Churros Sticks (without sauce)", "Wedges & Curry Sauce", "Noodle Bowl with Spring Rolls & Katsu Sauce", "Caramel Drizzle Chicken", "Salt 'n' Pepper Chicken", "Sweet & Sour Chicken", "BBQ Chicken", "Lemon Chicken TRIAL", "Katsu Chicken Curry", "Sweet Chilli Prawns", "Salt N Pepper Spicy Wings", "Prawn Crackers", "Duck Spring Rolls", "Chicken Balls - large & mini", "Noodle Bowl with Spicy Chicken Wings & Katsu Sauce", "Katsu Sauce"], 
        "nuts": ["Pumpkin Katsu Curry", "Salt & Pepper Potatoes", "Mini Vegetable Spring Rolls", "Churros Sticks (without sauce)", "Wedges & Curry Sauce", "Noodle Bowl with Spring Rolls & Katsu Sauce", "Caramel Drizzle Chicken", "Salt 'n' Pepper Chicken", "Sweet & Sour Chicken", "BBQ Chicken", "Lemon Chicken TRIAL", "Katsu Chicken Curry", "Sweet Chilli Prawns", "Salt N Pepper Spicy Wings", "Prawn Crackers", "Duck Spring Rolls", "Chicken Balls - large & mini", "Noodle Bowl with Spicy Chicken Wings & Katsu Sauce"], 
        "peanuts": [], 
        "sesame seeds": ["Egg Fried Rice", "Vegetable Noodles", "Skinny Rice", "Teriyaki Beef", "Pumpkin Katsu Curry", "Salt & Pepper Potatoes", "Mini Vegetable Spring Rolls", "Churros Sticks (without sauce)", "Wedges & Curry Sauce", "Noodle Bowl with Spring Rolls & Katsu Sauce", "Caramel Drizzle Chicken", "Salt 'n' Pepper Chicken", "Sweet & Sour Chicken", "BBQ Chicken", "Lemon Chicken TRIAL", "Katsu Chicken Curry", "Sweet Chilli Prawns", "Salt N Pepper Spicy Wings", "Prawn Crackers", "Duck Spring Rolls", "Chicken Balls - large & mini", "Noodle Bowl with Spicy Chicken Wings & Katsu Sauce"], 
        "soya": ["Egg Fried Rice", "Seasoned Rice", "Vegetable Noodles" ,"Skinny Rice", "Red Thai Chicken Curry", "Chinese Chicken Curry", "Massaman Chicken Curry", "Teriyaki Beef", "Plant Based Beef Stirfry TRIAL", "Pumpkin Katsu Curry", "Salt & Pepper Potatoes", "Mini Vegetable Spring Rolls", "Churros Sticks (without sauce)", "Wedges & Curry Sauce", "Noodle Bowl with Spring Rolls & Katsu Sauce", "Caramel Drizzle Chicken", "Salt 'n' Pepper Chicken", "Sweet & Sour Chicken", "BBQ Chicken", "Lemon Chicken TRIAL", "Katsu Chicken Curry", "Sweet Chilli Prawns", "Salt N Pepper Spicy Wings", "Prawn Crackers", "Duck Spring Rolls", "Chicken Balls - large & mini", "Noodle Bowl with Spicy Chicken Wings & Katsu Sauce", "Chocolate Sauce (Churros)"],
        "sulphur dioxide": ["Teriyaki Beef", "Plant Based Beef Stirfry TRIAL", "Pumpkin Katsu Curry", "Plant Based Beef Stirfry TRIAL", "Pumpkin Katsu Curry", "Salt & Pepper Potatoes", "Mini Vegetable Spring Rolls", "Churros Sticks (without sauce)", "Wedges & Curry Sauce", "Noodle Bowl with Spring Rolls & Katsu Sauce", "Caramel Drizzle Chicken", "Salt 'n' Pepper Chicken", "Sweet & Sour Chicken", "BBQ Chicken", "Lemon Chicken TRIAL", "Katsu Chicken Curry", "Sweet Chilli Prawns", "Salt N Pepper Spicy Wings", "Prawn Crackers", "Duck Spring Rolls", "Chicken Balls - large & mini", "Noodle Bowl with Spicy Chicken Wings & Katsu Sauce"]
    }
}

def get_values(ref, limit=10):
    res = []
    for record in ref.get().each():
        res.append(record.val())
    return res


def delete_values(ref):
    for record in ref.get().each():
        key = record.key()
        ref.child(key).remove()
        
def get_users():
    res = []
    ref = db.child("user")
    print(ref)
    print(ref.get().val())
    #for user in db.child("user").get().val().each():
    #    res.append(user)
    return res


@app.route('/')
def index():
    return app.send_static_file('index.html')

@app.errorhandler(404)
def not_found(e):
    return app.send_static_file('index.html')
    

@app.route('/getRestaurantData', methods=["GET"])
def get_restaurant():
    return json.dumps(get_values(db.child("restaurant")))

@app.route('/getUserFriends', methods=["GET"])
def getUserFriends():
    return json.dumps(get_values(db.child("user")))

    
if __name__ == '__main__':
    app.run(debug=True)

