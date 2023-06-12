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

wasabi = {
    "name": "wasabi",
    "location": "location coordinates",
    "city": "London",
    "menu": [
        "Avocado hosomaki", "Cucumber hosomaki", "Salmon hosomaki", "Tuna hosomaki", "Inari & red pepper hosomaki",
        "California roll", "Fried prawn roll", "Salmon & mango roll", "Surumi crabmeat & cucumber roll", "Tofu roll", "Salmon teriyaki roll",
        "Japanese omelette nigiri", "Salmon nigiri", "Shrimp nigiri", "Tofu nigiri", "Tuna nigiri",
        "Salmon sesame gunkan", "Surumi crabmeat gunkan",
        "Chicken teriyaki onigiri", "Salmon teriyaki onigiri", "Seaweed onigiri", "Edamame & butternut squash onigiri", "Chicken katsu & kimchi onigiri", "Tuna & mustard onigiri",
        "Chumaki set", "Harmony set", "Mini hosomaki set", "Mixed maki set", "Rainbow set", "Salmon nigiri set", "Sashimi set", "Tokyo salmon set", "Mini Tokyo Salmon set", "Osaka set", 
        "Wasabi special bento", "Yasai roll set", "Salmon teriyaki roll set", "Crispy ebi roll", "Chicken katsu roll set", "Veggie roll set", "Tofu pocket roll set",
        "Salmon hosomaki set", "Avocado hosomaki set", "Cucumber hosomaki set", "Spicy salmon roll", "Spicy yasai roll", "Kyoto set",
        "Chumaki set - brown rice", "Salmon nigiri set - brown rice", "Rainbow set - brown rice", "Yasai roll set - brown rice", "Harmony set - brown rice",  
        "Chicken katsu salad", "Chirashi bowl", "Salmon teriyaki salad", "Tofu teriyaki salad",
        "Salmon Matsuri platter", "Tsudoi platter", "Yasai platter"
        ],
    "ratings": ["3.55"],
    "allergens": {
        "celery": [],
        "cereals": [],
        "crustaceans": ["California roll", "Fried prawn roll", "Surumi crabmeat & cucumber roll", "Shrimp nigiri", "Surumi crabmeat gunkan",
                        "Chicken katsu & kimchi onigiri", "Chumaki set", "Harmony set", "Mixed maki set", "Rainbow set", "Osaka set", "Crispy ebi roll",
                        "Wasabi special bento", "Kyoto set", "Chumaki set - brown rice", "Rainbow set - brown rice", "Harmony set - brown rice", "Chirashi bowl", 
                        "Tsudoi platter", ],
        "eggs": ["California roll", "Fried prawn roll", "Surumi crabmeat & cucumber roll", "Japanese omelette nigiri", "Surumi crabmeat gunkan",
                 "Tuna & mustard onigiri", "Chumaki set", "Harmony set", "Mixed maki set", "Rainbow set", "Osaka set", "Crispy ebi roll", "Wasabi special bento", 
                 "Kyoto set", "Chumaki set - brown rice", "Rainbow set - brown rice", "Harmony set - brown rice", "Chicken katsu salad", "Chirashi bowl",
                 "Tsudoi platter", ],
        "fish": ["Salmon hosomaki", "Tuna hosomaki","California roll", "Salmon & mango roll", "Surumi crabmeat & cucumber roll", "Salmon teriyaki roll",
                 "Salmon nigiri", "Tuna nigiri", "Salmon sesame gunkan", "Surumi crabmeat gunkan", "Tuna & mustard onigiri", "Chicken katsu & kimchi onigiri",
                 "Salmon teriyaki onigiri",
                 "Chumaki set", "Harmony set", "Mini hosomaki set", "Mixed maki set", "Rainbow set", "Salmon nigiri set", "Sashimi set", "Tokyo salmon set", "Mini Tokyo Salmon set", "Osaka set",
                 "Salmon hosomaki set", "Salmon teriyaki roll set", "Wasabi special bento", "Spicy salmon roll", "Kyoto set", 
                 "Chumaki set - brown rice", "Salmon nigiri set - brown rice", "Rainbow set - brown rice", "Harmony set - brown rice", "Chirashi bowl", "Salmon teriyaki salad", 
                 "Salmon Matsuri platter", "Tsudoi platter", ],
        "lupin": [], 
        "milk": ["Fried prawn roll", "Chumaki set", "Harmony set", "Mixed maki set", "Rainbow set", "Crispy ebi roll", "Chumaki set - brown rice", "Rainbow set - brown rice", 
                 "Harmony set - brown rice", "Tsudoi platter", ],
        "molluscs": [],
        "mustard": ["Surumi crabmeat gunkan", "Tuna & mustard onigiri",
                    "Chumaki set", "Harmony set", "Mini hosomaki set", "Mixed maki set", "Rainbow set", "Salmon nigiri set", "Sashimi set", "Tokyo salmon set", "Mini Tokyo Salmon set", "Osaka set",
                    "Wasabi special bento", "Yasai roll set", "Salmon teriyaki roll set", "Crispy ebi roll", "Chicken katsu roll set", "Veggie roll set", "Tofu pocket roll set",
                    "Salmon hosomaki set", "Avocado hosomaki set", "Cucumber hosomaki set", "Spicy salmon roll", "Spicy yasai roll", "Kyoto set", 
                    "Chumaki set - brown rice", "Salmon nigiri set - brown rice", "Rainbow set - brown rice", "Yasai roll set - brown rice", "Harmony set - brown rice", 
                    "Chirashi bowl", "Salmon teriyaki salad", "Tofu teriyaki salad", "Salmon Matsuri platter", "Tsudoi platter", "Yasai platter"],
        "nuts": [],
        "peanuts": [], 
        "sesame seeds": ["California roll", "Fried prawn roll", "Salmon teriyaki roll", "Salmon sesame gunkan", "Chicken katsu & kimchi onigiri",
                         "Seaweed onigiri", "Salmon teriyaki onigiri", "Chicken teriyaki onigiri", "Chumaki set", "Harmony set", "Mini hosomaki set", 
                         "Mixed maki set", "Rainbow set", "Salmon nigiri set", "Sashimi set", "Osaka set", "Chicken katsu roll set", "Crispy ebi roll",
                         "Salmon teriyaki roll set", "Yasai roll set", "Spicy salmon roll",
                         "Chumaki set - brown rice", "Salmon nigiri set - brown rice", "Rainbow set - brown rice", "Yasai roll set - brown rice", "Harmony set - brown rice", 
                         "Chicken katsu salad", "Chirashi bowl", "Salmon teriyaki salad", "Tofu teriyaki salad", "Tsudoi platter", "Yasai platter"],
        "soya": ["Inari & red pepper hosomaki", "California roll", "Fried prawn roll", "Salmon & mango roll", "Surumi crabmeat & cucumber roll",
                 "Tofu roll", "Salmon teriyaki roll", "Tofu nigiri", "Salmon sesame gunkan", "Surumi crabmeat gunkan", "Chicken katsu & kimchi onigiri",
                 "Edamame & butternut squash onigiri", "Seaweed onigiri", "Salmon teriyaki onigiri", "Chicken teriyaki onigiri",
                 "Chumaki set", "Harmony set", "Mini hosomaki set", "Mixed maki set", "Rainbow set", "Salmon nigiri set", "Sashimi set", "Tokyo salmon set", "Mini Tokyo Salmon set", "Osaka set",
                 "Wasabi special bento", "Yasai roll set", "Salmon teriyaki roll set", "Crispy ebi roll", "Chicken katsu roll set", "Veggie roll set", "Tofu pocket roll set",
                 "Salmon hosomaki set", "Avocado hosomaki set", "Cucumber hosomaki set", "Spicy salmon roll", "Spicy yasai roll", "Kyoto set", 
                 "Chumaki set - brown rice", "Salmon nigiri set - brown rice", "Rainbow set - brown rice", "Yasai roll set - brown rice", "Harmony set - brown rice", 
                 "Chicken katsu salad", "Chirashi bowl", "Salmon teriyaki salad", "Tofu teriyaki salad", "Salmon Matsuri platter", "Tsudoi platter", "Yasai platter"
                 ],
        "sulphur dioxide": ["Surumi crabmeat & cucumber roll", "Surumi crabmeat gunkan", "Chicken katsu & kimchi onigiri", "Chicken teriyaki onigiri", 
                            "Chumaki set", "Harmony set", "Mixed maki set", "Rainbow set", "Osaka set", "Wasabi special bento", "Spicy yasai roll", "Kyoto set", 
                            "Chumaki set - brown rice", "Rainbow set - brown rice", "Harmony set - brown rice", "Chirashi bowl", ],
    }
}

fiveGuys = {
    "name": "Five Guys",
    "location": "location coordinates",
    "city": "London",
    "menu": ["Hamburger", "Cheeseburger", "Bacon Burger", "Bacon Cheeseburger", "Little Hamburger", "Little Cheeseburger", "Little Bacon Burger", "Little Bacon Cheeseburger",
             "All Beef Hot Dog", "Cheese Dog", "Bacon Dog", "Bacon Cheese Dog", "Veggie Sandwich", "Cheese Veggie Sandwich", "Grilled Cheese", "BLT", "Little Five Guys Style Fries",
             "Regular Five Guys Style Fries", "Large Five Guys Style Fries", "Little Cajun Style Fries", "Regular Cajun Style Fries", "Large Cajun Style Fries", "Five Guys Shake", "Reese's Peanut Butter Cups Shake", "Coca-Cola Original Taste",
             "Diet Coke", "Coca-Cola Zero Sugar", "Sprite", "Fanta Orange", "Dr Pepper", "Glaceau Smart Water", "Budweiser", "Corona", "Brooklyn Beer"],
    "ratings": ["4.80"],
    "allergens": {
        "celery": ["Little Five Guys Style Fries", "Regular Five Guys Style Fries", "Large Five Guys Style Fries", "Little Cajun Style Fries", "Regular Cajun Style Fries", "Large Cajun Style Fries"],
        "cereals": ["Hamburger", "Cheeseburger", "Bacon Burger", "Bacon Cheeseburger", "Little Hamburger", "Little Cheeseburger", "Little Bacon Burger", "Little Bacon Cheeseburger",
                    "All Beef Hot Dog", "Cheese Dog", "Bacon Dog", "Bacon Cheese Dog", "Veggie Sandwich", "Cheese Veggie Sandwich", "Grilled Cheese", "BLT"],
        "crustaceans": [],
        "eggs": ["Hamburger", "Cheeseburger", "Bacon Burger", "Bacon Cheeseburger", "Little Hamburger", "Little Cheeseburger", "Little Bacon Burger", "Little Bacon Cheeseburger",
             "All Beef Hot Dog", "Cheese Dog", "Bacon Dog", "Bacon Cheese Dog"],
        "fish": [],
        "lupin": [], 
        "milk": ["Hamburger", "Cheeseburger", "Bacon Burger", "Bacon Cheeseburger", "Little Hamburger", "Little Cheeseburger", "Little Bacon Burger", "Little Bacon Cheeseburger",
                 "All Beef Hot Dog", "Cheese Dog", "Bacon Dog", "Bacon Cheese Dog", "Five Guys Shake", "Reese's Peanut Butter Cups Shake"],
        "molluscs": [],
        "mustard": [],
        "nuts": ["Hamburger", "Cheeseburger", "Bacon Burger", "Bacon Cheeseburger", "Little Hamburger", "Little Cheeseburger", "Little Bacon Burger", "Little Bacon Cheeseburger", 
                 "All Beef Hot Dog", "Cheese Dog", "Bacon Dog", "Bacon Cheese Dog", "Reese's Peanut Butter Cups Shake"],
        "peanuts": ["Little Five Guys Style Fries", "Regular Five Guys Style Fries", "Large Five Guys Style Fries",
                    "Little Cajun Style Fries", "Regular Cajun Style Fries", "Large Cajun Style Fries", "Five Guys Shake", "Reese's Peanut Butter Cups Shake"], 
        "sesame seeds": ["Hamburger", "Cheeseburger", "Bacon Burger", "Bacon Cheeseburger", "Little Hamburger", "Little Cheeseburger", "Little Bacon Burger", "Little Bacon Cheeseburger", 
                         "All Beef Hot Dog", "Cheese Dog", "Bacon Dog", "Bacon Cheese Dog", "Reese's Peanut Butter Cups Shake"],
        "soya": ["Hamburger", "Cheeseburger", "Bacon Burger", "Bacon Cheeseburger", "Little Hamburger", "Little Cheeseburger", "Little Bacon Burger", "Little Bacon Cheeseburger", 
                 "All Beef Hot Dog", "Cheese Dog", "Bacon Dog", "Bacon Cheese Dog", "Five Guys Shake", "Reese's Peanut Butter Cups Shake"],
        "sulphur dioxide": [],
    }
}

default = {
    "name": "",
    "location": "location coordinates",
    "city": "London",
    "menu": [],
    "ratings": ["4.20"],
    "allergens": {
        "celery": [],
        "cereals": [],
        "crustaceans": [],
        "eggs": [],
        "fish": [],
        "lupin": [], 
        "milk": [],
        "molluscs": [],
        "mustard": [],
        "nuts": [],
        "peanuts": [], 
        "sesame seeds": [],
        "soya": [],
        "sulphur dioxide": [],
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

