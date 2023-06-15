from pyrebase import pyrebase
from flask import Flask, Response, request, session
from flask_cors import CORS
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
auth = firebase.auth()

app.secret_key = "secretive"

# default restaurants
restaurantA = {
        "name": "Restaurant A",
        "location": "location coordinates",
        "city" : "London",
        "menu" : ["peperroni pizza", "hotdog", "burger", "soup"],
        "ratings": ["5"],
        "allergens" : {"cereals" : ["hotdog", "burger", "peperroni pizza"], "soybeans" : ["soup"]},
        "tags" : ["Pizza", "American"]
    }

restaurantB = {
        "name": "Restaurant B",
        "location": "location coordinates",
        "city" : "London",
        "menu": ["salad", "sandwich"],
        "ratings": ["4"],
        "allergens" : {"celery" : ["salad"], "cereals" : ["sandwich"], "sesame" : ["salad"]},
        "tags" : ["Greek", "American"]
    }

restaurantC = {
        "name": "Restaurant C",
        "location": "location coordinates",
        "city" : "London",
        "menu": ["fries", "burger", "garlic bread"],
        "ratings": ["3"],
        "allergens" : {"cereals" : ["burger", "garlic bread"], "sesame" : ["fries"]},
        "tags" : ["Burgers", "American"]
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
    },
    "tags" : ["Japanese"]
}

thai_square = {
    "name": "Thai Square",
    "location": "location coordinates", 
    "city": "London",
    "menu": [
        "Prawn Crackers", "Thai Square Mixed Starters (for 2 people)", "Aromatic Duck (for 2 people)", "Thai Dumplings", "Chicken Satay", "Salt and Pepper Squid", "Butterfly Prawns", "Duck Spring Rolls",
        "Spicy Prawn Soup (Tom Yum Goong)", "Chicken in Coconut Soup (Tom Kha Gai)", "Papaya Salad", "Minced Chicken Salad",
        "Stir Fried with Basil Leaves", "Stir Fried with Cashew Nuts", "Sweet and Sour", "Stir Fried with Oyster Sauce", "Stir Fried with Ginger", "Chilli Lamb", "Drunken Duck", 
        "Tamarind Duck", "Weeping Tiger", "Grilled Pork Neck (Kor Moo Yang)",
        "Lamb Shank Panang Curry", "Green Curry", "Red Curry", "Panang Curry", "Jungle Curry", "Massaman Curry", "Duck Curry", "Golden Curry",
        "Chu Chi Jumbo Prawns", "Steamed Sea Bass", "Crispy Tilapia", "Spicy Seafood", "Garlic Prawns", "Prawns Love Scallops", 
        "Pad Thai", "Pad Si-ew", "Drunken Noodles", "Thai Square Fried Rice",
        "Steamed Thai Jasmine Rice", "Brown Rice", "Egg Fried Rice", "Sticky Rice", "Coconut Rice", "Thai Square Noodles", "Mixed Vegetables with Garlic Sauce", "Broccoli with Garlic and Soya Sauce", 
        "Mixed Vegetarian Starter (for 2 people)", "Vegetable Spring Rolls", "Corn Cakes", "Vegetable Tempura", "Vegetable and Tofu Satay", "Salt and Pepper Tofu", "Papaya Salad (Som Tum Jay)", "Mushroom in Coconut Soup (Tom Kha Hed)",
        "Tofu with Basil Leaves", "Vegetable Green Curry", "Vegetable Jungle Curry", "Sweet and Sour Tofu", "Tofu with Cashew Nuts", "Tofu with Ginger", "Spicy Aubergine", "Vegetarian Pad Thai"
    ],
    "ratings": ["3.6"], 
    "allergens": {
        "celery": ["Sweet and Sour", "Pad Thai", "Sweet and Sour Tofu", "Vegetarian Pad Thai"],
        "cereals": ["Thai Square Mixed Starters (for 2 people)", "Aromatic Duck (for 2 people)", "Thai Dumplings", "Salt and Pepper Squid", "Butterfly Prawns", "Duck Spring Rolls", "Stir Fried with Basil Leaves", "Stir Fried with Cashew Nuts", "Stir Fried with Oyster Sauce", "Stir Fried with Ginger", "Chilli Lamb", "Drunken Duck", "Tamarind Duck", "Weeping Tiger", "Grilled Pork Neck (Kor Moo Yang)", "Crispy Tilapia", "Spicy Seafood", "Garlic Prawns", "Prawns Love Scallops", "Pad Si-ew", "Drunken Noodles", "Thai Square Fried Rice", "Thai Square Noodles", "Mixed Vegetables with Garlic Sauce", "Broccoli with Garlic and Soya Sauce", "Mixed Vegetarian Starter (for 2 people)", "Vegetable Spring Rolls", "Corn Cakes", "Vegetable Tempura", "Sald and Pepper Tofu", "Papaya Salad (Som Tum Jay)", "Tofu with Basil Leaves", "Vegetable Jungle Curry", "Tofu with Cashew Nuts", "Tofu with Ginger", "Spicy Aubergine"],
        "crustaceans": ["Prawn Crackers", "Thai Square Mixed Starters (for 2 people)", "Thai Dumplings", "Butterfly Prawns", "Spicy Prawn Soup (Tom Yum Goong)", "Chicken in Coconut Soup (Tom Kha Gai)", "Chilli Lamb", "Lamb Shank Panang Curry", "Green Curry", "Red Curry", "Panang Curry", "Jungle Curry", "Massaman Curry", "Duck Curry", "Golden Curry", "Chu Chi Jumbo Prawns", "Spicy Seafood", "Garlic Prawns", "Prawns Love Scallops", "Thai Square Fried Rice"],
        "eggs": ["Thai Square Mixed Starters (for 2 people)", "Thai Dumplings", "Salt and Pepper Squid", "Butterfly Prawns", "Spicy Seafood", "Pad Thai", "Pad Si-ew", "Thai Square Fried Rice", "Egg Fried Rice", "Thai Square Noodles", "Vegetarian Pad Thai"],
        "fish": ["Spicy Prawn Soup (Tom Yum Goong)", "Chicken in Coconut Soup (Tom Kha Gai)", "Papaya Salad (Som Tum)", "Minced Chicken Salad (Laab Gai)", "Tamarind Duck", "Weeping Tiger", "Grilled Pork Neck (Kor Moo Yang)", "Lamb Shank Panang Curry", "Green Curry", "Red Curry", "Panang Curry", "Jungle Curry", "Massaman Curry", "Duck Curry", "Golden Curry", "Chu Chi Jumbo Prawns", "Steamed Sea Bass", "Crispy Tilapia", "Spicy Seafood", "Pad Thai"],
        "lupin": [], 
        "milk": ["Thai Square Mixed Starters (for 2 people)", "Duck Spring Rolls", "Spicy Prawn Soup (Tom Yum Goong)", "Mixed Vegetarian Starter (for 2 people)", "Vegetable Spring Rolls"],
        "molluscs": ["Salt and Pepper Squid", "Stir Fried with Basil Leaves", "Stir Fried with Cashew Nuts", "Stir Fried with Oyster Sauce", "Stir Fried with Ginger", "Chilli Lamb", "Drunken Duck", "Weeping Tiger", "Grilled Pork Neck (Kor Moo Yang)", "Spicy Seafood", "Garlic Prawns", "Prawns Love Scallops", "Pad Si-ew", "Drunken Noodles", "Thai Square Fried Rice"],
        "mustard": ["Thai Square Mixed Starters (for 2 people)", "Chicken Satay"],
        "nuts": ["Papaya Salad (Som Tum)", "Stir Fried with Cashew Nuts", "Pad Thai", "Papaya Salad (Som Tum Jay)", "Tofu with Cashew Nuts", "Vegetarian Pad Thai"],
        "peanuts": ["Thai Square Mixed Starters (for 2 people)", "Chicken Satay", "Pad Thai", "Mixed Vegetarian Starter (for 2 people)", "Vegetable and Tofu Satay", "Papaya Salad (Som Tum Jay)", "Vegetarian Pad Thai"], 
        "sesame seeds": ["Thai Square Mixed Starters (for 2 people)", "Aromatic Duck (for 2 people)", "Thai Dumplings", "Duck Spring Rolls", "Stir Fried with Cashew Nuts", "Thai Square Noodles", "Mixed Vegetarian Starter (for 2 people)", "Vegetable Spring Rolls", "Tofu with Cashew Nuts"],
        "soya": ["Thai Square Mixed Starters (for 2 people)", "Aromatic Duck (for 2 people)", "Thai Dumplings", "Butterfly Prawns", "Duck Spring Rolls", "Stir Fried with Basil Leaves", "Stir Fried with Cashew Nuts", "Stir Fried with Oyster Sauce", "Stir Fried with Ginger", "Chilli Lamb", "Drunken Duck", "Tamarind Duck", "Weeping Tiger", "Grilled Pork Neck (Kor Moo Yang)", "Spicy Seafood", "Garlic Prawns", "Prawns Love Scallops", "Pad Thai", "Pad Si-ew", "Drunken Noodles", "Thai Square Fried Rice", "Thai Square Noodles", "Mixed Vegetables with Garlic Sauce", "Broccoli with Garlic and Soya Sauce", "Mixed Vegetarian Starter (for 2 people)", "Vegetable Spring Rolls", "Vegetable and Tofu Satay", "Salt and Pepper Tofu", "Papaya Salad (Som Tum Jay)", "Tofu with Basil Leaves", "Vegetable Green Curry", "Vegetable Jungle Curry", "Sweet and Sour Tofu", "Tofu with Cashew Nuts", "Tofu with Ginger", "Spicy Aubergine", "Vegetarian Pad Thai"],
        "sulphur dioxide": [],
    },
    "tags" : ["Thai"]
}

comptoir_libanais = {
    "name": "Comptoir Libanais",
    "location": "location coordinates",
    "city": "London",
    "menu": [
        "Selection of Pickes", "Marinated Mixed Olives", "Warm Za'atar & Garlic Flatbread",
        "Mezze Platter", "Lentil Soup", "Hommos", "Tony's Hommos", "Baba Ghanuj", "Batata Harra", "Cheese Samboussek", "Falafel", "Halloumi & Tomato", "Lamb Kibbeh", "Tabbouleh", "Fattoush", "Whipped Feta Dip", "Halloumi & Roasted Figs", 
        "Mama Zohra Salad", "Falafel Salad", "The Wedge Salad", "Summer Salad", 
        "Chicken Wrap", "Falafel Wrap", "Lamb Kofta Wrap", "Chicken Taouk Plate", "Lamb Kofta Plate", "Falafel Plate", "Vanilla Ice-cream",
        "Chocolate Brownie", "Mango & Vanilla Cheesecake", "Orange Blossom Mouhalabia", "Baklawa Sandwich", "Comptoir Sundae",
        "Hadath", "Bokaj", "Pistachio", "Assabee", "Kolwashkur", 
        "Falafel", "Lamb Kofta", "Chicken Taouk", "Halloumi", 
        "Spiced Lamb Kofta", "Spced Chicken Kofta", "Marinated Chicken Taouk",
        "Mixed Grill", "Sea Bass Sayadiyah", "Lamb Kofta Roll", "Steak Skewer", "Spinach & Feta Borek",
        "Aubergine & Chickpea Tagine", "Lamb Kofta Tagine", "Chicken & Green Olive Tagine", 
        "Warm Flatbread", "Vermicelli Rice", "Steamed Couscous", "Jewelled Couscous", "Quinoa", "Garlic Sauce", "Mint Yoghurt Sauce", "Tahina Sauce", "Harissa Sauce", "Fries", 
        "Teas with Cow Milk", "Teas with Soya Milk", "Teas with Almond", "Hot Chocolate with Cow Milk", "Hot Chocolate with Soya Milk", "Hot Chocolate with Almond Milk", "Americano with Cow Milk", "Americano with Soya Milk", "Americano with Almond Milk", "Cappuccino with Cow Milk", "Cappuccino with Soya Milk", "Cappuccino with Almond Milk", "Latte with Cow Milk", "Latte with Soya Milk", "Latte with Almond Milk", "Flat White with Cow Milk", "Flat White with Soya Milk", "Flat White with Almond Milk", "Mocha with Cow Milk", "Mocha with Soya Milk", "Mocha with Almond Milk", "Espresso with Cow Milk", "Espresso with Soya Milk", "Espresson with Almond Milk", "Macchiato with Cow Milk", "Macchiato with Soya Milk", "Macchiato with Almond Milk", "Lebanese Coffee with Cow Milk", "Lebanese Coffee with Soya Milk", "Lebanese Coffee with Almond Milk", "Lebanese Spiced Hot Chocolate with Cow Milk", "Lebanese Spiced Hot Chocolate with Soya Milk", "Lebanese Spiced Hot Chocolate with Almond Milk"
    ],
    "ratings": ["4.0"],
    "allergens": {
        "celery": [],
        "cereals": ["Warm Za'atar & Garlic Flatbread", "Mezze Platter", "Lentil Soup", "Hommos", "Tony's Hommos", "Baba Ghanuj", "Batata Harra", "Cheese Samboussek", "Falafel", "Lamb Kibbeh", "Fattoush", "Whipped Feta Dip", "Mama Zohra Salad", "Falafel Salad", "The Wedge Salad", "Chicken Wrap", "Falafel Wrap", "Lamb Kofta Wrap", "Chicken Taouk Plate", "Lamb Kofta Plate", "Falafel Plate", "Vanilla Ice-cream", "Chocolate Brownie", "Mango & Vanilla Cheesecake", "Baklawa Sandwich", "Comptoir Sundae", "Hadath", "Bokaj", "Pistachio", "Assabee", "Kolwashkur", "Falafel", "Lamb Kofta", "Chicken Taouk", "Halloumi", "Sea Bass Sayadiyah", "Lamb Kofta Roll", "Steak Skewer", "Spinach & Feta Borek", "Aubergine & Chickpea Tagine", "Lamb Kofta Tagine", "Chicken & Green Olive Tagine", "Warm Flatbrread", "Vermicelli Rice", "Steamed Couscous", "Jewelled Couscous", "Fries"],
        "crustaceans": [],
        "eggs": ["Mezze Platter", "Tony's Hommos", "Batata Harra", "Cheese Samboussek", "Falafel", "Lamb Kibbeh", "Falafel Salad", "Chicken Wrap", "Falafel Wrap", "Lamb Kofta Wrap", "Chicken Taouk Plate", "Lamb Kofta Plate", "Falafel Plate", "Vanilla Ice-cream", "Chocolate Brownie", "Baklawa Sandwich", "Comptoir Sundae", "Falafel", "Sea Bass Sayadiyah", "Lamb Kofta Roll", "Steak Skewer", "Spinach & Feta Borek", "Jewelled Couscous", "Fries"],
        "fish": ["Sea Bass Sayadiyah"],
        "lupin": ["Warm Za'atar & Garlic Flatbread", "Mezze Platter", "Lentil Soup", "Hommos", "Tony's Hommos", "Baba Ghanuj", "Whipped Feta Dip", "Warm Flatbread"],
        "milk": ["Mezze Platter", "Tony's Hommos", "Batata Harra", "Cheese Samboussek", "Falafel", "Halloumi & Tomato", "Lamb Kibbeh", "Whipped Feta Dip", "Halloumi & Roasted Figs", "Mama Zohra Salad", "Falafel Salad", "Summer Salad", "Chicken Wrap", "Falafel Wrap", "Lamb Kofta Wrap", "Chicken Taouk Plate", "Lamb Kofta Plate", "Falafel Plate", "Vanilla Ice-cream", "Chocolate Brownie", "Mango & Vanilla Cheesecake", "Orange Blossom Mouhalabia", "Baklawa Sandwich", "Comptoir Sundae", "Hadath", "Bokaj", "Pistachio", "Assabee", "Kolwashkur", "Falafel", "Halloumi", "Sea Bass Sayadiyah", "Lamb Kofta Roll", "Steak Skewer", "Spinach & Feta Borek", "Lamb Kofta Tagine", "Jewelled Couscous", "Mint Yoghurt Sauce", "Fries", "Teas with Cow Milk", "Hot Chocolate with Cow Milk", "Americano with Cow Milk", "Cappuccino with Cow Milk", "Latte with Cow Milk", "Flat White with Cow Milk", "Mocha with Cow Milk", "Expresso with Cow Milk", "Macchiato with Cow Milk", "Lebanese Coffee with Cow Milk", "Lebanese Spiced Hot Chocolate with Cow Milk"],
        "molluscs": [],
        "mustard": ["Warm Za'atar & Garlic Flatboard", "Mezze Platter", "Lentil Soup", "Hommos", "Tony's Hommos", "Baba Ghanuj", "Whipped Feta Dip", "Warm Flatbread"],
        "nuts": ["Halloumi & Roasted Figs", "Summer Salad", "Chocolate Brownie", "Mango & Vanilla Cheesecake", "Baklawa Sandwich", "Comptoir Sundae", "Hadath", "Bokaj", "Pistachio", "Assabee", "Kolwashkur", "Teas with Almond", "Hot Chocolate with Almond Milk", "Americano with Almond Milk", "Cappuccino with Almond Milk", "Latte with Almond Milk", "Flat White with Almond Milk", "Mocha with Almond Milk", "Espresso with Almond Milk", "Macchiato with Almond Milk", "Lebanese Coffee with Almond Milk", "Lebanese Spiced Hot Chocolate with Cow Milk", "Lebanese Spiced Hot Chocolate with Soya Milk", "Lebanese Spiced Hot Chocolate with Almond Milk"],
        "peanuts": [], 
        "sesame seeds": ["Warm Za'atar & Garlic Flatbread", "Mezze Platter", "Lentil Soup", "Hommos", "Tony's Hommos", "Baba Ghanuj", "Batata Harra", "Cheese Samboussek", "Falafel", "Lamb Kibbeh", "Whipped Feta Dip", "Halloumi & Roated Figs", "Mama Zohra Salad", "Falafel Salad", "The Wedge Salad", "Summer Salad", "Chicken Wrap", "Falafel Wrap", "Lamb Kofta Wrap", "Chicken Taouk Plate", "Lamb Kofta Plate", "Falafel Plate", "Chocolate Brownie", "Orange Blossom Mouhalabia", "Baklawa Sandwich", "Comptoir Sundae", "Falafel", "Lamb Kofta", "Chicken Taouk", "Halloumi", "Spiced Lamb Kofta", "Spiced Chicken Kofta", "Marinated Chicken Taouk", "Mixed Grill", "Sea Bass Sayadiyah", "Lamb Kofta Roll", "Steak Skewer", "Spinach & Feta Borek", "Warm Flatbread", "Jewelled Couscous", "Garlic Sauce", "Tahina Sauce", "Harissa Sauce", "Fries", "Lebanese Spiced Hot Chocolate with Cow Milk", "Lebanese Spiced Hot Chocolate with Soya Milk", "Lebanese Spiced Hot Chocolate with Almond Milk"],
        "soya": ["Warm Za'atar & Garlic Flatbread", "Mezze Platter", "Lentil Soup", "Hommos", "Tony's Hommos", "Baba Ghanuj", "Whipped Feta Dip", "Chocolate Brownie", "Comptoir Sundae", "Lamb Kofta Roll", "Warm Flatbread", "Teas with Soya Milk", "Hot Chocolate with Soya Milk", "Americano with Soya Milk", "Cappuccino with Soya Milk", "Latte with Soya Milk", "Flat White with Soya Milk", "Mocha with Soya Milk", "Espresso with Soya Milk", "Macchiato with Sayo Milk", "Lebanese Coffee with Soya Milk", "Lebanese Spiced Hot Chocolate with Soya Milk"],
        "sulphur dioxide": ["Selection of Pickes", "Mezze Platter", "Falafel", "Whipped Feta Dip", "Halloumi & Roasted Figs", "Falafel Salad", "Summer Salad", "Falafel Plate", "Orange Blossom Mouhalabia", "Falafel", "Lamb Kofta", "Chicken Taouk", "Halloumi", "Spiced Lamb Kofta", "Spiced Chicken Kofta", "Marinated Chicken Taouk", "Mixed Grill", "Lamb Kofta Roll", "Chicken & Green Olive Tagine"],
    },
    "tags" : ["Greek"]
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
        "Salmon Matsuri platter", "Tsudoi platter", "Yasai platter", 
        "Chilli mayo sauce", "Chinese chilli sauce", "Sweet chilli sauce", "Japanese BBQ sauce", "Japanese dresing", "Teriyaki sauce", "Balsamic vinegar olive oil", 
        "Goma dressing", "Korean chilli sauce", "Ginger sachet", "Soy sauce sachet", "Sweet soy sauce sachet", "Gluten free soy sachet", "Reduced salt soy sauce sachet", "Wasabi sachet",
        "Chicken gyoza tanmen", "Spicy chicken tanmen", "Salmon teriyaki tanmen", "Veg tanmen", "Chicken gyoza soumen", "Spicy chicken soumen", "Veg soumen", "Tofu tom yum", "Prawn tom yum",
        "Chicken tom yum", "Miso soup", "Miso sachet", "Chicken curry bento", "Chicken curry yakisoba", "Chicken katsu curry bento", "Chicken katsu curry yakisoba", "Chicken katsu yakisoba bento", 
        "Spicy chicken bento", "Spicy chicken yakisoba", "Sweet chilli chicken bento", "Sweet chilli chicken yakisoba", "Tofu curry bento", "Tofu curry yakisoba", "Sweet chilli tofu bento", 
        "Sweet chilli tofu yakisoba", "Chicken yakisoba", "Tofu yakisoba", "Plain yakisoba", "Pork bulgogi bento", "Pork bulgogi yakisoba", "Pumpkin katsu curry", "Pumpkin katsu curry yakisoba", 
        "Chicken teriyaki bento", "Chicken teriyaki yakisoba", "Salmon teriyaki bento", "Salmon teriyaki yakisoba", "Thai green chicken curry bento", "Thai green chicken curry yakisoba", 
        "Kale salad", "Soy & garlic K-Wings", "Sweet & spicy K-Wings", "Sweet chilli chicken AIR BENTO", "Tofu curry AIR BENTO", "Pumpkin katsu curry AIR BENTO", "Chicken katsu curry AIR BENTO",
        "Chicken curry AIR BENTO", "Chicken teriyaki yakisoba AIR BENTO", "Chicken katsu", "Pumpkin Katsu", "Tempura prawn", "Fried chicken gyoza", "Steamed chicken gyoza", 
        "Steamed vegtable gyoza", "Chicken katsu bao bun", "Pumpkin katsu bao bun", "Rainbow pot", "Hana pot", "Wabi wrap", "Sabi wrap", "Mango & yogurt", "Berry & yogurt", 
        "Chicken gyoza salad", "Chicken katsu salad", "Chicken yakisoba salad", "Chilli noodle salad", "Chukka wakame salad", "Surimi crabmeat salad", "Wasabi house salad", 
        "Wasabi superfood salad", "King prawn and broccoli salad", "Sweet chilli chicken", "Mixed salad leaves", "Salmon poke potto", "Sweet chilli chicken potto", 
        "Chirashi potto", "Spicy chirashi potto", "Salmon teriyaki potto", "Edamame potto", "Ebi & chicken summer roll salad", "Raw naked tofu salad", "Yasai summer roll set", 
        "Original bubble tea", "Green apple bubble tea", "Lychee & rose bubble tea", "Matcha bubble tea", "Thai milk bubble tea", "Taro bubble tea", ],
    "ratings": ["3.55"],
    "allergens": {
        "celery": ["Surimi crabmeat salad", ],
        "cereals": ["Inari & red pepper hosomaki", "California roll", "Fried prawn roll", "Salmon & mango roll", "Surumi crabmeat & cucumber roll", "Tofu roll", "Salmon teriyaki roll", 
                    "Tofu nigiri", "Surumi crabmeat gunkan", "Chicken teriyaki onigiri", "Salmon teriyaki onigiri", "Seaweed onigiri", "Chicken katsu & kimchi onigiri", 
                    "Tuna & mustard onigiri", "Chumaki set", "Harmony set", "Mini hosomaki set", "Mixed maki set", "Rainbow set", "Salmon nigiri set", "Sashimi set", "Tokyo salmon set",
                    "Mini Tokyo Salmon set", "Osaka set", "Wasabi special bento", "Yasai roll set", "Salmon teriyaki roll set", "Crispy ebi roll", "Chicken katsu roll set", "Veggie roll set",
                    "Tofu pocket roll set", "Salmon hosomaki set", "Avocado hosomaki set", "Cucumber hosomaki set", "Spicy salmon roll", "Spicy yasai roll", "Kyoto set",
                    "Chumaki set - brown rice", "Salmon nigiri set - brown rice", "Rainbow set - brown rice", "Yasai roll set - brown rice", "Harmony set - brown rice", "Chicken katsu salad",
                    "Chirashi bowl", "Salmon teriyaki salad", "Tofu teriyaki salad", "Salmon Matsuri platter", "Tsudoi platter", "Yasai platter", "Chilli mayo sauce", "Chinese chilli sauce",
                    "Sweet chilli sauce", "Japanese BBQ sauce", "Japanese dresing", "Teriyaki sauce", "Balsamic vinegar olive oil", "Goma dressing", "Korean chilli sauce", "Ginger sachet",
                    "Soy sauce sachet", "Sweet soy sauce sachet", "Gluten free soy sachet", "Reduced salt soy sauce sachet", "Wasabi sachet""Japanese dresing", "Teriyaki sauce", "Goma dressing",
                    "Korean chilli sauce", "Soy sauce sachet", "Sweet soy sauce sachet", "Reduced salt soy sauce sachet", "Chicken gyoza tanmen", "Spicy chicken tanmen", "Salmon teriyaki tanmen", 
                    "Veg tanmen", "Chicken gyoza soumen", "Spicy chicken soumen", "Veg soumen", "Tofu tom yum", "Prawn tom yum", "Chicken tom yum", "Miso soup", "Miso sachet", 
                    "Chicken curry bento", "Chicken curry yakisoba", "Chicken katsu curry bento", "Chicken katsu curry yakisoba", "Chicken katsu yakisoba bento", "Spicy chicken bento", 
                    "Spicy chicken bento", "Spicy chicken yakisoba", "Sweet chilli chicken bento", "Sweet chilli chicken yakisoba", "Tofu curry bento", "Tofu curry yakisoba", "Sweet chilli tofu bento",
                    "Sweet chilli tofu yakisoba", "Chicken yakisoba", "Tofu yakisoba", "Plain yakisoba", "Pork bulgogi bento", "Pork bulgogi yakisoba", "Pumpkin katsu curry", "Pumpkin katsu curry yakisoba", 
                    "Chicken teriyaki bento", "Chicken teriyaki yakisoba", "Salmon teriyaki bento", "Salmon teriyaki yakisoba", "Thai green chicken curry yakisoba", "Soy & garlic K-Wings", 
                    "Sweet & spicy K-Wings", "Sweet chilli chicken AIR BENTO", "Tofu curry AIR BENTO", "Pumpkin katsu curry AIR BENTO", "Chicken katsu curry AIR BENTO", "Chicken curry AIR BENTO", 
                    "Chicken teriyaki yakisoba AIR BENTO", "Chicken katsu", "Pumpkin Katsu", "Tempura prawn", "Fried chicken gyoza", "Steamed chicken gyoza", "Steamed vegtable gyoza", 
                    "Chicken katsu bao bun", "Pumpkin katsu bao bun", "Hana pot", "Wabi wrap", "Sabi wrap", "Chicken gyoza salad", "Chicken katsu salad", "Chicken yakisoba salad", 
                    "Chukka wakame salad", "Surimi crabmeat salad", "Sweet chilli chicken", "Salmon poke potto", "Sweet chilli chicken potto", "Chirashi potto", "Spicy chirashi potto", 
                    "Salmon teriyaki potto", "Ebi & chicken summer roll salad", "Raw naked tofu salad", "Yasai summer roll set", ],
        "crustaceans": ["California roll", "Fried prawn roll", "Surumi crabmeat & cucumber roll", "Shrimp nigiri", "Surumi crabmeat gunkan", 
                        "Chicken katsu & kimchi onigiri", "Chumaki set", "Harmony set", "Mixed maki set", "Rainbow set", "Osaka set", "Crispy ebi roll",
                        "Wasabi special bento", "Kyoto set", "Chumaki set - brown rice", "Rainbow set - brown rice", "Harmony set - brown rice", "Chirashi bowl", 
                        "Tsudoi platter", "Prawn tom yum", "Thai green chicken curry bento", "Thai green chicken curry yakisoba",  "Tempura prawn", "Surimi crabmeat salad", 
                        "King prawn and broccoli salad", "Chirashi potto", "Spicy chirashi potto", "Ebi & chicken summer roll salad", "Raw naked tofu salad", ],
        "eggs": ["California roll", "Fried prawn roll", "Surumi crabmeat & cucumber roll", "Japanese omelette nigiri", "Surumi crabmeat gunkan",
                 "Tuna & mustard onigiri", "Chumaki set", "Harmony set", "Mixed maki set", "Rainbow set", "Osaka set", "Crispy ebi roll", "Wasabi special bento", 
                 "Kyoto set", "Chumaki set - brown rice", "Rainbow set - brown rice", "Harmony set - brown rice", "Chicken katsu salad", "Chirashi bowl",
                 "Tsudoi platter", "Chilli mayo sauce", "Chicken gyoza tanmen", "Spicy chicken tanmen", "Chicken gyoza soumen", "Spicy chicken soumen", "Tempura prawn", 
                 "Rainbow pot", "Hana pot", "Wabi wrap", "Sabi wrap", "Chicken gyoza salad", "Chilli noodle salad", "Surimi crabmeat salad", "Wasabi house salad", 
                 "King prawn and broccoli salad", "Chirashi potto", "Spicy chirashi potto", ],
        "fish": ["Salmon hosomaki", "Tuna hosomaki","California roll", "Salmon & mango roll", "Surumi crabmeat & cucumber roll", "Salmon teriyaki roll",
                 "Salmon nigiri", "Tuna nigiri", "Salmon sesame gunkan", "Surumi crabmeat gunkan", "Tuna & mustard onigiri", "Chicken katsu & kimchi onigiri",
                 "Salmon teriyaki onigiri",
                 "Chumaki set", "Harmony set", "Mini hosomaki set", "Mixed maki set", "Rainbow set", "Salmon nigiri set", "Sashimi set", "Tokyo salmon set", "Mini Tokyo Salmon set", "Osaka set",
                 "Salmon hosomaki set", "Salmon teriyaki roll set", "Wasabi special bento", "Spicy salmon roll", "Kyoto set", 
                 "Chumaki set - brown rice", "Salmon nigiri set - brown rice", "Rainbow set - brown rice", "Harmony set - brown rice", "Chirashi bowl", "Salmon teriyaki salad", 
                 "Salmon Matsuri platter", "Tsudoi platter", "Chicken gyoza tanmen", "Spicy chicken tanmen", "Salmon teriyaki tanmen", "Chicken gyoza soumen", "Spicy chicken soumen",
                 "Prawn tom yum", "Chicken tom yum", "Miso soup", "Miso sachet", "Salmon teriyaki bento", "Salmon teriyaki yakisoba", "Soy & garlic K-Wings", "Sweet & spicy K-Wings", 
                 "Surimi crabmeat salad", "Salmon poke potto", "Chirashi potto", "Spicy chirashi potto", "Salmon teriyaki potto", ],
        "lupin": [], 
        "milk": ["Fried prawn roll", "Chumaki set", "Harmony set", "Mixed maki set", "Rainbow set", "Crispy ebi roll", "Chumaki set - brown rice", "Rainbow set - brown rice", 
                 "Harmony set - brown rice", "Tsudoi platter", "Tempura prawn", "Rainbow pot", "Hana pot", "Wabi wrap", "Sabi wrap", "Mango & yogurt", "Berry & yogurt", "Chirashi potto",
                 "Spicy chirashi potto", "Ebi & chicken summer roll salad", "Raw naked tofu salad", "Original bubble tea", "Matcha bubble tea", "Thai milk bubble tea", "Taro bubble tea", ],
        "molluscs": [],
        "mustard": ["Surumi crabmeat gunkan", "Tuna & mustard onigiri",
                    "Chumaki set", "Harmony set", "Mini hosomaki set", "Mixed maki set", "Rainbow set", "Salmon nigiri set", "Sashimi set", "Tokyo salmon set", "Mini Tokyo Salmon set", "Osaka set",
                    "Wasabi special bento", "Yasai roll set", "Salmon teriyaki roll set", "Crispy ebi roll", "Chicken katsu roll set", "Veggie roll set", "Tofu pocket roll set",
                    "Salmon hosomaki set", "Avocado hosomaki set", "Cucumber hosomaki set", "Spicy salmon roll", "Spicy yasai roll", "Kyoto set", 
                    "Chumaki set - brown rice", "Salmon nigiri set - brown rice", "Rainbow set - brown rice", "Yasai roll set - brown rice", "Harmony set - brown rice", 
                    "Chirashi bowl", "Salmon teriyaki salad", "Tofu teriyaki salad", "Salmon Matsuri platter", "Tsudoi platter", "Yasai platter", "Japanese dresing", "Wasabi sachet", 
                    "Chicken katsu bao bun", "Pumpkin katsu bao bun", "Surimi crabmeat salad", "King prawn and broccoli salad", "Salmon poke potto", "Chirashi potto", "Spicy chirashi potto", 
                    ],
        "nuts": ["Wasabi house salad", "Wasabi superfood salad", ],
        "peanuts": ["Goma dressing", "Ebi & chicken summer roll salad", "Raw naked tofu salad", "Yasai summer roll set", ], 
        "sesame seeds": ["California roll", "Fried prawn roll", "Salmon teriyaki roll", "Salmon sesame gunkan", "Chicken katsu & kimchi onigiri",
                         "Seaweed onigiri", "Salmon teriyaki onigiri", "Chicken teriyaki onigiri", "Chumaki set", "Harmony set", "Mini hosomaki set", 
                         "Mixed maki set", "Rainbow set", "Salmon nigiri set", "Sashimi set", "Osaka set", "Chicken katsu roll set", "Crispy ebi roll",
                         "Salmon teriyaki roll set", "Yasai roll set", "Spicy salmon roll",
                         "Chumaki set - brown rice", "Salmon nigiri set - brown rice", "Rainbow set - brown rice", "Yasai roll set - brown rice", "Harmony set - brown rice", 
                         "Chicken katsu salad", "Chirashi bowl", "Salmon teriyaki salad", "Tofu teriyaki salad", "Tsudoi platter", "Yasai platter", "Goma dressing", "Korean chilli sauce",
                         "Chicken gyoza tanmen", "Spicy chicken tanmen", "Salmon teriyaki tanmen", "Veg tanmen", "Chicken gyoza soumen", "Spicy chicken soumen", "Tofu tom yum", "Prawn tom yum", "Chicken tom yum", 
                         "Chicken curry yakisoba", "Chicken katsu curry yakisoba", "Chicken katsu yakisoba bento", "Spicy chicken bento", "Spicy chicken yakisoba", "Sweet chilli chicken yakisoba", 
                         "Tofu curry yakisoba", "Sweet chilli tofu yakisoba", "Chicken yakisoba", "Tofu yakisoba", "Plain yakisoba", "Pork bulgogi bento", "Pork bulgogi yakisoba", "Pumpkin katsu curry yakisoba", 
                         "Chicken teriyaki bento", "Chicken teriyaki yakisoba", "Salmon teriyaki bento", "Salmon teriyaki yakisoba", "Thai green chicken curry yakisoba", "Chicken teriyaki yakisoba AIR BENTO", 
                         "Fried chicken gyoza", "Steamed chicken gyoza", "Hana pot", "Sabi wrap", "Chicken gyoza salad", "Chicken yakisoba salad", "Chukka wakame salad", "Chirashi potto",
                         "Spicy chirashi potto", "Salmon teriyaki potto", "Ebi & chicken summer roll salad", "Raw naked tofu salad", "Yasai summer roll set", ],
        "soya": ["Inari & red pepper hosomaki", "California roll", "Fried prawn roll", "Salmon & mango roll", "Surumi crabmeat & cucumber roll",
                 "Tofu roll", "Salmon teriyaki roll", "Tofu nigiri", "Salmon sesame gunkan", "Surumi crabmeat gunkan", "Chicken katsu & kimchi onigiri",
                 "Edamame & butternut squash onigiri", "Seaweed onigiri", "Salmon teriyaki onigiri", "Chicken teriyaki onigiri",
                 "Chumaki set", "Harmony set", "Mini hosomaki set", "Mixed maki set", "Rainbow set", "Salmon nigiri set", "Sashimi set", "Tokyo salmon set", "Mini Tokyo Salmon set", "Osaka set",
                 "Wasabi special bento", "Yasai roll set", "Salmon teriyaki roll set", "Crispy ebi roll", "Chicken katsu roll set", "Veggie roll set", "Tofu pocket roll set",
                 "Salmon hosomaki set", "Avocado hosomaki set", "Cucumber hosomaki set", "Spicy salmon roll", "Spicy yasai roll", "Kyoto set", 
                 "Chumaki set - brown rice", "Salmon nigiri set - brown rice", "Rainbow set - brown rice", "Yasai roll set - brown rice", "Harmony set - brown rice", 
                 "Chicken katsu salad", "Chirashi bowl", "Salmon teriyaki salad", "Tofu teriyaki salad", "Salmon Matsuri platter", "Tsudoi platter", "Yasai platter", "Japanese dresing",
                 "Teriyaki sauce", "Goma dressing", "Korean chilli sauce", "Soy sauce sachet", "Sweet soy sauce sachet", "Gluten free soy sachet", "Reduced salt soy sauce sachet",
                 "Chicken gyoza tanmen", "Spicy chicken tanmen", "Salmon teriyaki tanmen", "Veg tanmen", "Chicken gyoza soumen", 
                 "Spicy chicken soumen", "Veg soumen", "Tofu tom yum", "Prawn tom yum", "Chicken tom yum", "Miso soup", "Miso sachet", "Chicken curry bento", "Chicken curry yakisoba", 
                 "Chicken katsu curry bento", "Chicken katsu curry yakisoba", "Chicken katsu yakisoba bento", "Spicy chicken bento", "Spicy chicken yakisoba", "Sweet chilli chicken bento", 
                 "Sweet chilli chicken yakisoba", "Tofu curry bento", "Tofu curry yakisoba", "Sweet chilli tofu bento", "Sweet chilli tofu yakisoba", "Chicken yakisoba", "Tofu yakisoba", 
                 "Plain yakisoba", "Pork bulgogi bento", "Pork bulgogi yakisoba", "Pumpkin katsu curry", "Pumpkin katsu curry yakisoba", "Chicken teriyaki bento", "Chicken teriyaki yakisoba", 
                 "Salmon teriyaki bento", "Salmon teriyaki yakisoba", "Thai green chicken curry bento", "Thai green chicken curry yakisoba", "Kale salad", "Soy & garlic K-Wings", "Sweet & spicy K-Wings", 
                 "Sweet chilli chicken AIR BENTO", "Tofu curry AIR BENTO", "Pumpkin katsu curry AIR BENTO", "Chicken katsu curry AIR BENTO", "Chicken curry AIR BENTO", "Chicken teriyaki yakisoba AIR BENTO", 
                 "Chicken katsu", "Tempura prawn", "Fried chicken gyoza", "Steamed chicken gyoza", "Steamed vegtable gyoza", "Chicken katsu bao bun", "Hana pot", "Sabi wrap", "Chicken gyoza salad", 
                 "Chicken katsu salad", "Chicken yakisoba salad", "Chukka wakame salad", "Surimi crabmeat salad", "Sweet chilli chicken", "Salmon poke potto", "Sweet chilli chicken potto", 
                 "Chirashi potto", "Spicy chirashi potto", "Salmon teriyaki potto", "Edamame potto", "Ebi & chicken summer roll salad", "Raw naked tofu salad", "Yasai summer roll set", 
                 ],
        "sulphur dioxide": ["Surumi crabmeat & cucumber roll", "Surumi crabmeat gunkan", "Chicken katsu & kimchi onigiri", "Chicken teriyaki onigiri", 
                            "Chumaki set", "Harmony set", "Mixed maki set", "Rainbow set", "Osaka set", "Wasabi special bento", "Spicy yasai roll", "Kyoto set", 
                            "Chumaki set - brown rice", "Rainbow set - brown rice", "Harmony set - brown rice", "Chirashi bowl", "Chinese chilli sauce", "Balsamic vinegar olive oil",
                            "Spicy chicken tanmen", "Spicy chicken soumen", "Tofu tom yum", "Chicken tom yum", "Chicken curry yakisoba", "Chicken katsu curry yakisoba", "Chicken katsu yakisoba bento", 
                            "Spicy chicken yakisoba", "Sweet chilli chicken yakisoba", "Tofu curry yakisoba", "Sweet chilli tofu yakisoba", "Chicken yakisoba", "Tofu yakisoba", "Pork bulgogi yakisoba", 
                            "Pumpkin katsu curry yakisoba", "Chicken teriyaki bento", "Chicken teriyaki yakisoba", "Salmon teriyaki yakisoba", "Thai green chicken curry yakisoba", 
                            "Chicken teriyaki yakisoba AIR BENTO", "Chicken katsu bao bun", "Pumpkin katsu bao bun", "Chicken yakisoba salad", 
                            "Surimi crabmeat salad", "Chirashi potto", "Spicy chirashi potto", ],
    },
    "tags" : ["Japanese", "Sushi"]
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
    },
    "tags" : ["American", "Fast Food", "Burgers"]
}

honestBurger = {
    "name": "Honest Burger",
    "location": "location coordinates",
    "city": "London",
    "menu": ["Caribbean Fried Chicken Burger", "Plant Burger", "Beef Burger", "Cheese Burger", "Blue Cheese Burger", "Honest Burger", "Tribute Burger", "Chilli Burger", "Pesto Burger",
             "Buffalo Burger", "Fritter Burger", "Vegan Fritter Burger", "Vegan Teriyaki Burger", "Smashed By Honest", "Rosemary Salted Chips", "Buffalo Wings", "Onion Rings",
             "Dressed Green Salad", "Seasonal Coleslaw", "Vegan Chipotle Slaw", "Chicken Tenders", "Mushroom Fritters", "Gluten Free Bun - Order w/ burger to make it GF",
             "Honest Hot Sauce", "Chipotle Mayo",
             "Vegan Chipotle Mayo", "Vegan Bacon Ketchup", "Bacon Gravy", "Cheesy Bacon Gravy", "BBQ Honey Mustard", "South Kensington", "Homemade Lemonade", "Homemade Mint Lemonade",
             "Botanic Garden", "Brozen Bar Old Fashioned", "Grapefruit Spritz", "Bristol Cain & Ting", "Brighton Hugo", "Cambridge G&T", "Cardiff G&T", "Liverpool G&T",
             "Manchester Salford Mule", "Portabello G&T", "Jeffrey's G&T", "Pink G&T", "Espresso Martini", "Kings St Punch", "Portabello Spritz", "Vanilla Milkshake", "Strawberry Milkshake",
             "Aperol Spritz", "Original: Chocolate Milkshake", "Original: Salted Caramel Milkshake", "Honey I'm Home", "Rum Bongo", "Winter Spiced Mule", "Smashed Cheeseburger",
             "Smashed Baconburger", "Smashed Fried Chicken Burger", "Smashed Cali Burger", "Smashed BBQ Burger", "Smashed Chilli Burger", "Smashed Plant Burger", ],
    "ratings": ["4.50"],
    "allergens": {
        "celery": ["Caribbean Fried Chicken Burger", "Tribute Burger", "Dressed Green Salad", "Vegan Bacon Ketchup", "Smashed Cali Burger", ],
        "cereals": ["Caribbean Fried Chicken Burger", "Plant Burger", "Beef Burger", "Cheese Burger", "Blue Cheese Burger", "Honest Burger", "Tribute Burger", "Chilli Burger", "Pesto Burger",
                    "Buffalo Burger", "Fritter Burger", "Vegan Fritter Burger", "Vegan Teriyaki Burger", "Smashed By Honest", "South Kensington", "Vanilla Milkshake", "Strawberry Milkshake", 
                    "Smashed Cheeseburger", "Smashed Baconburger", "Smashed Fried Chicken Burger", "Smashed Cali Burger", "Smashed BBQ Burger", "Smashed Chilli Burger", "Smashed Plant Burger", ],
        "crustaceans": [],
        "eggs": ["Caribbean Fried Chicken Burger", "Beef Burger", "Cheese Burger", "Blue Cheese Burger", "Honest Burger", "Tribute Burger", "Chilli Burger", "Pesto Burger", "Buffalo Burger",
                 "Fritter Burger", "Vegan Fritter Burger", "Smashed By Honest", "Buffalo Wings", "Seasonal Coleslaw", "Chicken Tenders", "Gluten Free Bun - Order w/ burger to make it GF",
                 "Chipotle Mayo", "South Kensington", "Vanilla Milkshake", "Strawberry Milkshake", "Smashed Cheeseburger", "Smashed Baconburger", "Smashed Fried Chicken Burger", "Smashed Cali Burger", 
                 "Smashed BBQ Burger", "Smashed Chilli Burger", ],
        "fish": ["Tribute Burger", "Buffalo Burger", "Chicken Tenders", "Smashed Cali Burger", ],
        "lupin": ["Gluten Free Bun - Order w/ burger to make it GF", ], 
        "milk": ["Caribbean Fried Chicken Burger", "Beef Burger", "Cheese Burger", "Blue Cheese Burger", "Honest Burger", "Tribute Burger", "Chilli Burger", "Pesto Burger", "Buffalo Burger",
                 "Fritter Burger", "Vegan Fritter Burger", "Smashed By Honest", "Buffalo Wings", "Seasonal Coleslaw", "Chicken Tenders", "Gluten Free Bun - Order w/ burger to make it GF",
                 "Cheesy Bacon Gravy", "South Kensington", "Vanilla Milkshake", "Strawberry Milkshake", "Original: Chocolate Milkshake", "Original: Salted Caramel Milkshake", "Smashed Cheeseburger", 
                 "Smashed Baconburger", "Smashed Fried Chicken Burger", "Smashed Cali Burger", "Smashed BBQ Burger", "Smashed Chilli Burger", ],
        "molluscs": [],
        "mustard": ["Caribbean Fried Chicken Burger", "Plant Burger", "Honest Burger", "Tribute Burger", "Pesto Burger", "Buffalo Burger", "Fritter Burger", "Vegan Fritter Burger",
                    "Vegan Teriyaki Burger", "Smashed By Honest", "Buffalo Wings", "Dressed Green Salad", "Seasonal Coleslaw", "Vegan Chipotle Slaw", "Chicken Tenders", "Mushroom Fritters",
                    "Gluten Free Bun - Order w/ burger to make it GF", "Chipotle Mayo", "Vegan Chipotle Mayo", "Vegan Bacon Ketchup", "BBQ Honey Mustard", "Smashed Cheeseburger", "Smashed Baconburger", 
                    "Smashed Fried Chicken Burger", "Smashed Cali Burger", "Smashed BBQ Burger", "Smashed Chilli Burger", "Smashed Plant Burger"],
        "nuts": [],
        "peanuts": [], 
        "sesame seeds": ["Gluten Free Bun - Order w/ burger to make it GF", ],
        "soya": ["Caribbean Fried Chicken Burger", "Plant Burger", "Beef Burger", "Cheese Burger", "Blue Cheese Burger", "Honest Burger", "Tribute Burger", "Chilli Burger", "Pesto Burger", "Buffalo Burger",
                 "Fritter Burger", "Vegan Fritter Burger", "Vegan Teriyaki Burger", "Smashed By Honest", "Onion Rings", "Mushroom Fritters", "Gluten Free Bun - Order w/ burger to make it GF",
                 "Vegan Bacon Ketchup", "Bacon Gravy", "Cheesy Bacon Gravy", "South Kensington", "Smashed Cheeseburger", "Smashed Baconburger", "Smashed Fried Chicken Burger", "Smashed Cali Burger", 
                 "Smashed BBQ Burger", "Smashed Chilli Burger", "Smashed Plant Burger", ],
        "sulphur dioxide": ["Caribbean Fried Chicken Burger", "Plant Burger", "Beef Burger", "Cheese Burger", "Blue Cheese Burger", "Honest Burger", "Pesto Burger", "Buffalo Burger", "Fritter Burger",
                            "Vegan Fritter Burger", "Smashed By Honest", "Buffalo Wings", "Dressed Green Salad", "Vegan Chipotle Slaw", "Mushroom Fritters", "Vegan Chipotle Mayo", "Vegan Bacon Ketchup",
                            "Bacon Gravy", "Cheesy Bacon Gravy", "Grapefruit Spritz", "Brighton Hugo", "Portabello Spritz", "Aperol Spritz", "Smashed Baconburger", "Smashed Cali Burger", "Smashed BBQ Burger", 
                            "Smashed Plant Burger", ],
    },
    "tags" : ["American", "Burgers"]
}

tapasBrindisa = {
    "name": "Tapas Brindisa",
    "location": "location coordinates",
    "city": "London",
    "menu": ["Pan de Coca con Tomate", "Aceitunas Gordales Perello", "Pimientos do Padron", "Jamon Croquetas", "Anchovy with onions", "Beetroot Salmorejo", 
             "Sea Bream Ceviche, Apple & Radishes", "Boquerones Chilli & Parsley", 
             "Squid ala Plancha Black Ink Sauce", "Leon Chorizo", "Sirloin", "Skrei Cod", "Pollo al Limon", "White Asparagus Gratin",
             "Octopus with saffron olive oil mash",
             "Huevos Rotos con Sobrasada", "Monte Enebro", "patatas Bravas y Alioli", "Tortilla Espanola", "Huevos Rotos con pisto", 
             "Arroz Negro (to share)", "Lamb Shoulder", "Gambas al Ajillo", "Faba beans base",
             "Pan de la casa", "Spring salad", "Raw Cavolo salad", "Spinach Catalan", "Iberico Jamon de Bellota", "Tabla de Quesos", "Seleccion de Charcuteria",
             "Vanilla Ice Cream", "Coconut & Lime rice pudding", "Bitter chocolate and orange catalana", "Cheesecake"],
    "ratings": ["4.20"],
    "allergens": {
        "celery": ["Squid ala Plancha Black Ink Sauce", "Skrei Cod", "Octopus with saffron olive oil mash", "Arroz Negro (to share)", "Tabla de Quesos", "Seleccion de Charcuteria",],
        "cereals": ["Pan de Coca con Tomate", "Jamon Croquetas", "Anchovy with onions", "Sea Bream Ceviche, Apple & Radishes", "Leon Chorizo", "White Asparagus Gratin",
                    "Octopus with saffron olive oil mash", "Monte Enebro",
                    "Pan de la casa", "Raw Cavolo salad", "Spinach Catalan", "Iberico Jamon de Bellota", "Tabla de Quesos", "Seleccion de Charcuteria",
                    "Bitter chocolate and orange catalana",],
        "crustaceans": ["Squid ala Plancha Black Ink Sauce", "Skrei Cod", "Octopus with saffron olive oil mash", "Arroz Negro (to share)", "Gambas al Ajillo",],
        "eggs": ["Jamon Croquetas", "White Asparagus Gratin", "Huevos Rotos con Sobrasada", "Monte Enebro", "patatas Bravas y Alioli", "Tortilla Espanola", "Huevos Rotos con pisto", 
                 "Arroz Negro (to share)", "Raw Cavolo salad", "Tabla de Quesos", "Vanilla Ice Cream", "Bitter chocolate and orange catalana", "Cheesecake"],
        "fish": ["Aceitunas Gordales Perello", "Anchovy with onions", "Beetroot Salmorejo", "Sea Bream Ceviche, Apple & Radishes", "Boquerones Chilli & Parsley", 
                 "Squid ala Plancha Black Ink Sauce", "Skrei Cod", "Pollo al Limon", "Octopus with saffron olive oil mash", "Arroz Negro (to share)",
                 "Gambas al Ajillo", "Raw Cavolo salad", "Seleccion de Charcuteria",],
        "lupin": [], 
        "milk": ["Jamon Croquetas", "Squid ala Plancha Black Ink Sauce", "Leon Chorizo", "Skrei Cod", "White Asparagus Gratin", "Octopus with saffron olive oil mash",
                 "Monte Enebro", "Arroz Negro (to share)", "Pan de la casa", "Raw Cavolo salad", "Tabla de Quesos", "Seleccion de Charcuteria",
                 "Vanilla Ice Cream", "Bitter chocolate and orange catalana", "Cheesecake"],
        "molluscs": ["Squid ala Plancha Black Ink Sauce", "Skrei Cod", "Octopus with saffron olive oil mash", "Arroz Negro (to share)",],
        "mustard": ["Sea Bream Ceviche, Apple & Radishes"],
        "nuts": ["Aceitunas Gordales Perello", "Sea Bream Ceviche, Apple & Radishes", "Pollo al Limon", "White Asparagus Gratin", "Monte Enebro",
                 "Pan de la casa", "Spring salad", "Spinach Catalan", "Tabla de Quesos", "Seleccion de Charcuteria", "Bitter chocolate and orange catalana"],
        "peanuts": ["White Asparagus Gratin", "Pan de la casa", "Spinach Catalan",], 
        "sesame seeds": ["Sea Bream Ceviche, Apple & Radishes", "Pollo al Limon", "White Asparagus Gratin", "Tabla de Quesos", "Seleccion de Charcuteria",],
        "soya": ["Octopus with saffron olive oil mash", "Tabla de Quesos", "Seleccion de Charcuteria", "Coconut & Lime rice pudding", "Bitter chocolate and orange catalana"],
        "sulphur dioxide": ["Aceitunas Gordales Perello", "Anchovy with onions", "Beetroot Salmorejo", "Sea Bream Ceviche, Apple & Radishes",
                            "Squid ala Plancha Black Ink Sauce", "Sirloin", "Pollo al Limon", "White Asparagus Gratin", "Octopus with saffron olive oil mash",
                            "Tortilla Espanola", "Arroz Negro (to share)", "Spring salad", "Raw Cavolo salad", "Spinach Catalan",
                            "Tabla de Quesos", "Seleccion de Charcuteria", "Coconut & Lime rice pudding", "Bitter chocolate and orange catalana", "Cheesecake"],
    },
    "tags" : ["Greek"]
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
    },
    "tags" : [],
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

def get_user_info(email):
    for user in db.child("user").get().each():
        if user.val().get('email') == email:
            # print(user.key())
            # print(user.val())
            return user.key(), user.val()
    return None

def foo():
    ref = db.child("user")
    members = ["-NXkKtFF_hiBZ88gE16r", "-NXkKtFF_hiBZ88gE16r", "-NXkKtFF_hiBZ88gE16r"]
    for user in ref.get().each():
        key = user.key()
        db.child("user").child(key).child("groups/group1").set(members)
        db.child("user").child(key).child("groups/group2").set(members)
        
@app.route('/')
def index():
    return app.send_static_file('index.html')

@app.errorhandler(404)
def not_found(e):
    return app.send_static_file('index.html')
    
@app.route('/api/getRestaurantData', methods=["GET"])
def get_restaurant():
    return json.dumps(get_values(db.child("restaurant")))

@app.route('/api/getUserFriends', methods=["GET"])
def getUserFriends():
    return json.dumps(get_values(db.child("user")))

@app.route('/api/getFirstUser', methods=["GET"])
def getUserGroups():
    ref = db.child("user").order_by_key().limit_to_first(1)
    return json.dumps(get_values(ref))

@app.route('/api/add_group/<group_name>', methods=["GET"])
def add_group(group_name):
    db.child("user").child(session['key']).child("groups").child(group_name).set(0)
    session['groups'][group_name] = []
    session.modified = True
    return session['groups']

@app.route('/api/remove_group/<group_name>', methods=["GET"])
def remove_group(group_name):
    db.child("user").child(session['key']).child("groups").child(group_name).remove()
    session['groups'].pop(group_name, None)
    session.modified = True
    return session['groups']

@app.route("/api/get_groups", methods=["GET"])
def groups():
    return session['groups']

@app.route("/api/get_allergens", methods=["GET"])
def get_allergens():
    return {"message": f"{session['allergens']}"}

@app.route("/api/get_user_token", methods=["GET"])
def get_user_token():
    token = session['user']
    user = auth.get_account_info(token)
    return {"message": f"{user}"}

@app.route("/api/get_current_session", methods=["GET"])
def get_current_session():
    return {"message": f"{session}"}

@app.route("/api/register", methods=["POST"])
def register():
    email = request.json.get("email")
    password = request.json.get("password")
    age = int(request.json.get("age"))
    first_name = request.json.get("firstName")
    last_name = request.json.get("lastName")
    try:
        template_data = {
            "age": age, 
            "allergens": [],
            "firstName": first_name,
            "friends": {},
            "groups": {},
            "lastName": last_name,
            "email": email
        }
        user = auth.create_user_with_email_and_password(email, password)
        user_ref = db.child("user").push(template_data)
        session['user'] = user['idToken']
        session['key'] = user_ref['name']
        session['allergens'] = []
        session['friends'] = {}
        session['groups'] = {}
        return {"message": "User created successfully."}, 200
    except Exception as e:
        return {"error": str(e)}, 500

@app.route("/api/login", methods=["POST"])
def login():
    email = request.json.get("email")
    password = request.json.get("password")
    try:
        user = auth.sign_in_with_email_and_password(email, password)
        user = auth.refresh(user['refreshToken'])
        session['user'] = user['idToken']
        session['email'] = email
        key, data = get_user_info(email)
        session['key'] = key
        session['allergens'] = data['allergens'] if ('allergens' in data.keys()) else []
        session['friends'] = data['allergens'] if ('allergens' in data.keys()) else {}
        session['groups'] = data['allergens'] if ('allergens' in data.keys()) else {}
        return {"message": "Login successful."}, 200
    except Exception as e:
        return {"error": str(e)}, 401

@app.route('/api/logout')
def logout():
    for key in ['user', 'allergens', 'friends', 'groups', 'data']:
        session.pop(key, None)
    return {"message": f"{session}"}
    
if __name__ == '__main__':
    app.run(debug=True)

