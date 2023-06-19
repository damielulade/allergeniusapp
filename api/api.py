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


def refresh_info(user, key, email, privacy, allergens, friends, groups, first_name, last_name, user_image, tags):
    session['user'] = user
    session['key'] = key
    session['email'] = email
    session['privacy'] = privacy
    session['allergens'] = allergens
    session['friends'] = friends
    session['groups'] = groups
    session['firstName'] = first_name
    session['lastName'] = last_name
    session['userImage'] = user_image
    session['current_filter'] = "Myself"
    session['restaurants_view'] = "map"
    session['tags'] = tags


def get_values(ref, limit=10):
    res = []
    for record in ref.get().each():
        res.append(record.val())
    return res


def delete_values(ref):
    for record in ref.get().each():
        key = record.key()
        ref.child(key).remove()


def get_user_by_email(email):
    for user in db.child("user").get().each():
        if user.val().get('email') == email:
            return user.key(), user.val()
    return None, None


def get_user_by_key(key):
    return db.child("user").child(key).get().val()


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


@app.route('/api/groups', methods=["GET", "POST"])
def groups():
    if request.method == 'POST':
        group_name = request.json.get("groupName")
        mode = request.json.get("mode")
        action = request.json.get("action")
        if mode == "group":
            if (action == "add"):
                # db.child("user").child(session['key']).child("groups").child(group_name).set(0)
                session['groups'][group_name] = []
                session.modified = True
            elif (action == "remove"):
                db.child("user").child(session['key']).child("groups").child(group_name).remove()
                session['groups'].pop(group_name, None)
                session.modified = True
        elif mode == "member":
            user = request.json.get("member")
            # print(user)
            temp = session['groups'][group_name]
            if action == "add":
                temp.append(user)
            if action == "remove":
                temp.remove(user)
            session['groups'][group_name] = list(set(temp))
            session.modified = True
            db.child("user").child(session['key']).child("groups").set(session['groups'])
    return session['groups']


@app.route('/api/update_db/<field>', methods=["GET"])
def update_db(field):
    db.child("user").child(session['key']).child(field).set(session[field])
    return json.dumps([])
    

@app.route('/api/allergens', methods=["GET", "POST"])
def allergens():
    if request.method == 'POST':
        allergen = request.json.get("allergen")
        new_state = request.json.get("newState")
        temp = session['allergens']
        if (new_state == True):
            temp.append(allergen)
        elif (new_state == False):
            temp.remove(allergen)
        session['allergens'] = list(set(temp))
        session.modified = True
        db.child("user").child(session['key']).child("allergens").set(session['allergens'])
    return session['allergens']


@app.route('/api/friends', methods=["GET", "POST"], defaults={'settings': None})
@app.route('/api/friends/<settings>', methods=["GET", "POST"])
def friends(settings):
    if request.method == 'POST':
        friend_key = request.json.get("friendKey")
        mode = request.json.get("mode")
        temp = session['friends']
        if (mode == "add"):
            temp[friend_key] = get_user_by_key(friend_key)
        elif (mode == "remove"):
            temp.pop(friend_key, None)
        session['friends'] = temp
        print("Looking for temp keys work as below:")
        print(list(temp.keys()))
        db.child("user").child(session['key']).child("friends").set(list(temp.keys()))
    if (settings == 'live'):
        friends = db.child("user").child(session['key']).child("friends").get().val()
        if friends:
            for friend in list(friends):
                session['friends'][friend] = get_user_by_key(friend)
                session.modified = True
        print("Looking for friends list")
        print(session)
    return session['friends']


@app.route('/api/privacy', methods=["GET", "POST"])
def privacy():
    if request.method == 'POST':
        new_state = request.json.get("newState")
        db.child("user").child(session['key']).child("privacy").set(new_state)
        session['privacy'] = new_state
        session.modified = True
    return json.dumps(session['privacy'])

@app.route('/api/set_restaurant_filter', methods=["GET", "POST"])
def set_restaurant_filter():
    if request.method == 'POST':
        cuisine = request.json.get("cuisine")
        new_state = request.json.get("newState")
        temp = session['tags']
        if (new_state == True):
            temp.append(cuisine)
        elif (new_state == False):
            temp.remove(cuisine)
        session['tags'] = list(set(temp))
        session.modified = True
    return json.dumps(session['tags'])

@app.route('/api/current_filter/<mode>', methods=["GET", "POST"])
def current_filter(mode):
    if mode == "setting":
        if request.method == 'POST':
            new_state = request.json.get("newState")
            session['current_filter'] = new_state
            session.modified = True
    if mode == "allergens":
        filter = session['current_filter']
        if filter == "Myself":
            return session['allergens']
        else:
            res = session['allergens']
            users = session['groups'][filter]
            for user in users:
                data = db.child("user").child(user).child("allergens").get().val()
                if (data):
                    res.extend(data)
            return list(set(res))
    return json.dumps(session['current_filter'])


@app.route('/api/view', methods=["GET", "POST"])
def view():
    if request.method == "POST":
        new_state = request.json.get("newState")
        session['restaurants_view'] = new_state
        session.modified = True
    return json.dumps(session['restaurants_view'])


@app.route('/api/user_by_email/<email>', methods=["GET"])
def user_by_email(email):
    try:
        if (session['email'] == email.lower()):
            raise Exception("You cannot request the current user using this API request")
        key, data = get_user_by_email(email)
        if (key):
            return key
        else:
            raise Exception("Server canot find a user with this email.")
    except Exception as e:
        return {"error": str(e)}, 500


@app.route('/api/get_name', methods=["GET"])
def get_name():
    return session['firstName'] + " " + session['lastName']


@app.route('/api/get_user_image', methods=["GET"])
def get_user_image():
    try:
        return session['userImage']
    except KeyError:
        return ""
    
@app.route('/api/get_friend_name', methods=["GET"])
def get_friend_name(member):
    friend = db.child("user").child(member.id).get()
    return (friend["firstname"] + " " + friend["lastName"])


@app.route("/api/get_user_token", methods=["GET"])
def get_user_token():
    token = session['user']
    user = auth.get_account_info(token)
    return {"message": f"{user}"}


@app.route("/api/get_current_session", methods=["GET"])
def get_current_session():
    return json.dumps(list(session.items()))


@app.route("/api/register", methods=["POST"])
def register():
    email = request.json.get("email")
    password = request.json.get("password")
    age = int(request.json.get("age"))
    first_name = request.json.get("firstName")
    last_name = request.json.get("lastName")
    try:
        user = auth.create_user_with_email_and_password(email, password)
        # print("I'm working!!")
        new_ref = db.child("user").push({
            "age": age,
            "allergens": [],
            "firstName": first_name,
            "friends": [],
            "groups": {},
            "lastName": last_name,
            "email": email.lower(),
            "privacy": False,
            "userImage": "default",
        })
        refresh_info(user['idToken'], new_ref['name'], email.lower(), False, [], {}, {}, first_name, last_name, "default", [])
        # print(first_name)
        # print(last_name)
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
        key, data = get_user_by_email(email.lower())
        allergens = list(set(data['allergens'])) if ('allergens' in data.keys()) else []
        friends = {}
        if 'friends' in data.keys():
            for friend in data['friends']:
                friends[friend] = get_user_by_key(friend)
        groups = data['groups'] if ('groups' in data.keys()) else {}
        privacy = data['privacy'] if ('privacy' in data.keys()) else False

        first_name = data['firstName'] if ('firstName' in data.keys()) else {}
        last_name = data['lastName'] if ('lastName' in data.keys()) else {}

        user_image = data['userImage'] if ('userImage' in data.keys()) else "default"

        refresh_info(user['idToken'], key, email.lower(), privacy, allergens, friends, groups, first_name, last_name, user_image, [])
        return {"message": "Login successful."}, 200
    except Exception as e:
        return {"error": str(e)}, 401


@app.route('/api/logout')
def logout():
    for key in ['user', 'key', 'email', 'privacy', 'allergens', 'friends', 'groups', 'first_name', 'last_name', 'user_image', 'current_filter']:
        session.pop(key, None)
    return {"message": "Successfully logged out"}

if __name__ == '__main__':
    app.run(debug=True)

# default restaurants
restaurantA = {
    "name": "Restaurant A",
    "location": "location coordinates",
    "city": "London",
    "menu": ["peperroni pizza", "hotdog", "burger", "soup"],
    "ratings": ["5"],
    "allergens": {"cereals": ["hotdog", "burger", "peperroni pizza"], "soybeans": ["soup"]},
    "tags": ["Pizza", "American"]
}

restaurantB = {
    "name": "Restaurant B",
    "location": "location coordinates",
    "city": "London",
    "menu": ["salad", "sandwich"],
    "ratings": ["4"],
    "allergens": {"celery": ["salad"], "cereals": ["sandwich"], "sesame": ["salad"]},
    "tags": ["Greek", "American"]
}

restaurantC = {
    "name": "Restaurant C",
    "location": "location coordinates",
    "city": "London",
    "menu": ["fries", "burger", "garlic bread"],
    "ratings": ["3"],
    "allergens": {"cereals": ["burger", "garlic bread"], "sesame": ["fries"]},
    "tags": ["Burgers", "American"]
}

chopstix = {
    "name": "Chopstix",
    "location": "location coordinates",
    "city": "London",
    "menu": ["Egg Fried Rice", "Seasoned Rice", "Vegetable Noodles", "Skinny Rice", "Red Thai Chicken Curry",
             "Chinese Chicken Curry", "Massaman Chicken Curry", "Teriyaki Beef", "Plant Based Beef Stirfry TRIAL",
             "Pumpkin Katsu Curry", "Salt & Pepper Potatoes", "Mini Vegetable Spring Rolls",
             "Churros Sticks (without sauce)", "Wedges & Curry Sauce", "Noodle Bowl with Spring Rolls & Katsu Sauce",
             "Caramel Drizzle Chicken", "Salt 'n' Pepper Chicken", "Sweet & Sour Chicken", "BBQ Chicken",
             "Lemon Chicken TRIAL", "Katsu Chicken Curry", "Sweet Chilli Prawns", "Salt N Pepper Spicy Wings",
             "Prawn Crackers", "Duck Spring Rolls", "Chicken Balls - large & mini",
             "Noodle Bowl with Spicy Chicken Wings & Katsu Sauce", "Sweet Chilli Sauce POT", "Katsu Sauce",
             "Chocolate Sauce (Churros)", "Caramel Sauce (Churros)"],
    "ratings": ["3.6"],
    "allergens": {
        "celery": ["Red Thai Chicken Curry", "Plant Based Beef Stirfry TRIAL", "Pumpkin Katsu Curry",
                   "Plant Based Beef Stirfry TRIAL", "Pumpkin Katsu Curry", "Salt & Pepper Potatoes",
                   "Mini Vegetable Spring Rolls", "Churros Sticks (without sauce)", "Wedges & Curry Sauce",
                   "Noodle Bowl with Spring Rolls & Katsu Sauce", "Caramel Drizzle Chicken", "Salt 'n' Pepper Chicken",
                   "Sweet & Sour Chicken", "BBQ Chicken", "Lemon Chicken TRIAL", "Katsu Chicken Curry",
                   "Sweet Chilli Prawns", "Salt N Pepper Spicy Wings", "Prawn Crackers", "Duck Spring Rolls",
                   "Chicken Balls - large & mini", "Noodle Bowl with Spicy Chicken Wings & Katsu Sauce"],
        "cereals": ["Egg Fried Rice", "Seasoned Rice", "Vegetable Noodles", "Skinny Rice", "Red Thai Chicken Curry",
                    "Chinese Chicken Curry", "Massaman Chicken Curry", "Teriyaki Beef",
                    "Plant Based Beef Stirfry TRIAL", "Pumpkin Katsu Curry", "Salt & Pepper Potatoes",
                    "Mini Vegetable Spring Rolls", "Churros Sticks (without sauce)", "Wedges & Curry Sauce",
                    "Noodle Bowl with Spring Rolls & Katsu Sauce", "Caramel Drizzle Chicken", "Salt 'n' Pepper Chicken",
                    "Sweet & Sour Chicken", "BBQ Chicken", "Lemon Chicken TRIAL", "Katsu Chicken Curry",
                    "Sweet Chilli Prawns", "Salt N Pepper Spicy Wings", "Prawn Crackers", "Duck Spring Rolls",
                    "Chicken Balls - large & mini", "Noodle Bowl with Spicy Chicken Wings & Katsu Sauce",
                    "Katsu Sauce"],
        "crustaceans": ["Massaman Chicken Curry", "Teriyaki Beef", "Pumpkin Katsu Curry", "Salt & Pepper Potatoes",
                        "Mini Vegetable Spring Rolls", "Churros Sticks (without sauce)", "Wedges & Curry Sauce",
                        "Noodle Bowl with Spring Rolls & Katsu Sauce", "Caramel Drizzle Chicken",
                        "Salt 'n' Pepper Chicken", "Sweet & Sour Chicken", "BBQ Chicken", "Lemon Chicken TRIAL",
                        "Katsu Chicken Curry", "Sweet Chilli Prawns", "Salt N Pepper Spicy Wings", "Prawn Crackers",
                        "Duck Spring Rolls", "Chicken Balls - large & mini",
                        "Noodle Bowl with Spicy Chicken Wings & Katsu Sauce"],
        "eggs": ["Egg Fried Rice", "Vegetable Noodles", "Pumpkin Katsu Curry", "Salt & Pepper Potatoes",
                 "Mini Vegetable Spring Rolls", "Churros Sticks (without sauce)", "Wedges & Curry Sauce",
                 "Noodle Bowl with Spring Rolls & Katsu Sauce", "Caramel Drizzle Chicken", "Salt 'n' Pepper Chicken",
                 "Sweet & Sour Chicken", "BBQ Chicken", "Lemon Chicken TRIAL", "Katsu Chicken Curry",
                 "Sweet Chilli Prawns", "Salt N Pepper Spicy Wings", "Prawn Crackers", "Duck Spring Rolls",
                 "Chicken Balls - large & mini", "Noodle Bowl with Spicy Chicken Wings & Katsu Sauce"],
        "fish": ["Massaman Chicken Curry", "Pumpkin Katsu Curry", "Salt & Pepper Potatoes",
                 "Mini Vegetable Spring Rolls", "Churros Sticks (without sauce)", "Wedges & Curry Sauce",
                 "Noodle Bowl with Spring Rolls & Katsu Sauce", "Caramel Drizzle Chicken", "Salt 'n' Pepper Chicken",
                 "Sweet & Sour Chicken", "BBQ Chicken", "Lemon Chicken TRIAL", "Katsu Chicken Curry",
                 "Sweet Chilli Prawns", "Salt N Pepper Spicy Wings", "Prawn Crackers", "Duck Spring Rolls",
                 "Chicken Balls - large & mini", "Noodle Bowl with Spicy Chicken Wings & Katsu Sauce"],
        "lupin": [],
        "milk": ["Vegetable Noodles", "Plant Based Beef Stirfry TRIAL", "Pumpkin Katsu Curry", "Salt & Pepper Potatoes",
                 "Mini Vegetable Spring Rolls", "Churros Sticks (without sauce)", "Wedges & Curry Sauce",
                 "Noodle Bowl with Spring Rolls & Katsu Sauce", "Caramel Drizzle Chicken", "Salt 'n' Pepper Chicken",
                 "Sweet & Sour Chicken", "BBQ Chicken", "Lemon Chicken TRIAL", "Katsu Chicken Curry",
                 "Sweet Chilli Prawns", "Salt N Pepper Spicy Wings", "Prawn Crackers", "Duck Spring Rolls",
                 "Chicken Balls - large & mini", "Noodle Bowl with Spicy Chicken Wings & Katsu Sauce", "Caramel Sauce"],
        "molluscs": ["Pumpkin Katsu Curry", "Salt & Pepper Potatoes", "Mini Vegetable Spring Rolls",
                     "Churros Sticks (without sauce)", "Wedges & Curry Sauce",
                     "Noodle Bowl with Spring Rolls & Katsu Sauce", "Caramel Drizzle Chicken",
                     "Salt 'n' Pepper Chicken", "Sweet & Sour Chicken", "BBQ Chicken", "Lemon Chicken TRIAL",
                     "Katsu Chicken Curry", "Sweet Chilli Prawns", "Salt N Pepper Spicy Wings", "Prawn Crackers",
                     "Duck Spring Rolls", "Chicken Balls - large & mini",
                     "Noodle Bowl with Spicy Chicken Wings & Katsu Sauce"],
        "mustard": ["Red Thai Chicken Curry", "Chinese Chicken Curry", "Massaman Chicken Curry",
                    "Plant Based Beef Stirfry TRIAL", "Pumpkin Katsu Curry", "Salt & Pepper Potatoes",
                    "Mini Vegetable Spring Rolls", "Churros Sticks (without sauce)", "Wedges & Curry Sauce",
                    "Noodle Bowl with Spring Rolls & Katsu Sauce", "Caramel Drizzle Chicken", "Salt 'n' Pepper Chicken",
                    "Sweet & Sour Chicken", "BBQ Chicken", "Lemon Chicken TRIAL", "Katsu Chicken Curry",
                    "Sweet Chilli Prawns", "Salt N Pepper Spicy Wings", "Prawn Crackers", "Duck Spring Rolls",
                    "Chicken Balls - large & mini", "Noodle Bowl with Spicy Chicken Wings & Katsu Sauce",
                    "Katsu Sauce"],
        "nuts": ["Pumpkin Katsu Curry", "Salt & Pepper Potatoes", "Mini Vegetable Spring Rolls",
                 "Churros Sticks (without sauce)", "Wedges & Curry Sauce",
                 "Noodle Bowl with Spring Rolls & Katsu Sauce", "Caramel Drizzle Chicken", "Salt 'n' Pepper Chicken",
                 "Sweet & Sour Chicken", "BBQ Chicken", "Lemon Chicken TRIAL", "Katsu Chicken Curry",
                 "Sweet Chilli Prawns", "Salt N Pepper Spicy Wings", "Prawn Crackers", "Duck Spring Rolls",
                 "Chicken Balls - large & mini", "Noodle Bowl with Spicy Chicken Wings & Katsu Sauce"],
        "peanuts": [],
        "sesame seeds": ["Egg Fried Rice", "Vegetable Noodles", "Skinny Rice", "Teriyaki Beef", "Pumpkin Katsu Curry",
                         "Salt & Pepper Potatoes", "Mini Vegetable Spring Rolls", "Churros Sticks (without sauce)",
                         "Wedges & Curry Sauce", "Noodle Bowl with Spring Rolls & Katsu Sauce",
                         "Caramel Drizzle Chicken", "Salt 'n' Pepper Chicken", "Sweet & Sour Chicken", "BBQ Chicken",
                         "Lemon Chicken TRIAL", "Katsu Chicken Curry", "Sweet Chilli Prawns",
                         "Salt N Pepper Spicy Wings", "Prawn Crackers", "Duck Spring Rolls",
                         "Chicken Balls - large & mini", "Noodle Bowl with Spicy Chicken Wings & Katsu Sauce"],
        "soya": ["Egg Fried Rice", "Seasoned Rice", "Vegetable Noodles", "Skinny Rice", "Red Thai Chicken Curry",
                 "Chinese Chicken Curry", "Massaman Chicken Curry", "Teriyaki Beef", "Plant Based Beef Stirfry TRIAL",
                 "Pumpkin Katsu Curry", "Salt & Pepper Potatoes", "Mini Vegetable Spring Rolls",
                 "Churros Sticks (without sauce)", "Wedges & Curry Sauce",
                 "Noodle Bowl with Spring Rolls & Katsu Sauce", "Caramel Drizzle Chicken", "Salt 'n' Pepper Chicken",
                 "Sweet & Sour Chicken", "BBQ Chicken", "Lemon Chicken TRIAL", "Katsu Chicken Curry",
                 "Sweet Chilli Prawns", "Salt N Pepper Spicy Wings", "Prawn Crackers", "Duck Spring Rolls",
                 "Chicken Balls - large & mini", "Noodle Bowl with Spicy Chicken Wings & Katsu Sauce",
                 "Chocolate Sauce (Churros)"],
        "sulphur dioxide": ["Teriyaki Beef", "Plant Based Beef Stirfry TRIAL", "Pumpkin Katsu Curry",
                            "Plant Based Beef Stirfry TRIAL", "Pumpkin Katsu Curry", "Salt & Pepper Potatoes",
                            "Mini Vegetable Spring Rolls", "Churros Sticks (without sauce)", "Wedges & Curry Sauce",
                            "Noodle Bowl with Spring Rolls & Katsu Sauce", "Caramel Drizzle Chicken",
                            "Salt 'n' Pepper Chicken", "Sweet & Sour Chicken", "BBQ Chicken", "Lemon Chicken TRIAL",
                            "Katsu Chicken Curry", "Sweet Chilli Prawns", "Salt N Pepper Spicy Wings", "Prawn Crackers",
                            "Duck Spring Rolls", "Chicken Balls - large & mini",
                            "Noodle Bowl with Spicy Chicken Wings & Katsu Sauce"]
    },
    "tags": ["Japanese"]
}

thai_square = {
    "name": "Thai Square",
    "location": "location coordinates",
    "city": "London",
    "menu": [
        "Prawn Crackers", "Thai Square Mixed Starters (for 2 people)", "Aromatic Duck (for 2 people)", "Thai Dumplings",
        "Chicken Satay", "Salt and Pepper Squid", "Butterfly Prawns", "Duck Spring Rolls",
        "Spicy Prawn Soup (Tom Yum Goong)", "Chicken in Coconut Soup (Tom Kha Gai)", "Papaya Salad",
        "Minced Chicken Salad",
        "Stir Fried with Basil Leaves", "Stir Fried with Cashew Nuts", "Sweet and Sour", "Stir Fried with Oyster Sauce",
        "Stir Fried with Ginger", "Chilli Lamb", "Drunken Duck",
        "Tamarind Duck", "Weeping Tiger", "Grilled Pork Neck (Kor Moo Yang)",
        "Lamb Shank Panang Curry", "Green Curry", "Red Curry", "Panang Curry", "Jungle Curry", "Massaman Curry",
        "Duck Curry", "Golden Curry",
        "Chu Chi Jumbo Prawns", "Steamed Sea Bass", "Crispy Tilapia", "Spicy Seafood", "Garlic Prawns",
        "Prawns Love Scallops",
        "Pad Thai", "Pad Si-ew", "Drunken Noodles", "Thai Square Fried Rice",
        "Steamed Thai Jasmine Rice", "Brown Rice", "Egg Fried Rice", "Sticky Rice", "Coconut Rice",
        "Thai Square Noodles", "Mixed Vegetables with Garlic Sauce", "Broccoli with Garlic and Soya Sauce",
        "Mixed Vegetarian Starter (for 2 people)", "Vegetable Spring Rolls", "Corn Cakes", "Vegetable Tempura",
        "Vegetable and Tofu Satay", "Salt and Pepper Tofu", "Papaya Salad (Som Tum Jay)",
        "Mushroom in Coconut Soup (Tom Kha Hed)",
        "Tofu with Basil Leaves", "Vegetable Green Curry", "Vegetable Jungle Curry", "Sweet and Sour Tofu",
        "Tofu with Cashew Nuts", "Tofu with Ginger", "Spicy Aubergine", "Vegetarian Pad Thai"
    ],
    "ratings": ["3.6"],
    "allergens": {
        "celery": ["Sweet and Sour", "Pad Thai", "Sweet and Sour Tofu", "Vegetarian Pad Thai"],
        "cereals": ["Thai Square Mixed Starters (for 2 people)", "Aromatic Duck (for 2 people)", "Thai Dumplings",
                    "Salt and Pepper Squid", "Butterfly Prawns", "Duck Spring Rolls", "Stir Fried with Basil Leaves",
                    "Stir Fried with Cashew Nuts", "Stir Fried with Oyster Sauce", "Stir Fried with Ginger",
                    "Chilli Lamb", "Drunken Duck", "Tamarind Duck", "Weeping Tiger", "Grilled Pork Neck (Kor Moo Yang)",
                    "Crispy Tilapia", "Spicy Seafood", "Garlic Prawns", "Prawns Love Scallops", "Pad Si-ew",
                    "Drunken Noodles", "Thai Square Fried Rice", "Thai Square Noodles",
                    "Mixed Vegetables with Garlic Sauce", "Broccoli with Garlic and Soya Sauce",
                    "Mixed Vegetarian Starter (for 2 people)", "Vegetable Spring Rolls", "Corn Cakes",
                    "Vegetable Tempura", "Sald and Pepper Tofu", "Papaya Salad (Som Tum Jay)", "Tofu with Basil Leaves",
                    "Vegetable Jungle Curry", "Tofu with Cashew Nuts", "Tofu with Ginger", "Spicy Aubergine"],
        "crustaceans": ["Prawn Crackers", "Thai Square Mixed Starters (for 2 people)", "Thai Dumplings",
                        "Butterfly Prawns", "Spicy Prawn Soup (Tom Yum Goong)", "Chicken in Coconut Soup (Tom Kha Gai)",
                        "Chilli Lamb", "Lamb Shank Panang Curry", "Green Curry", "Red Curry", "Panang Curry",
                        "Jungle Curry", "Massaman Curry", "Duck Curry", "Golden Curry", "Chu Chi Jumbo Prawns",
                        "Spicy Seafood", "Garlic Prawns", "Prawns Love Scallops", "Thai Square Fried Rice"],
        "eggs": ["Thai Square Mixed Starters (for 2 people)", "Thai Dumplings", "Salt and Pepper Squid",
                 "Butterfly Prawns", "Spicy Seafood", "Pad Thai", "Pad Si-ew", "Thai Square Fried Rice",
                 "Egg Fried Rice", "Thai Square Noodles", "Vegetarian Pad Thai"],
        "fish": ["Spicy Prawn Soup (Tom Yum Goong)", "Chicken in Coconut Soup (Tom Kha Gai)", "Papaya Salad (Som Tum)",
                 "Minced Chicken Salad (Laab Gai)", "Tamarind Duck", "Weeping Tiger",
                 "Grilled Pork Neck (Kor Moo Yang)", "Lamb Shank Panang Curry", "Green Curry", "Red Curry",
                 "Panang Curry", "Jungle Curry", "Massaman Curry", "Duck Curry", "Golden Curry", "Chu Chi Jumbo Prawns",
                 "Steamed Sea Bass", "Crispy Tilapia", "Spicy Seafood", "Pad Thai"],
        "lupin": [],
        "milk": ["Thai Square Mixed Starters (for 2 people)", "Duck Spring Rolls", "Spicy Prawn Soup (Tom Yum Goong)",
                 "Mixed Vegetarian Starter (for 2 people)", "Vegetable Spring Rolls"],
        "molluscs": ["Salt and Pepper Squid", "Stir Fried with Basil Leaves", "Stir Fried with Cashew Nuts",
                     "Stir Fried with Oyster Sauce", "Stir Fried with Ginger", "Chilli Lamb", "Drunken Duck",
                     "Weeping Tiger", "Grilled Pork Neck (Kor Moo Yang)", "Spicy Seafood", "Garlic Prawns",
                     "Prawns Love Scallops", "Pad Si-ew", "Drunken Noodles", "Thai Square Fried Rice"],
        "mustard": ["Thai Square Mixed Starters (for 2 people)", "Chicken Satay"],
        "nuts": ["Papaya Salad (Som Tum)", "Stir Fried with Cashew Nuts", "Pad Thai", "Papaya Salad (Som Tum Jay)",
                 "Tofu with Cashew Nuts", "Vegetarian Pad Thai"],
        "peanuts": ["Thai Square Mixed Starters (for 2 people)", "Chicken Satay", "Pad Thai",
                    "Mixed Vegetarian Starter (for 2 people)", "Vegetable and Tofu Satay", "Papaya Salad (Som Tum Jay)",
                    "Vegetarian Pad Thai"],
        "sesame seeds": ["Thai Square Mixed Starters (for 2 people)", "Aromatic Duck (for 2 people)", "Thai Dumplings",
                         "Duck Spring Rolls", "Stir Fried with Cashew Nuts", "Thai Square Noodles",
                         "Mixed Vegetarian Starter (for 2 people)", "Vegetable Spring Rolls", "Tofu with Cashew Nuts"],
        "soya": ["Thai Square Mixed Starters (for 2 people)", "Aromatic Duck (for 2 people)", "Thai Dumplings",
                 "Butterfly Prawns", "Duck Spring Rolls", "Stir Fried with Basil Leaves", "Stir Fried with Cashew Nuts",
                 "Stir Fried with Oyster Sauce", "Stir Fried with Ginger", "Chilli Lamb", "Drunken Duck",
                 "Tamarind Duck", "Weeping Tiger", "Grilled Pork Neck (Kor Moo Yang)", "Spicy Seafood", "Garlic Prawns",
                 "Prawns Love Scallops", "Pad Thai", "Pad Si-ew", "Drunken Noodles", "Thai Square Fried Rice",
                 "Thai Square Noodles", "Mixed Vegetables with Garlic Sauce", "Broccoli with Garlic and Soya Sauce",
                 "Mixed Vegetarian Starter (for 2 people)", "Vegetable Spring Rolls", "Vegetable and Tofu Satay",
                 "Salt and Pepper Tofu", "Papaya Salad (Som Tum Jay)", "Tofu with Basil Leaves",
                 "Vegetable Green Curry", "Vegetable Jungle Curry", "Sweet and Sour Tofu", "Tofu with Cashew Nuts",
                 "Tofu with Ginger", "Spicy Aubergine", "Vegetarian Pad Thai"],
        "sulphur dioxide": [],
    },
    "tags": ["Thai"]
}

comptoir_libanais = {
    "name": "Comptoir Libanais",
    "location": "location coordinates",
    "city": "London",
    "menu": [
        "Selection of Pickes", "Marinated Mixed Olives", "Warm Za'atar & Garlic Flatbread",
        "Mezze Platter", "Lentil Soup", "Hommos", "Tony's Hommos", "Baba Ghanuj", "Batata Harra", "Cheese Samboussek",
        "Falafel", "Halloumi & Tomato", "Lamb Kibbeh", "Tabbouleh", "Fattoush", "Whipped Feta Dip",
        "Halloumi & Roasted Figs",
        "Mama Zohra Salad", "Falafel Salad", "The Wedge Salad", "Summer Salad",
        "Chicken Wrap", "Falafel Wrap", "Lamb Kofta Wrap", "Chicken Taouk Plate", "Lamb Kofta Plate", "Falafel Plate",
        "Vanilla Ice-cream",
        "Chocolate Brownie", "Mango & Vanilla Cheesecake", "Orange Blossom Mouhalabia", "Baklawa Sandwich",
        "Comptoir Sundae",
        "Hadath", "Bokaj", "Pistachio", "Assabee", "Kolwashkur",
        "Falafel", "Lamb Kofta", "Chicken Taouk", "Halloumi",
        "Spiced Lamb Kofta", "Spced Chicken Kofta", "Marinated Chicken Taouk",
        "Mixed Grill", "Sea Bass Sayadiyah", "Lamb Kofta Roll", "Steak Skewer", "Spinach & Feta Borek",
        "Aubergine & Chickpea Tagine", "Lamb Kofta Tagine", "Chicken & Green Olive Tagine",
        "Warm Flatbread", "Vermicelli Rice", "Steamed Couscous", "Jewelled Couscous", "Quinoa", "Garlic Sauce",
        "Mint Yoghurt Sauce", "Tahina Sauce", "Harissa Sauce", "Fries",
        "Teas with Cow Milk", "Teas with Soya Milk", "Teas with Almond", "Hot Chocolate with Cow Milk",
        "Hot Chocolate with Soya Milk", "Hot Chocolate with Almond Milk", "Americano with Cow Milk",
        "Americano with Soya Milk", "Americano with Almond Milk", "Cappuccino with Cow Milk",
        "Cappuccino with Soya Milk", "Cappuccino with Almond Milk", "Latte with Cow Milk", "Latte with Soya Milk",
        "Latte with Almond Milk", "Flat White with Cow Milk", "Flat White with Soya Milk",
        "Flat White with Almond Milk", "Mocha with Cow Milk", "Mocha with Soya Milk", "Mocha with Almond Milk",
        "Espresso with Cow Milk", "Espresso with Soya Milk", "Espresson with Almond Milk", "Macchiato with Cow Milk",
        "Macchiato with Soya Milk", "Macchiato with Almond Milk", "Lebanese Coffee with Cow Milk",
        "Lebanese Coffee with Soya Milk", "Lebanese Coffee with Almond Milk",
        "Lebanese Spiced Hot Chocolate with Cow Milk", "Lebanese Spiced Hot Chocolate with Soya Milk",
        "Lebanese Spiced Hot Chocolate with Almond Milk"
    ],
    "ratings": ["4.0"],
    "allergens": {
        "celery": [],
        "cereals": ["Warm Za'atar & Garlic Flatbread", "Mezze Platter", "Lentil Soup", "Hommos", "Tony's Hommos",
                    "Baba Ghanuj", "Batata Harra", "Cheese Samboussek", "Falafel", "Lamb Kibbeh", "Fattoush",
                    "Whipped Feta Dip", "Mama Zohra Salad", "Falafel Salad", "The Wedge Salad", "Chicken Wrap",
                    "Falafel Wrap", "Lamb Kofta Wrap", "Chicken Taouk Plate", "Lamb Kofta Plate", "Falafel Plate",
                    "Vanilla Ice-cream", "Chocolate Brownie", "Mango & Vanilla Cheesecake", "Baklawa Sandwich",
                    "Comptoir Sundae", "Hadath", "Bokaj", "Pistachio", "Assabee", "Kolwashkur", "Falafel", "Lamb Kofta",
                    "Chicken Taouk", "Halloumi", "Sea Bass Sayadiyah", "Lamb Kofta Roll", "Steak Skewer",
                    "Spinach & Feta Borek", "Aubergine & Chickpea Tagine", "Lamb Kofta Tagine",
                    "Chicken & Green Olive Tagine", "Warm Flatbrread", "Vermicelli Rice", "Steamed Couscous",
                    "Jewelled Couscous", "Fries"],
        "crustaceans": [],
        "eggs": ["Mezze Platter", "Tony's Hommos", "Batata Harra", "Cheese Samboussek", "Falafel", "Lamb Kibbeh",
                 "Falafel Salad", "Chicken Wrap", "Falafel Wrap", "Lamb Kofta Wrap", "Chicken Taouk Plate",
                 "Lamb Kofta Plate", "Falafel Plate", "Vanilla Ice-cream", "Chocolate Brownie", "Baklawa Sandwich",
                 "Comptoir Sundae", "Falafel", "Sea Bass Sayadiyah", "Lamb Kofta Roll", "Steak Skewer",
                 "Spinach & Feta Borek", "Jewelled Couscous", "Fries"],
        "fish": ["Sea Bass Sayadiyah"],
        "lupin": ["Warm Za'atar & Garlic Flatbread", "Mezze Platter", "Lentil Soup", "Hommos", "Tony's Hommos",
                  "Baba Ghanuj", "Whipped Feta Dip", "Warm Flatbread"],
        "milk": ["Mezze Platter", "Tony's Hommos", "Batata Harra", "Cheese Samboussek", "Falafel", "Halloumi & Tomato",
                 "Lamb Kibbeh", "Whipped Feta Dip", "Halloumi & Roasted Figs", "Mama Zohra Salad", "Falafel Salad",
                 "Summer Salad", "Chicken Wrap", "Falafel Wrap", "Lamb Kofta Wrap", "Chicken Taouk Plate",
                 "Lamb Kofta Plate", "Falafel Plate", "Vanilla Ice-cream", "Chocolate Brownie",
                 "Mango & Vanilla Cheesecake", "Orange Blossom Mouhalabia", "Baklawa Sandwich", "Comptoir Sundae",
                 "Hadath", "Bokaj", "Pistachio", "Assabee", "Kolwashkur", "Falafel", "Halloumi", "Sea Bass Sayadiyah",
                 "Lamb Kofta Roll", "Steak Skewer", "Spinach & Feta Borek", "Lamb Kofta Tagine", "Jewelled Couscous",
                 "Mint Yoghurt Sauce", "Fries", "Teas with Cow Milk", "Hot Chocolate with Cow Milk",
                 "Americano with Cow Milk", "Cappuccino with Cow Milk", "Latte with Cow Milk",
                 "Flat White with Cow Milk", "Mocha with Cow Milk", "Expresso with Cow Milk", "Macchiato with Cow Milk",
                 "Lebanese Coffee with Cow Milk", "Lebanese Spiced Hot Chocolate with Cow Milk"],
        "molluscs": [],
        "mustard": ["Warm Za'atar & Garlic Flatboard", "Mezze Platter", "Lentil Soup", "Hommos", "Tony's Hommos",
                    "Baba Ghanuj", "Whipped Feta Dip", "Warm Flatbread"],
        "nuts": ["Halloumi & Roasted Figs", "Summer Salad", "Chocolate Brownie", "Mango & Vanilla Cheesecake",
                 "Baklawa Sandwich", "Comptoir Sundae", "Hadath", "Bokaj", "Pistachio", "Assabee", "Kolwashkur",
                 "Teas with Almond", "Hot Chocolate with Almond Milk", "Americano with Almond Milk",
                 "Cappuccino with Almond Milk", "Latte with Almond Milk", "Flat White with Almond Milk",
                 "Mocha with Almond Milk", "Espresso with Almond Milk", "Macchiato with Almond Milk",
                 "Lebanese Coffee with Almond Milk", "Lebanese Spiced Hot Chocolate with Cow Milk",
                 "Lebanese Spiced Hot Chocolate with Soya Milk", "Lebanese Spiced Hot Chocolate with Almond Milk"],
        "peanuts": [],
        "sesame seeds": ["Warm Za'atar & Garlic Flatbread", "Mezze Platter", "Lentil Soup", "Hommos", "Tony's Hommos",
                         "Baba Ghanuj", "Batata Harra", "Cheese Samboussek", "Falafel", "Lamb Kibbeh",
                         "Whipped Feta Dip", "Halloumi & Roated Figs", "Mama Zohra Salad", "Falafel Salad",
                         "The Wedge Salad", "Summer Salad", "Chicken Wrap", "Falafel Wrap", "Lamb Kofta Wrap",
                         "Chicken Taouk Plate", "Lamb Kofta Plate", "Falafel Plate", "Chocolate Brownie",
                         "Orange Blossom Mouhalabia", "Baklawa Sandwich", "Comptoir Sundae", "Falafel", "Lamb Kofta",
                         "Chicken Taouk", "Halloumi", "Spiced Lamb Kofta", "Spiced Chicken Kofta",
                         "Marinated Chicken Taouk", "Mixed Grill", "Sea Bass Sayadiyah", "Lamb Kofta Roll",
                         "Steak Skewer", "Spinach & Feta Borek", "Warm Flatbread", "Jewelled Couscous", "Garlic Sauce",
                         "Tahina Sauce", "Harissa Sauce", "Fries", "Lebanese Spiced Hot Chocolate with Cow Milk",
                         "Lebanese Spiced Hot Chocolate with Soya Milk",
                         "Lebanese Spiced Hot Chocolate with Almond Milk"],
        "soya": ["Warm Za'atar & Garlic Flatbread", "Mezze Platter", "Lentil Soup", "Hommos", "Tony's Hommos",
                 "Baba Ghanuj", "Whipped Feta Dip", "Chocolate Brownie", "Comptoir Sundae", "Lamb Kofta Roll",
                 "Warm Flatbread", "Teas with Soya Milk", "Hot Chocolate with Soya Milk", "Americano with Soya Milk",
                 "Cappuccino with Soya Milk", "Latte with Soya Milk", "Flat White with Soya Milk",
                 "Mocha with Soya Milk", "Espresso with Soya Milk", "Macchiato with Sayo Milk",
                 "Lebanese Coffee with Soya Milk", "Lebanese Spiced Hot Chocolate with Soya Milk"],
        "sulphur dioxide": ["Selection of Pickes", "Mezze Platter", "Falafel", "Whipped Feta Dip",
                            "Halloumi & Roasted Figs", "Falafel Salad", "Summer Salad", "Falafel Plate",
                            "Orange Blossom Mouhalabia", "Falafel", "Lamb Kofta", "Chicken Taouk", "Halloumi",
                            "Spiced Lamb Kofta", "Spiced Chicken Kofta", "Marinated Chicken Taouk", "Mixed Grill",
                            "Lamb Kofta Roll", "Chicken & Green Olive Tagine"],
    },
    "tags": ["Greek"]
}

wasabi = {
    "name": "wasabi",
    "location": "location coordinates",
    "city": "London",
    "menu": [
        "Avocado hosomaki", "Cucumber hosomaki", "Salmon hosomaki", "Tuna hosomaki", "Inari & red pepper hosomaki",
        "California roll", "Fried prawn roll", "Salmon & mango roll", "Surumi crabmeat & cucumber roll", "Tofu roll",
        "Salmon teriyaki roll",
        "Japanese omelette nigiri", "Salmon nigiri", "Shrimp nigiri", "Tofu nigiri", "Tuna nigiri",
        "Salmon sesame gunkan", "Surumi crabmeat gunkan",
        "Chicken teriyaki onigiri", "Salmon teriyaki onigiri", "Seaweed onigiri", "Edamame & butternut squash onigiri",
        "Chicken katsu & kimchi onigiri", "Tuna & mustard onigiri",
        "Chumaki set", "Harmony set", "Mini hosomaki set", "Mixed maki set", "Rainbow set", "Salmon nigiri set",
        "Sashimi set", "Tokyo salmon set", "Mini Tokyo Salmon set", "Osaka set",
        "Wasabi special bento", "Yasai roll set", "Salmon teriyaki roll set", "Crispy ebi roll",
        "Chicken katsu roll set", "Veggie roll set", "Tofu pocket roll set",
        "Salmon hosomaki set", "Avocado hosomaki set", "Cucumber hosomaki set", "Spicy salmon roll", "Spicy yasai roll",
        "Kyoto set",
        "Chumaki set - brown rice", "Salmon nigiri set - brown rice", "Rainbow set - brown rice",
        "Yasai roll set - brown rice", "Harmony set - brown rice",
        "Chicken katsu salad", "Chirashi bowl", "Salmon teriyaki salad", "Tofu teriyaki salad",
        "Salmon Matsuri platter", "Tsudoi platter", "Yasai platter",
        "Chilli mayo sauce", "Chinese chilli sauce", "Sweet chilli sauce", "Japanese BBQ sauce", "Japanese dresing",
        "Teriyaki sauce", "Balsamic vinegar olive oil",
        "Goma dressing", "Korean chilli sauce", "Ginger sachet", "Soy sauce sachet", "Sweet soy sauce sachet",
        "Gluten free soy sachet", "Reduced salt soy sauce sachet", "Wasabi sachet",
        "Chicken gyoza tanmen", "Spicy chicken tanmen", "Salmon teriyaki tanmen", "Veg tanmen", "Chicken gyoza soumen",
        "Spicy chicken soumen", "Veg soumen", "Tofu tom yum", "Prawn tom yum",
        "Chicken tom yum", "Miso soup", "Miso sachet", "Chicken curry bento", "Chicken curry yakisoba",
        "Chicken katsu curry bento", "Chicken katsu curry yakisoba", "Chicken katsu yakisoba bento",
        "Spicy chicken bento", "Spicy chicken yakisoba", "Sweet chilli chicken bento", "Sweet chilli chicken yakisoba",
        "Tofu curry bento", "Tofu curry yakisoba", "Sweet chilli tofu bento",
        "Sweet chilli tofu yakisoba", "Chicken yakisoba", "Tofu yakisoba", "Plain yakisoba", "Pork bulgogi bento",
        "Pork bulgogi yakisoba", "Pumpkin katsu curry", "Pumpkin katsu curry yakisoba",
        "Chicken teriyaki bento", "Chicken teriyaki yakisoba", "Salmon teriyaki bento", "Salmon teriyaki yakisoba",
        "Thai green chicken curry bento", "Thai green chicken curry yakisoba",
        "Kale salad", "Soy & garlic K-Wings", "Sweet & spicy K-Wings", "Sweet chilli chicken AIR BENTO",
        "Tofu curry AIR BENTO", "Pumpkin katsu curry AIR BENTO", "Chicken katsu curry AIR BENTO",
        "Chicken curry AIR BENTO", "Chicken teriyaki yakisoba AIR BENTO", "Chicken katsu", "Pumpkin Katsu",
        "Tempura prawn", "Fried chicken gyoza", "Steamed chicken gyoza",
        "Steamed vegtable gyoza", "Chicken katsu bao bun", "Pumpkin katsu bao bun", "Rainbow pot", "Hana pot",
        "Wabi wrap", "Sabi wrap", "Mango & yogurt", "Berry & yogurt",
        "Chicken gyoza salad", "Chicken katsu salad", "Chicken yakisoba salad", "Chilli noodle salad",
        "Chukka wakame salad", "Surimi crabmeat salad", "Wasabi house salad",
        "Wasabi superfood salad", "King prawn and broccoli salad", "Sweet chilli chicken", "Mixed salad leaves",
        "Salmon poke potto", "Sweet chilli chicken potto",
        "Chirashi potto", "Spicy chirashi potto", "Salmon teriyaki potto", "Edamame potto",
        "Ebi & chicken summer roll salad", "Raw naked tofu salad", "Yasai summer roll set",
        "Original bubble tea", "Green apple bubble tea", "Lychee & rose bubble tea", "Matcha bubble tea",
        "Thai milk bubble tea", "Taro bubble tea", ],
    "ratings": ["3.55"],
    "allergens": {
        "celery": ["Surimi crabmeat salad", ],
        "cereals": ["Inari & red pepper hosomaki", "California roll", "Fried prawn roll", "Salmon & mango roll",
                    "Surumi crabmeat & cucumber roll", "Tofu roll", "Salmon teriyaki roll",
                    "Tofu nigiri", "Surumi crabmeat gunkan", "Chicken teriyaki onigiri", "Salmon teriyaki onigiri",
                    "Seaweed onigiri", "Chicken katsu & kimchi onigiri",
                    "Tuna & mustard onigiri", "Chumaki set", "Harmony set", "Mini hosomaki set", "Mixed maki set",
                    "Rainbow set", "Salmon nigiri set", "Sashimi set", "Tokyo salmon set",
                    "Mini Tokyo Salmon set", "Osaka set", "Wasabi special bento", "Yasai roll set",
                    "Salmon teriyaki roll set", "Crispy ebi roll", "Chicken katsu roll set", "Veggie roll set",
                    "Tofu pocket roll set", "Salmon hosomaki set", "Avocado hosomaki set", "Cucumber hosomaki set",
                    "Spicy salmon roll", "Spicy yasai roll", "Kyoto set",
                    "Chumaki set - brown rice", "Salmon nigiri set - brown rice", "Rainbow set - brown rice",
                    "Yasai roll set - brown rice", "Harmony set - brown rice", "Chicken katsu salad",
                    "Chirashi bowl", "Salmon teriyaki salad", "Tofu teriyaki salad", "Salmon Matsuri platter",
                    "Tsudoi platter", "Yasai platter", "Chilli mayo sauce", "Chinese chilli sauce",
                    "Sweet chilli sauce", "Japanese BBQ sauce", "Japanese dresing", "Teriyaki sauce",
                    "Balsamic vinegar olive oil", "Goma dressing", "Korean chilli sauce", "Ginger sachet",
                    "Soy sauce sachet", "Sweet soy sauce sachet", "Gluten free soy sachet",
                    "Reduced salt soy sauce sachet", "Wasabi sachet""Japanese dresing", "Teriyaki sauce",
                    "Goma dressing",
                    "Korean chilli sauce", "Soy sauce sachet", "Sweet soy sauce sachet",
                    "Reduced salt soy sauce sachet", "Chicken gyoza tanmen", "Spicy chicken tanmen",
                    "Salmon teriyaki tanmen",
                    "Veg tanmen", "Chicken gyoza soumen", "Spicy chicken soumen", "Veg soumen", "Tofu tom yum",
                    "Prawn tom yum", "Chicken tom yum", "Miso soup", "Miso sachet",
                    "Chicken curry bento", "Chicken curry yakisoba", "Chicken katsu curry bento",
                    "Chicken katsu curry yakisoba", "Chicken katsu yakisoba bento", "Spicy chicken bento",
                    "Spicy chicken bento", "Spicy chicken yakisoba", "Sweet chilli chicken bento",
                    "Sweet chilli chicken yakisoba", "Tofu curry bento", "Tofu curry yakisoba",
                    "Sweet chilli tofu bento",
                    "Sweet chilli tofu yakisoba", "Chicken yakisoba", "Tofu yakisoba", "Plain yakisoba",
                    "Pork bulgogi bento", "Pork bulgogi yakisoba", "Pumpkin katsu curry",
                    "Pumpkin katsu curry yakisoba",
                    "Chicken teriyaki bento", "Chicken teriyaki yakisoba", "Salmon teriyaki bento",
                    "Salmon teriyaki yakisoba", "Thai green chicken curry yakisoba", "Soy & garlic K-Wings",
                    "Sweet & spicy K-Wings", "Sweet chilli chicken AIR BENTO", "Tofu curry AIR BENTO",
                    "Pumpkin katsu curry AIR BENTO", "Chicken katsu curry AIR BENTO", "Chicken curry AIR BENTO",
                    "Chicken teriyaki yakisoba AIR BENTO", "Chicken katsu", "Pumpkin Katsu", "Tempura prawn",
                    "Fried chicken gyoza", "Steamed chicken gyoza", "Steamed vegtable gyoza",
                    "Chicken katsu bao bun", "Pumpkin katsu bao bun", "Hana pot", "Wabi wrap", "Sabi wrap",
                    "Chicken gyoza salad", "Chicken katsu salad", "Chicken yakisoba salad",
                    "Chukka wakame salad", "Surimi crabmeat salad", "Sweet chilli chicken", "Salmon poke potto",
                    "Sweet chilli chicken potto", "Chirashi potto", "Spicy chirashi potto",
                    "Salmon teriyaki potto", "Ebi & chicken summer roll salad", "Raw naked tofu salad",
                    "Yasai summer roll set", ],
        "crustaceans": ["California roll", "Fried prawn roll", "Surumi crabmeat & cucumber roll", "Shrimp nigiri",
                        "Surumi crabmeat gunkan",
                        "Chicken katsu & kimchi onigiri", "Chumaki set", "Harmony set", "Mixed maki set", "Rainbow set",
                        "Osaka set", "Crispy ebi roll",
                        "Wasabi special bento", "Kyoto set", "Chumaki set - brown rice", "Rainbow set - brown rice",
                        "Harmony set - brown rice", "Chirashi bowl",
                        "Tsudoi platter", "Prawn tom yum", "Thai green chicken curry bento",
                        "Thai green chicken curry yakisoba", "Tempura prawn", "Surimi crabmeat salad",
                        "King prawn and broccoli salad", "Chirashi potto", "Spicy chirashi potto",
                        "Ebi & chicken summer roll salad", "Raw naked tofu salad", ],
        "eggs": ["California roll", "Fried prawn roll", "Surumi crabmeat & cucumber roll", "Japanese omelette nigiri",
                 "Surumi crabmeat gunkan",
                 "Tuna & mustard onigiri", "Chumaki set", "Harmony set", "Mixed maki set", "Rainbow set", "Osaka set",
                 "Crispy ebi roll", "Wasabi special bento",
                 "Kyoto set", "Chumaki set - brown rice", "Rainbow set - brown rice", "Harmony set - brown rice",
                 "Chicken katsu salad", "Chirashi bowl",
                 "Tsudoi platter", "Chilli mayo sauce", "Chicken gyoza tanmen", "Spicy chicken tanmen",
                 "Chicken gyoza soumen", "Spicy chicken soumen", "Tempura prawn",
                 "Rainbow pot", "Hana pot", "Wabi wrap", "Sabi wrap", "Chicken gyoza salad", "Chilli noodle salad",
                 "Surimi crabmeat salad", "Wasabi house salad",
                 "King prawn and broccoli salad", "Chirashi potto", "Spicy chirashi potto", ],
        "fish": ["Salmon hosomaki", "Tuna hosomaki", "California roll", "Salmon & mango roll",
                 "Surumi crabmeat & cucumber roll", "Salmon teriyaki roll",
                 "Salmon nigiri", "Tuna nigiri", "Salmon sesame gunkan", "Surumi crabmeat gunkan",
                 "Tuna & mustard onigiri", "Chicken katsu & kimchi onigiri",
                 "Salmon teriyaki onigiri",
                 "Chumaki set", "Harmony set", "Mini hosomaki set", "Mixed maki set", "Rainbow set",
                 "Salmon nigiri set", "Sashimi set", "Tokyo salmon set", "Mini Tokyo Salmon set", "Osaka set",
                 "Salmon hosomaki set", "Salmon teriyaki roll set", "Wasabi special bento", "Spicy salmon roll",
                 "Kyoto set",
                 "Chumaki set - brown rice", "Salmon nigiri set - brown rice", "Rainbow set - brown rice",
                 "Harmony set - brown rice", "Chirashi bowl", "Salmon teriyaki salad",
                 "Salmon Matsuri platter", "Tsudoi platter", "Chicken gyoza tanmen", "Spicy chicken tanmen",
                 "Salmon teriyaki tanmen", "Chicken gyoza soumen", "Spicy chicken soumen",
                 "Prawn tom yum", "Chicken tom yum", "Miso soup", "Miso sachet", "Salmon teriyaki bento",
                 "Salmon teriyaki yakisoba", "Soy & garlic K-Wings", "Sweet & spicy K-Wings",
                 "Surimi crabmeat salad", "Salmon poke potto", "Chirashi potto", "Spicy chirashi potto",
                 "Salmon teriyaki potto", ],
        "lupin": [],
        "milk": ["Fried prawn roll", "Chumaki set", "Harmony set", "Mixed maki set", "Rainbow set", "Crispy ebi roll",
                 "Chumaki set - brown rice", "Rainbow set - brown rice",
                 "Harmony set - brown rice", "Tsudoi platter", "Tempura prawn", "Rainbow pot", "Hana pot", "Wabi wrap",
                 "Sabi wrap", "Mango & yogurt", "Berry & yogurt", "Chirashi potto",
                 "Spicy chirashi potto", "Ebi & chicken summer roll salad", "Raw naked tofu salad",
                 "Original bubble tea", "Matcha bubble tea", "Thai milk bubble tea", "Taro bubble tea", ],
        "molluscs": [],
        "mustard": ["Surumi crabmeat gunkan", "Tuna & mustard onigiri",
                    "Chumaki set", "Harmony set", "Mini hosomaki set", "Mixed maki set", "Rainbow set",
                    "Salmon nigiri set", "Sashimi set", "Tokyo salmon set", "Mini Tokyo Salmon set", "Osaka set",
                    "Wasabi special bento", "Yasai roll set", "Salmon teriyaki roll set", "Crispy ebi roll",
                    "Chicken katsu roll set", "Veggie roll set", "Tofu pocket roll set",
                    "Salmon hosomaki set", "Avocado hosomaki set", "Cucumber hosomaki set", "Spicy salmon roll",
                    "Spicy yasai roll", "Kyoto set",
                    "Chumaki set - brown rice", "Salmon nigiri set - brown rice", "Rainbow set - brown rice",
                    "Yasai roll set - brown rice", "Harmony set - brown rice",
                    "Chirashi bowl", "Salmon teriyaki salad", "Tofu teriyaki salad", "Salmon Matsuri platter",
                    "Tsudoi platter", "Yasai platter", "Japanese dresing", "Wasabi sachet",
                    "Chicken katsu bao bun", "Pumpkin katsu bao bun", "Surimi crabmeat salad",
                    "King prawn and broccoli salad", "Salmon poke potto", "Chirashi potto", "Spicy chirashi potto",
                    ],
        "nuts": ["Wasabi house salad", "Wasabi superfood salad", ],
        "peanuts": ["Goma dressing", "Ebi & chicken summer roll salad", "Raw naked tofu salad",
                    "Yasai summer roll set", ],
        "sesame seeds": ["California roll", "Fried prawn roll", "Salmon teriyaki roll", "Salmon sesame gunkan",
                         "Chicken katsu & kimchi onigiri",
                         "Seaweed onigiri", "Salmon teriyaki onigiri", "Chicken teriyaki onigiri", "Chumaki set",
                         "Harmony set", "Mini hosomaki set",
                         "Mixed maki set", "Rainbow set", "Salmon nigiri set", "Sashimi set", "Osaka set",
                         "Chicken katsu roll set", "Crispy ebi roll",
                         "Salmon teriyaki roll set", "Yasai roll set", "Spicy salmon roll",
                         "Chumaki set - brown rice", "Salmon nigiri set - brown rice", "Rainbow set - brown rice",
                         "Yasai roll set - brown rice", "Harmony set - brown rice",
                         "Chicken katsu salad", "Chirashi bowl", "Salmon teriyaki salad", "Tofu teriyaki salad",
                         "Tsudoi platter", "Yasai platter", "Goma dressing", "Korean chilli sauce",
                         "Chicken gyoza tanmen", "Spicy chicken tanmen", "Salmon teriyaki tanmen", "Veg tanmen",
                         "Chicken gyoza soumen", "Spicy chicken soumen", "Tofu tom yum", "Prawn tom yum",
                         "Chicken tom yum",
                         "Chicken curry yakisoba", "Chicken katsu curry yakisoba", "Chicken katsu yakisoba bento",
                         "Spicy chicken bento", "Spicy chicken yakisoba", "Sweet chilli chicken yakisoba",
                         "Tofu curry yakisoba", "Sweet chilli tofu yakisoba", "Chicken yakisoba", "Tofu yakisoba",
                         "Plain yakisoba", "Pork bulgogi bento", "Pork bulgogi yakisoba",
                         "Pumpkin katsu curry yakisoba",
                         "Chicken teriyaki bento", "Chicken teriyaki yakisoba", "Salmon teriyaki bento",
                         "Salmon teriyaki yakisoba", "Thai green chicken curry yakisoba",
                         "Chicken teriyaki yakisoba AIR BENTO",
                         "Fried chicken gyoza", "Steamed chicken gyoza", "Hana pot", "Sabi wrap", "Chicken gyoza salad",
                         "Chicken yakisoba salad", "Chukka wakame salad", "Chirashi potto",
                         "Spicy chirashi potto", "Salmon teriyaki potto", "Ebi & chicken summer roll salad",
                         "Raw naked tofu salad", "Yasai summer roll set", ],
        "soya": ["Inari & red pepper hosomaki", "California roll", "Fried prawn roll", "Salmon & mango roll",
                 "Surumi crabmeat & cucumber roll",
                 "Tofu roll", "Salmon teriyaki roll", "Tofu nigiri", "Salmon sesame gunkan", "Surumi crabmeat gunkan",
                 "Chicken katsu & kimchi onigiri",
                 "Edamame & butternut squash onigiri", "Seaweed onigiri", "Salmon teriyaki onigiri",
                 "Chicken teriyaki onigiri",
                 "Chumaki set", "Harmony set", "Mini hosomaki set", "Mixed maki set", "Rainbow set",
                 "Salmon nigiri set", "Sashimi set", "Tokyo salmon set", "Mini Tokyo Salmon set", "Osaka set",
                 "Wasabi special bento", "Yasai roll set", "Salmon teriyaki roll set", "Crispy ebi roll",
                 "Chicken katsu roll set", "Veggie roll set", "Tofu pocket roll set",
                 "Salmon hosomaki set", "Avocado hosomaki set", "Cucumber hosomaki set", "Spicy salmon roll",
                 "Spicy yasai roll", "Kyoto set",
                 "Chumaki set - brown rice", "Salmon nigiri set - brown rice", "Rainbow set - brown rice",
                 "Yasai roll set - brown rice", "Harmony set - brown rice",
                 "Chicken katsu salad", "Chirashi bowl", "Salmon teriyaki salad", "Tofu teriyaki salad",
                 "Salmon Matsuri platter", "Tsudoi platter", "Yasai platter", "Japanese dresing",
                 "Teriyaki sauce", "Goma dressing", "Korean chilli sauce", "Soy sauce sachet", "Sweet soy sauce sachet",
                 "Gluten free soy sachet", "Reduced salt soy sauce sachet",
                 "Chicken gyoza tanmen", "Spicy chicken tanmen", "Salmon teriyaki tanmen", "Veg tanmen",
                 "Chicken gyoza soumen",
                 "Spicy chicken soumen", "Veg soumen", "Tofu tom yum", "Prawn tom yum", "Chicken tom yum", "Miso soup",
                 "Miso sachet", "Chicken curry bento", "Chicken curry yakisoba",
                 "Chicken katsu curry bento", "Chicken katsu curry yakisoba", "Chicken katsu yakisoba bento",
                 "Spicy chicken bento", "Spicy chicken yakisoba", "Sweet chilli chicken bento",
                 "Sweet chilli chicken yakisoba", "Tofu curry bento", "Tofu curry yakisoba", "Sweet chilli tofu bento",
                 "Sweet chilli tofu yakisoba", "Chicken yakisoba", "Tofu yakisoba",
                 "Plain yakisoba", "Pork bulgogi bento", "Pork bulgogi yakisoba", "Pumpkin katsu curry",
                 "Pumpkin katsu curry yakisoba", "Chicken teriyaki bento", "Chicken teriyaki yakisoba",
                 "Salmon teriyaki bento", "Salmon teriyaki yakisoba", "Thai green chicken curry bento",
                 "Thai green chicken curry yakisoba", "Kale salad", "Soy & garlic K-Wings", "Sweet & spicy K-Wings",
                 "Sweet chilli chicken AIR BENTO", "Tofu curry AIR BENTO", "Pumpkin katsu curry AIR BENTO",
                 "Chicken katsu curry AIR BENTO", "Chicken curry AIR BENTO", "Chicken teriyaki yakisoba AIR BENTO",
                 "Chicken katsu", "Tempura prawn", "Fried chicken gyoza", "Steamed chicken gyoza",
                 "Steamed vegtable gyoza", "Chicken katsu bao bun", "Hana pot", "Sabi wrap", "Chicken gyoza salad",
                 "Chicken katsu salad", "Chicken yakisoba salad", "Chukka wakame salad", "Surimi crabmeat salad",
                 "Sweet chilli chicken", "Salmon poke potto", "Sweet chilli chicken potto",
                 "Chirashi potto", "Spicy chirashi potto", "Salmon teriyaki potto", "Edamame potto",
                 "Ebi & chicken summer roll salad", "Raw naked tofu salad", "Yasai summer roll set",
                 ],
        "sulphur dioxide": ["Surumi crabmeat & cucumber roll", "Surumi crabmeat gunkan",
                            "Chicken katsu & kimchi onigiri", "Chicken teriyaki onigiri",
                            "Chumaki set", "Harmony set", "Mixed maki set", "Rainbow set", "Osaka set",
                            "Wasabi special bento", "Spicy yasai roll", "Kyoto set",
                            "Chumaki set - brown rice", "Rainbow set - brown rice", "Harmony set - brown rice",
                            "Chirashi bowl", "Chinese chilli sauce", "Balsamic vinegar olive oil",
                            "Spicy chicken tanmen", "Spicy chicken soumen", "Tofu tom yum", "Chicken tom yum",
                            "Chicken curry yakisoba", "Chicken katsu curry yakisoba", "Chicken katsu yakisoba bento",
                            "Spicy chicken yakisoba", "Sweet chilli chicken yakisoba", "Tofu curry yakisoba",
                            "Sweet chilli tofu yakisoba", "Chicken yakisoba", "Tofu yakisoba", "Pork bulgogi yakisoba",
                            "Pumpkin katsu curry yakisoba", "Chicken teriyaki bento", "Chicken teriyaki yakisoba",
                            "Salmon teriyaki yakisoba", "Thai green chicken curry yakisoba",
                            "Chicken teriyaki yakisoba AIR BENTO", "Chicken katsu bao bun", "Pumpkin katsu bao bun",
                            "Chicken yakisoba salad",
                            "Surimi crabmeat salad", "Chirashi potto", "Spicy chirashi potto", ],
    },
    "tags": ["Japanese", "Sushi"]
}

fiveGuys = {
    "name": "Five Guys",
    "location": "location coordinates",
    "city": "London",
    "menu": ["Hamburger", "Cheeseburger", "Bacon Burger", "Bacon Cheeseburger", "Little Hamburger",
             "Little Cheeseburger", "Little Bacon Burger", "Little Bacon Cheeseburger",
             "All Beef Hot Dog", "Cheese Dog", "Bacon Dog", "Bacon Cheese Dog", "Veggie Sandwich",
             "Cheese Veggie Sandwich", "Grilled Cheese", "BLT", "Little Five Guys Style Fries",
             "Regular Five Guys Style Fries", "Large Five Guys Style Fries", "Little Cajun Style Fries",
             "Regular Cajun Style Fries", "Large Cajun Style Fries", "Five Guys Shake",
             "Reese's Peanut Butter Cups Shake", "Coca-Cola Original Taste",
             "Diet Coke", "Coca-Cola Zero Sugar", "Sprite", "Fanta Orange", "Dr Pepper", "Glaceau Smart Water",
             "Budweiser", "Corona", "Brooklyn Beer"],
    "ratings": ["4.80"],
    "allergens": {
        "celery": ["Little Five Guys Style Fries", "Regular Five Guys Style Fries", "Large Five Guys Style Fries",
                   "Little Cajun Style Fries", "Regular Cajun Style Fries", "Large Cajun Style Fries"],
        "cereals": ["Hamburger", "Cheeseburger", "Bacon Burger", "Bacon Cheeseburger", "Little Hamburger",
                    "Little Cheeseburger", "Little Bacon Burger", "Little Bacon Cheeseburger",
                    "All Beef Hot Dog", "Cheese Dog", "Bacon Dog", "Bacon Cheese Dog", "Veggie Sandwich",
                    "Cheese Veggie Sandwich", "Grilled Cheese", "BLT"],
        "crustaceans": [],
        "eggs": ["Hamburger", "Cheeseburger", "Bacon Burger", "Bacon Cheeseburger", "Little Hamburger",
                 "Little Cheeseburger", "Little Bacon Burger", "Little Bacon Cheeseburger",
                 "All Beef Hot Dog", "Cheese Dog", "Bacon Dog", "Bacon Cheese Dog"],
        "fish": [],
        "lupin": [],
        "milk": ["Hamburger", "Cheeseburger", "Bacon Burger", "Bacon Cheeseburger", "Little Hamburger",
                 "Little Cheeseburger", "Little Bacon Burger", "Little Bacon Cheeseburger",
                 "All Beef Hot Dog", "Cheese Dog", "Bacon Dog", "Bacon Cheese Dog", "Five Guys Shake",
                 "Reese's Peanut Butter Cups Shake"],
        "molluscs": [],
        "mustard": [],
        "nuts": ["Hamburger", "Cheeseburger", "Bacon Burger", "Bacon Cheeseburger", "Little Hamburger",
                 "Little Cheeseburger", "Little Bacon Burger", "Little Bacon Cheeseburger",
                 "All Beef Hot Dog", "Cheese Dog", "Bacon Dog", "Bacon Cheese Dog", "Reese's Peanut Butter Cups Shake"],
        "peanuts": ["Little Five Guys Style Fries", "Regular Five Guys Style Fries", "Large Five Guys Style Fries",
                    "Little Cajun Style Fries", "Regular Cajun Style Fries", "Large Cajun Style Fries",
                    "Five Guys Shake", "Reese's Peanut Butter Cups Shake"],
        "sesame seeds": ["Hamburger", "Cheeseburger", "Bacon Burger", "Bacon Cheeseburger", "Little Hamburger",
                         "Little Cheeseburger", "Little Bacon Burger", "Little Bacon Cheeseburger",
                         "All Beef Hot Dog", "Cheese Dog", "Bacon Dog", "Bacon Cheese Dog",
                         "Reese's Peanut Butter Cups Shake"],
        "soya": ["Hamburger", "Cheeseburger", "Bacon Burger", "Bacon Cheeseburger", "Little Hamburger",
                 "Little Cheeseburger", "Little Bacon Burger", "Little Bacon Cheeseburger",
                 "All Beef Hot Dog", "Cheese Dog", "Bacon Dog", "Bacon Cheese Dog", "Five Guys Shake",
                 "Reese's Peanut Butter Cups Shake"],
        "sulphur dioxide": [],
    },
    "tags": ["American", "Fast Food", "Burgers"]
}

honestBurger = {
    "name": "Honest Burger",
    "location": "location coordinates",
    "city": "London",
    "menu": ["Caribbean Fried Chicken Burger", "Plant Burger", "Beef Burger", "Cheese Burger", "Blue Cheese Burger",
             "Honest Burger", "Tribute Burger", "Chilli Burger", "Pesto Burger",
             "Buffalo Burger", "Fritter Burger", "Vegan Fritter Burger", "Vegan Teriyaki Burger", "Smashed By Honest",
             "Rosemary Salted Chips", "Buffalo Wings", "Onion Rings",
             "Dressed Green Salad", "Seasonal Coleslaw", "Vegan Chipotle Slaw", "Chicken Tenders", "Mushroom Fritters",
             "Gluten Free Bun - Order w/ burger to make it GF",
             "Honest Hot Sauce", "Chipotle Mayo",
             "Vegan Chipotle Mayo", "Vegan Bacon Ketchup", "Bacon Gravy", "Cheesy Bacon Gravy", "BBQ Honey Mustard",
             "South Kensington", "Homemade Lemonade", "Homemade Mint Lemonade",
             "Botanic Garden", "Brozen Bar Old Fashioned", "Grapefruit Spritz", "Bristol Cain & Ting", "Brighton Hugo",
             "Cambridge G&T", "Cardiff G&T", "Liverpool G&T",
             "Manchester Salford Mule", "Portabello G&T", "Jeffrey's G&T", "Pink G&T", "Espresso Martini",
             "Kings St Punch", "Portabello Spritz", "Vanilla Milkshake", "Strawberry Milkshake",
             "Aperol Spritz", "Original: Chocolate Milkshake", "Original: Salted Caramel Milkshake", "Honey I'm Home",
             "Rum Bongo", "Winter Spiced Mule", "Smashed Cheeseburger",
             "Smashed Baconburger", "Smashed Fried Chicken Burger", "Smashed Cali Burger", "Smashed BBQ Burger",
             "Smashed Chilli Burger", "Smashed Plant Burger", ],
    "ratings": ["4.50"],
    "allergens": {
        "celery": ["Caribbean Fried Chicken Burger", "Tribute Burger", "Dressed Green Salad", "Vegan Bacon Ketchup",
                   "Smashed Cali Burger", ],
        "cereals": ["Caribbean Fried Chicken Burger", "Plant Burger", "Beef Burger", "Cheese Burger",
                    "Blue Cheese Burger", "Honest Burger", "Tribute Burger", "Chilli Burger", "Pesto Burger",
                    "Buffalo Burger", "Fritter Burger", "Vegan Fritter Burger", "Vegan Teriyaki Burger",
                    "Smashed By Honest", "South Kensington", "Vanilla Milkshake", "Strawberry Milkshake",
                    "Smashed Cheeseburger", "Smashed Baconburger", "Smashed Fried Chicken Burger",
                    "Smashed Cali Burger", "Smashed BBQ Burger", "Smashed Chilli Burger", "Smashed Plant Burger", ],
        "crustaceans": [],
        "eggs": ["Caribbean Fried Chicken Burger", "Beef Burger", "Cheese Burger", "Blue Cheese Burger",
                 "Honest Burger", "Tribute Burger", "Chilli Burger", "Pesto Burger", "Buffalo Burger",
                 "Fritter Burger", "Vegan Fritter Burger", "Smashed By Honest", "Buffalo Wings", "Seasonal Coleslaw",
                 "Chicken Tenders", "Gluten Free Bun - Order w/ burger to make it GF",
                 "Chipotle Mayo", "South Kensington", "Vanilla Milkshake", "Strawberry Milkshake",
                 "Smashed Cheeseburger", "Smashed Baconburger", "Smashed Fried Chicken Burger", "Smashed Cali Burger",
                 "Smashed BBQ Burger", "Smashed Chilli Burger", ],
        "fish": ["Tribute Burger", "Buffalo Burger", "Chicken Tenders", "Smashed Cali Burger", ],
        "lupin": ["Gluten Free Bun - Order w/ burger to make it GF", ],
        "milk": ["Caribbean Fried Chicken Burger", "Beef Burger", "Cheese Burger", "Blue Cheese Burger",
                 "Honest Burger", "Tribute Burger", "Chilli Burger", "Pesto Burger", "Buffalo Burger",
                 "Fritter Burger", "Vegan Fritter Burger", "Smashed By Honest", "Buffalo Wings", "Seasonal Coleslaw",
                 "Chicken Tenders", "Gluten Free Bun - Order w/ burger to make it GF",
                 "Cheesy Bacon Gravy", "South Kensington", "Vanilla Milkshake", "Strawberry Milkshake",
                 "Original: Chocolate Milkshake", "Original: Salted Caramel Milkshake", "Smashed Cheeseburger",
                 "Smashed Baconburger", "Smashed Fried Chicken Burger", "Smashed Cali Burger", "Smashed BBQ Burger",
                 "Smashed Chilli Burger", ],
        "molluscs": [],
        "mustard": ["Caribbean Fried Chicken Burger", "Plant Burger", "Honest Burger", "Tribute Burger", "Pesto Burger",
                    "Buffalo Burger", "Fritter Burger", "Vegan Fritter Burger",
                    "Vegan Teriyaki Burger", "Smashed By Honest", "Buffalo Wings", "Dressed Green Salad",
                    "Seasonal Coleslaw", "Vegan Chipotle Slaw", "Chicken Tenders", "Mushroom Fritters",
                    "Gluten Free Bun - Order w/ burger to make it GF", "Chipotle Mayo", "Vegan Chipotle Mayo",
                    "Vegan Bacon Ketchup", "BBQ Honey Mustard", "Smashed Cheeseburger", "Smashed Baconburger",
                    "Smashed Fried Chicken Burger", "Smashed Cali Burger", "Smashed BBQ Burger",
                    "Smashed Chilli Burger", "Smashed Plant Burger"],
        "nuts": [],
        "peanuts": [],
        "sesame seeds": ["Gluten Free Bun - Order w/ burger to make it GF", ],
        "soya": ["Caribbean Fried Chicken Burger", "Plant Burger", "Beef Burger", "Cheese Burger", "Blue Cheese Burger",
                 "Honest Burger", "Tribute Burger", "Chilli Burger", "Pesto Burger", "Buffalo Burger",
                 "Fritter Burger", "Vegan Fritter Burger", "Vegan Teriyaki Burger", "Smashed By Honest", "Onion Rings",
                 "Mushroom Fritters", "Gluten Free Bun - Order w/ burger to make it GF",
                 "Vegan Bacon Ketchup", "Bacon Gravy", "Cheesy Bacon Gravy", "South Kensington", "Smashed Cheeseburger",
                 "Smashed Baconburger", "Smashed Fried Chicken Burger", "Smashed Cali Burger",
                 "Smashed BBQ Burger", "Smashed Chilli Burger", "Smashed Plant Burger", ],
        "sulphur dioxide": ["Caribbean Fried Chicken Burger", "Plant Burger", "Beef Burger", "Cheese Burger",
                            "Blue Cheese Burger", "Honest Burger", "Pesto Burger", "Buffalo Burger", "Fritter Burger",
                            "Vegan Fritter Burger", "Smashed By Honest", "Buffalo Wings", "Dressed Green Salad",
                            "Vegan Chipotle Slaw", "Mushroom Fritters", "Vegan Chipotle Mayo", "Vegan Bacon Ketchup",
                            "Bacon Gravy", "Cheesy Bacon Gravy", "Grapefruit Spritz", "Brighton Hugo",
                            "Portabello Spritz", "Aperol Spritz", "Smashed Baconburger", "Smashed Cali Burger",
                            "Smashed BBQ Burger",
                            "Smashed Plant Burger", ],
    },
    "tags": ["American", "Burgers"]
}

tapasBrindisa = {
    "name": "Tapas Brindisa",
    "location": "location coordinates",
    "city": "London",
    "menu": ["Pan de Coca con Tomate", "Aceitunas Gordales Perello", "Pimientos do Padron", "Jamon Croquetas",
             "Anchovy with onions", "Beetroot Salmorejo",
             "Sea Bream Ceviche, Apple & Radishes", "Boquerones Chilli & Parsley",
             "Squid ala Plancha Black Ink Sauce", "Leon Chorizo", "Sirloin", "Skrei Cod", "Pollo al Limon",
             "White Asparagus Gratin",
             "Octopus with saffron olive oil mash",
             "Huevos Rotos con Sobrasada", "Monte Enebro", "patatas Bravas y Alioli", "Tortilla Espanola",
             "Huevos Rotos con pisto",
             "Arroz Negro (to share)", "Lamb Shoulder", "Gambas al Ajillo", "Faba beans base",
             "Pan de la casa", "Spring salad", "Raw Cavolo salad", "Spinach Catalan", "Iberico Jamon de Bellota",
             "Tabla de Quesos", "Seleccion de Charcuteria",
             "Vanilla Ice Cream", "Coconut & Lime rice pudding", "Bitter chocolate and orange catalana", "Cheesecake"],
    "ratings": ["4.20"],
    "allergens": {
        "celery": ["Squid ala Plancha Black Ink Sauce", "Skrei Cod", "Octopus with saffron olive oil mash",
                   "Arroz Negro (to share)", "Tabla de Quesos", "Seleccion de Charcuteria", ],
        "cereals": ["Pan de Coca con Tomate", "Jamon Croquetas", "Anchovy with onions",
                    "Sea Bream Ceviche, Apple & Radishes", "Leon Chorizo", "White Asparagus Gratin",
                    "Octopus with saffron olive oil mash", "Monte Enebro",
                    "Pan de la casa", "Raw Cavolo salad", "Spinach Catalan", "Iberico Jamon de Bellota",
                    "Tabla de Quesos", "Seleccion de Charcuteria",
                    "Bitter chocolate and orange catalana", ],
        "crustaceans": ["Squid ala Plancha Black Ink Sauce", "Skrei Cod", "Octopus with saffron olive oil mash",
                        "Arroz Negro (to share)", "Gambas al Ajillo", ],
        "eggs": ["Jamon Croquetas", "White Asparagus Gratin", "Huevos Rotos con Sobrasada", "Monte Enebro",
                 "patatas Bravas y Alioli", "Tortilla Espanola", "Huevos Rotos con pisto",
                 "Arroz Negro (to share)", "Raw Cavolo salad", "Tabla de Quesos", "Vanilla Ice Cream",
                 "Bitter chocolate and orange catalana", "Cheesecake"],
        "fish": ["Aceitunas Gordales Perello", "Anchovy with onions", "Beetroot Salmorejo",
                 "Sea Bream Ceviche, Apple & Radishes", "Boquerones Chilli & Parsley",
                 "Squid ala Plancha Black Ink Sauce", "Skrei Cod", "Pollo al Limon",
                 "Octopus with saffron olive oil mash", "Arroz Negro (to share)",
                 "Gambas al Ajillo", "Raw Cavolo salad", "Seleccion de Charcuteria", ],
        "lupin": [],
        "milk": ["Jamon Croquetas", "Squid ala Plancha Black Ink Sauce", "Leon Chorizo", "Skrei Cod",
                 "White Asparagus Gratin", "Octopus with saffron olive oil mash",
                 "Monte Enebro", "Arroz Negro (to share)", "Pan de la casa", "Raw Cavolo salad", "Tabla de Quesos",
                 "Seleccion de Charcuteria",
                 "Vanilla Ice Cream", "Bitter chocolate and orange catalana", "Cheesecake"],
        "molluscs": ["Squid ala Plancha Black Ink Sauce", "Skrei Cod", "Octopus with saffron olive oil mash",
                     "Arroz Negro (to share)", ],
        "mustard": ["Sea Bream Ceviche, Apple & Radishes"],
        "nuts": ["Aceitunas Gordales Perello", "Sea Bream Ceviche, Apple & Radishes", "Pollo al Limon",
                 "White Asparagus Gratin", "Monte Enebro",
                 "Pan de la casa", "Spring salad", "Spinach Catalan", "Tabla de Quesos", "Seleccion de Charcuteria",
                 "Bitter chocolate and orange catalana"],
        "peanuts": ["White Asparagus Gratin", "Pan de la casa", "Spinach Catalan", ],
        "sesame seeds": ["Sea Bream Ceviche, Apple & Radishes", "Pollo al Limon", "White Asparagus Gratin",
                         "Tabla de Quesos", "Seleccion de Charcuteria", ],
        "soya": ["Octopus with saffron olive oil mash", "Tabla de Quesos", "Seleccion de Charcuteria",
                 "Coconut & Lime rice pudding", "Bitter chocolate and orange catalana"],
        "sulphur dioxide": ["Aceitunas Gordales Perello", "Anchovy with onions", "Beetroot Salmorejo",
                            "Sea Bream Ceviche, Apple & Radishes",
                            "Squid ala Plancha Black Ink Sauce", "Sirloin", "Pollo al Limon", "White Asparagus Gratin",
                            "Octopus with saffron olive oil mash",
                            "Tortilla Espanola", "Arroz Negro (to share)", "Spring salad", "Raw Cavolo salad",
                            "Spinach Catalan",
                            "Tabla de Quesos", "Seleccion de Charcuteria", "Coconut & Lime rice pudding",
                            "Bitter chocolate and orange catalana", "Cheesecake"],
    },
    "tags": ["Greek"]
}

bellaItalia = {
    "name": "Bella Italia",
    "location": "location coordinates",
    "city": "London",
    "menu": ["Green Olives", "Black Olives", "Mixed Olives", "Calamari", "Garlic Dough Balls", "Mozzarella Dough Balls", "Meatballs", "Vegan Meatballs", "King Prawns", 
             "GF King Prawns", "Mushroom Al-Forno", "GF Mushroom Al-Forno", "Tomato Bruschetta", "GF Tomato Bruschetta", "Cheese Filled Gnocchi Bites", "Garlic Flatbread",
             "Vegan Garlic Flatbread", "GF Garlic Flatbread", "Mozzarella & Garlic Flatbread", "Vegan Mozzarella & Garlic Flatbread", "GF Mozzarella & Garlic Flatbread",
             "Caramelised Onion Flatbread", "GF Caramelised Onion Flatbread", "Tomato & Basil Flatbread", "GF Tomato & Basil Flatbread", "Carbonara", "Buffalo Pomodoro", 
             "Vegan Buffalo Pomodoro", "GF Buffalo Pomodoro", "Bolognese", "Vegan Bolognese", "GF Bolognese", "Spaghetti and Meatballs", "Vegan Spaghetti and Meatballs", 
             "Pollo Cacciatore", "GF Pollo Cacciatore", "Marco Polo", "GF Marco Polo", "Gamberoni", "GF Gamberoni", "Pollo Funghi", "GF Pollo Funghi", "Spicy Sausage", 
             "Pesto Genovese", "GF Pesto Genovese", "Lasagne", "Rigatoni Pepperoni", "Four Cheese Macaroni", "Pea and Asparagus", "Mixed Seafood", "Magherita", 
             "Vegan Magherita", "GF Magherita", "Pepperoni", "Vegan Pepperoni", "GF Pepperoni", "Chicken, Ham and Mushroom", "GF Chicken, Ham and Mushroom", 
             "Vegetariana", "Vegan Vegetariana", "GF Vegetariana", "Calzone", "Formaggio", "GF Formaggio", "Meat Feast", "Vegetarian Meat Feast", "Piccante", "GF Piccante", 
             "Prosciutto Buffalo", "GF Prosciutto Buffalo", "Mushroom, Truffle and Pecorino", "GF Mushroom, Truffle and Pecorino", "Cheeseburger", "GF Cheeseburger", 
             "Grilled Chicken Burger", "GF Grilled Chicken Burger", "Chicken Milanese", "Chicken Genovese", "Sea Bass", "Chicken Caesar Salad", "GF Chicken Caesar Salad",
             "Italian Garden Salad", "Fries", "GF & Vegan Fries", "Mixed Salad", "Sweet potato Fries", "Garlic Ciabatta", "Coleslaw", "Steamed Spinach", ],
    "ratings": ["4.20"],
    "allergens": {
        "celery": ["Garlic Dough Balls", "Mozzarella Dough Balls", "Bolognese", "GF Bolognese", "Gamberoni", "GF Gamberoni", "Pollo Funghi", "Rigatoni Pepperoni", "Pea and Asparagus", 
                    "Mixed Seafood", "Vegetarian Meat Feast", ],
        "cereals": ["Calamari", "Garlic Dough Balls", "Mozzarella Dough Balls", "Meatballs", "Vegan Meatballs", "King Prawns", "Mushroom Al-Forno", "Tomato Bruschetta",  
                    "Cheese Filled Gnocchi Bites", "Garlic Flatbread", "Vegan Garlic Flatbread", "Mozzarella & Garlic Flatbread", "Vegan Mozzarella & Garlic Flatbread", 
                    "Caramelised Onion Flatbread", "Tomato & Basil Flatbread", "Carbonara", "Buffalo Pomodoro", "Vegan Buffalo Pomodoro", "Bolognese", "Vegan Bolognese", 
                    "GF Bolognese", "Spaghetti and Meatballs", "Vegan Spaghetti and Meatballs", "Pollo Cacciatore", "Marco Polo", "Gamberoni", "Spicy Sausage", "Pesto Genovese", 
                    "Lasagne", "Rigatoni Pepperoni", "Rigatoni Pepperoni", "Four Cheese Macaroni", "Pea and Asparagus", "Magherita", "Vegan Magherita", "Pepperoni", 
                    "Vegan Pepperoni", "Chicken, Ham and Mushroom", "Vegetariana", "Vegan Vegetariana", "Calzone", "Formaggio", "Meat Feast", "Vegetarian Meat Feast", "Piccante", 
                    "Prosciutto Buffalo", "Mushroom, Truffle and Pecorino", "Cheeseburger", "Grilled Chicken Burger", "Chicken Milanese", "Chicken Caesar Salad", "Fries", 
                     "Sweet potato Fries", "Garlic Ciabatta",  ],
        "crustaceans": ["Calamari", "King Prawns", "GF King Prawns", "Cheese Filled Gnocchi Bites", "Bolognese", "GF Bolognese", "Gamberoni", "GF Gamberoni", "Rigatoni Pepperoni",  
                        "Mixed Seafood", "Chicken Milanese", "Fries", "Sweet potato Fries", ],
        "eggs": ["Calamari", "Meatballs", "Vegan Meatballs", "King Prawns", "Mushroom Al-Forno", "Tomato Bruschetta", "Cheese Filled Gnocchi Bites", "Carbonara", 
                 "Bolognese", "Vegan Bolognese", "GF Bolognese", "Spaghetti and Meatballs", "Pollo Cacciatore", "GF Pollo Cacciatore", "Marco Polo", "Pollo Funghi", 
                 "Spicy Sausage", "Pesto Genovese", "GF Pesto Genovese", "Lasagne", "Rigatoni Pepperoni", "Four Cheese Macaroni", "Calzone", "Meat Feast", "Vegetarian Meat Feast", 
                 "Cheeseburger", "GF Cheeseburger", "Grilled Chicken Burger", "GF Grilled Chicken Burger", "Chicken Milanese", "Chicken Caesar Salad", "GF Chicken Caesar Salad", 
                 "Fries", "Sweet potato Fries", "Garlic Ciabatta", "Coleslaw", ],
        "fish": ["Calamari", "Cheese Filled Gnocchi Bites", "Bolognese", "GF Bolognese", "Rigatoni Pepperoni", "Chicken Milanese", "Sea Bass", "Fries", "Sweet potato Fries",   ],
        "lupin": ["Garlic Dough Balls", "Mozzarella Dough Balls", ],
        "milk": ["Calamari", "Garlic Dough Balls", "Mozzarella Dough Balls", "Meatballs", "Vegan Meatballs", "King Prawns", "GF King Prawns", "Mushroom Al-Forno", 
                 "GF Mushroom Al-Forno", "Tomato Bruschetta", "Cheese Filled Gnocchi Bites", "Garlic Flatbread", "GF Garlic Flatbread", "Mozzarella & Garlic Flatbread", 
                 "GF Mozzarella & Garlic Flatbread", "Caramelised Onion Flatbread", "GF Caramelised Onion Flatbread", "Carbonara", "Buffalo Pomodoro", "GF Buffalo Pomodoro", 
                 "Bolognese", "Vegan Bolognese", "GF Bolognese", "Spaghetti and Meatballs", "Pollo Cacciatore", "GF Pollo Cacciatore", "Marco Polo", "Gamberoni", "GF Gamberoni", 
                 "Pollo Funghi", "GF Pollo Funghi", "Spicy Sausage", "Pesto Genovese", "GF Pesto Genovese", "Lasagne", "Rigatoni Pepperoni", "Four Cheese Macaroni", "Mixed Seafood", 
                 "Magherita", "GF Magherita", "Pepperoni", "GF Pepperoni", "Chicken, Ham and Mushroom", "GF Chicken, Ham and Mushroom", "Vegetariana", "GF Vegetariana", "Calzone", 
                 "Formaggio", "GF Formaggio", "Meat Feast", "Vegetarian Meat Feast", "Piccante", "GF Piccante", "Prosciutto Buffalo",  "GF Prosciutto Buffalo", "Mushroom, Truffle and Pecorino", 
                 "GF Mushroom, Truffle and Pecorino", "Cheeseburger", "GF Cheeseburger", "Grilled Chicken Burger", "GF Grilled Chicken Burger", "Chicken Milanese", "Chicken Genovese", 
                 "Chicken Caesar Salad", "GF Chicken Caesar Salad", "Fries", "Sweet potato Fries", "Garlic Ciabatta", ],
        "molluscs": ["Calamari", "Cheese Filled Gnocchi Bites", "Bolognese", "GF Bolognese", "Rigatoni Pepperoni", "Mixed Seafood", "Chicken Milanese", "Fries", "Sweet potato Fries", 
                      ],
        "mustard": ["Calamari", "Cheese Filled Gnocchi Bites", "Carbonara", "Buffalo Pomodoro", "Vegan Buffalo Pomodoro", "Bolognese", "Vegan Bolognese", "GF Bolognese", 
                    "Spaghetti and Meatballs", "Vegan Spaghetti and Meatballs", "Pollo Cacciatore", "Marco Polo", "Gamberoni", "Rigatoni Pepperoni", "Vegetarian Meat Feast", 
                    "Chicken Milanese", "Chicken Caesar Salad", "GF Chicken Caesar Salad", "Fries", "Sweet potato Fries", ],
        "nuts": ["Garlic Dough Balls", "Mozzarella Dough Balls", "Meatballs", "Vegan Meatballs", "King Prawns", "Mushroom Al-Forno", "Tomato Bruschetta", "Bolognese", 
                 "Vegan Bolognese", "GF Bolognese", "Rigatoni Pepperoni", "Four Cheese Macaroni", "Cheeseburger", "Grilled Chicken Burger", "Chicken Milanese",  
                 "Chicken Caesar Salad", "Garlic Ciabatta", ],
        "peanuts": ["Garlic Dough Balls", "Mozzarella Dough Balls", "Meatballs", "Vegan Meatballs", "King Prawns", "Mushroom Al-Forno", "Tomato Bruschetta", "Vegan Bolognese", 
                    "Four Cheese Macaroni", "Chicken Milanese", "Chicken Caesar Salad", "Garlic Ciabatta", ],
        "sesame seeds": ["Garlic Dough Balls", "Mozzarella Dough Balls", "Meatballs", "Vegan Meatballs", "King Prawns", "Mushroom Al-Forno", "Tomato Bruschetta", 
                         "Bolognese", "GF Bolognese", "Rigatoni Pepperoni",  "Vegetarian Meat Feast", "Cheeseburger", "Grilled Chicken Burger", "Chicken Caesar Salad", 
                         "Garlic Ciabatta", ],
        "soya": ["Calamari", "Garlic Dough Balls", "Mozzarella Dough Balls", "Meatballs", "Vegan Meatballs", "King Prawns", "GF King Prawns", "Mushroom Al-Forno", 
                 "GF Mushroom Al-Forno", "Tomato Bruschetta", "GF Tomato Bruschetta", "Garlic Flatbread", "Vegan Garlic Flatbread", "GF Garlic Flatbread", "Mozzarella & Garlic Flatbread", 
                 "Vegan Mozzarella & Garlic Flatbread", "GF Mozzarella & Garlic Flatbread", "Caramelised Onion Flatbread", "GF Caramelised Onion Flatbread", "Tomato & Basil Flatbread", 
                 "GF Tomato & Basil Flatbread", "Carbonara", "Buffalo Pomodoro", "Vegan Buffalo Pomodoro", "Bolognese", "Vegan Bolognese", "GF Bolognese", "Spaghetti and Meatballs", 
                 "Vegan Spaghetti and Meatballs", "Pollo Cacciatore", "Marco Polo", "GF Marco Polo", "Gamberoni", "Pollo Funghi", "GF Pollo Funghi", "Rigatoni Pepperoni",  "Magherita",
                 "Vegan Magherita", "GF Magherita", "Pepperoni", "Vegan Pepperoni", "GF Pepperoni", "GF Chicken, Ham and Mushroom", "Vegetariana", "Vegan Vegetariana",
                 "GF Vegetariana", "Calzone", "Formaggio", "GF Formaggio", "Meat Feast", "Vegetarian Meat Feast", "Piccante", "GF Piccante", "Prosciutto Buffalo",  "GF Prosciutto Buffalo", 
                 "Mushroom, Truffle and Pecorino", "GF Mushroom, Truffle and Pecorino", "Cheeseburger", "Grilled Chicken Burger", "Chicken Milanese", "Chicken Genovese", 
                 "Chicken Caesar Salad", "GF Chicken Caesar Salad", "Garlic Ciabatta", ],
        "sulphur dioxide": ["Calamari", "Mushroom Al-Forno", "GF Mushroom Al-Forno", "Cheese Filled Gnocchi Bites", "Caramelised Onion Flatbread", "GF Caramelised Onion Flatbread", 
                            "Bolognese", "GF Bolognese", "Pollo Cacciatore", "GF Pollo Cacciatore", "Gamberoni", "GF Gamberoni", "Pollo Funghi", "GF Pollo Funghi", "Rigatoni Pepperoni", 
                            "Vegetariana", "Vegan Vegetariana", "GF Vegetariana", "Mushroom, Truffle and Pecorino", "GF Mushroom, Truffle and Pecorino", "Cheeseburger", 
                            "GF Cheeseburger", "Chicken Genovese", "Italian Garden Salad", "Mixed Salad", ],
    },
    "tags": ["Italian"],
}

francoManca = {
    "name": "Franco Manca",
    "location": [51.49266,-0.17710,17],
    "city": "London",
    "menu": ["Nocellara green olives", "Sharer platter", "Cured meats", "Sourdough pizza bread with salt & rosemary", "Garlic bread with a light tomato base", "Garlic bread with mozzarella",
             "Burrata on toasted sourdough pizza bread bites", "Buffalo mozzarella & marinated baby plum toatoes with mint bites", "Beef ragu al forno bites", "Free range spicy Yorkshire lamb sausage bites", 
             "Tuscan pork fennel sausage & buffalo mozzarella bruschetta", "Aubergine parmigiana", "Organic tomato, garlic, basil & organo pizza", "Organic tomato, garlic & basil pizza", 
             "Traditional halloumi D.O.P cheese, roasted courgettes, mozzarella & baby plum tomato pizza", "Roasted cured ham, mozzarella, ricotta & wild mushrroms pizza", 
             "Organic tomato, garlic, oregano, capers, olives, anchovies & mozzarella pizza", "Organic tomato, cured natural and Iberico chorizo & mozzarella pizza",
             "Lightly smoked beechwood spicy salami, tomato, mozzarella & onion pizza", "Slow-cooked beef ragu, tomato, mozzarella, cheese, pancetta & basil pizza",
              "Wild mushroom, burrata, truffle pesto base, mozzarella & basil pizza", "Tuscan pork fennel sausage, broccoli pesto base, mozzarella and Franco & Cantarelli Grana pizza",
              "Organic tomato, garlic, basil & organo pizza GF base", "Organic tomato, garlic & basil pizza GF base", "Traditional halloumi D.O.P cheese, roasted courgettes, mozzarella & baby plum tomato pizza GF base", 
             "Roasted cured ham, mozzarella, ricotta & wild mushrroms pizza GF base", "Organic tomato, garlic, oregano, capers, olives, anchovies & mozzarella pizza GF base", 
             "Organic tomato, cured natural and Iberico chorizo & mozzarella pizza GF base", "Lightly smoked beechwood spicy salami, tomato, mozzarella & onion pizza GF base", 
             "Slow-cooked beef ragu, tomato, mozzarella, cheese, pancetta & basil pizza GF base", "Wild mushroom, burrata, truffle pesto base, mozzarella & basil pizza GF base",
             "Tuscan pork fennel sausage, broccoli pesto base, mozzarella and Franco & Cantarelli Grana pizza GF base",
              "Seasonal pesto dip", "Garlic dip", "Spicy 'nduja dip", "Scotch bonnet chilli dip", "Colston Bassett Stilton dip", "Yellowfin tuna, plum tomato, black olive, pepper salad", 
              "Roasted butternut squash, artichoke, plum tomato, goat cheese & walnut salad", "Mixed leaves, cucumber & plum tomato side salad", "Mixed leaves, cucumber, plum tomato & black olive side salad", 
              "Affogato", "Caramel pecan cheesecake", "Chocolate & hazelnut cake with ice cream", "Homemade tiramisu", "Madagascan vanilla ice cream", "Chocolate & sea salt ice cream", 
              "Salted caramel ice cream", "Chocolate & blood orange ice cream", "Raspberry sorbet", "Lemon sorbet", "Espresso", "Macchiato", "Cappuccino", "Flat white",
               "Americano", "Fresh mint tea", "English breakfast tea", "Grappa digestif", "Limoncello digestif", "Amaro digestif", "Insolia: Tenute Normanno (wine)", "Pinot Grigio: Nativo (wine)",
               "Trebbiano: Francesco Cirelli (wine)", "Grillo: Della Mora (wine)", "Nero d'Avola: Tenute Normanno (wine)", "Nero d'Avola: Tenute Normanno (wine)", "Sangiovese: Nativo (wine)", "Montepulciano : Francesco Cirelli (wine)",
                   "Syrah: Della Mora (wine)", "Extra dry Prosecco (wine)", "Aperol spritz", "Negroni", "Negroni Sbagliato", "Gin & Tonic", "Homemade organic lemonade",
                   "Orange juice", "Apple juice", "San Pellegrino sparkling water", "Acqua Panna still water", "San Pellegrino Limonata", "San Pellegrino Aranciata",
                   "Coke", "Diet Coke", "Coke Zero"],
    "ratings": ["4.20"],
    "allergens": {
        "celery": ["Beef ragu al forno bites", "Slow-cooked beef ragu, tomato, mozzarella, cheese, pancetta & basil pizza", "Slow-cooked beef ragu, tomato, mozzarella, cheese, pancetta & basil pizza GF base",
                   ],
        "cereals": ["Sharer Platter", "Cured meats", "Sourdough pizza bread with salt & rosemary", "Garlic bread with a light tomato base", "Garlic bread with mozzarella",
                    "Burrata on toasted sourdough pizza bread bites", "Beef ragu al forno bites", "Tuscan pork fennel sausage & buffalo mozzarella bruschetta", "Organic tomato, garlic, basil & organo pizza", 
                    "Organic tomato, garlic & basil pizza", "Traditional halloumi D.O.P cheese, roasted courgettes, mozzarella & baby plum tomato pizza", "Roasted cured ham, mozzarella, ricotta & wild mushrroms pizza", 
                    "Organic tomato, garlic, oregano, capers, olives, anchovies & mozzarella pizza", "Organic tomato, cured natural and Iberico chorizo & mozzarella pizza", 
                    "Lightly smoked beechwood spicy salami, tomato, mozzarella & onion pizza", "Slow-cooked beef ragu, tomato, mozzarella, cheese, pancetta & basil pizza", 
                    "Wild mushroom, burrata, truffle pesto base, mozzarella & basil pizza", "Tuscan pork fennel sausage, broccoli pesto base, mozzarella and Franco & Cantarelli Grana pizza", 
                     "Caramel pecan cheesecake", "Chocolate & hazelnut cake with ice cream", "Homemade tiramisu", ],
        "crustaceans": [],
        "eggs": ["Sharer Platter", "Cured meats", "Beef ragu al forno bites", "Aubergine parmigiana", "Tuscan pork fennel sausage, broccoli pesto base, mozzarella and Franco & Cantarelli Grana pizza", 
                 "Seasonal pesto dip", "Mixed leaves, cucumber, plum tomato & black olive side salad", "Tuscan pork fennel sausage, broccoli pesto base, mozzarella and Franco & Cantarelli Grana pizza GF base",
                 "Caramel pecan cheesecake", "Chocolate & hazelnut cake with ice cream", "Homemade tiramisu",],
        "fish": ["Organic tomato, garlic, oregano, capers, olives, anchovies & mozzarella pizza",  "Yellowfin tuna, plum tomato, black olive, pepper salad", ],
        "lupin": ["Nocellara green olives", ],
        "milk": ["Sharer Platter", "Cured meats", "Garlic bread with mozzarella", "Burrata on toasted sourdough pizza bread bites",  "Buffalo mozzarella & marinated baby plum toatoes with mint bites", 
                 "Beef ragu al forno bites", "Free range spicy Yorkshire lamb sausage bites", "Tuscan pork fennel sausage & buffalo mozzarella bruschetta", "Aubergine parmigiana", "Traditional halloumi D.O.P cheese, roasted courgettes, mozzarella & baby plum tomato pizza", 
                 "Roasted cured ham, mozzarella, ricotta & wild mushrroms pizza", "Organic tomato, garlic, oregano, capers, olives, anchovies & mozzarella pizza", 
                 "Organic tomato, cured natural and Iberico chorizo & mozzarella pizza", "Lightly smoked beechwood spicy salami, tomato, mozzarella & onion pizza",
                 "Slow-cooked beef ragu, tomato, mozzarella, cheese, pancetta & basil pizza", "Wild mushroom, burrata, truffle pesto base, mozzarella & basil pizza",
                 "Tuscan pork fennel sausage, broccoli pesto base, mozzarella and Franco & Cantarelli Grana pizza", "Seasonal pesto dip", "Colston Bassett Stilton dip", 
                 "Yellowfin tuna, plum tomato, black olive, pepper salad", "Roasted butternut squash, artichoke, plum tomato, goat cheese & walnut salad", "Mixed leaves, cucumber, plum tomato & black olive side salad", 
                 "Organic tomato, garlic & basil pizza GF base", "Traditional halloumi D.O.P cheese, roasted courgettes, mozzarella & baby plum tomato pizza GF base", "Roasted cured ham, mozzarella, ricotta & wild mushrroms pizza GF base", 
                 "Organic tomato, garlic, oregano, capers, olives, anchovies & mozzarella pizza GF base", "Organic tomato, cured natural and Iberico chorizo & mozzarella pizza GF base",
                 "Lightly smoked beechwood spicy salami, tomato, mozzarella & onion pizza GF base", "Slow-cooked beef ragu, tomato, mozzarella, cheese, pancetta & basil pizza GF base",
                 "Wild mushroom, burrata, truffle pesto base, mozzarella & basil pizza GF base", "Tuscan pork fennel sausage, broccoli pesto base, mozzarella and Franco & Cantarelli Grana pizza GF base",
                 "Affogato", "Caramel pecan cheesecake", "Chocolate & hazelnut cake with ice cream", "Homemade tiramisu", "Madagascan vanilla ice cream", "Chocolate & sea salt ice cream",
                 "Macchiato", "Cappuccino", "Flat white", ],
        "molluscs": [],
        "mustard": ["Sharer Platter", "Cured meats", "Sourdough pizza bread with salt & rosemary", "Garlic bread with a light tomato base", "Garlic bread with mozzarella", 
                    "Burrata on toasted sourdough pizza bread bites", "Beef ragu al forno bites", "Tuscan pork fennel sausage & buffalo mozzarella bruschetta", "Organic tomato, garlic, basil & organo pizza", 
                    "Organic tomato, garlic & basil pizza", "Traditional halloumi D.O.P cheese, roasted courgettes, mozzarella & baby plum tomato pizza", "Roasted cured ham, mozzarella, ricotta & wild mushrroms pizza", 
                    "Organic tomato, garlic, oregano, capers, olives, anchovies & mozzarella pizza", "Organic tomato, cured natural and Iberico chorizo & mozzarella pizza", 
                    "Lightly smoked beechwood spicy salami, tomato, mozzarella & onion pizza", "Slow-cooked beef ragu, tomato, mozzarella, cheese, pancetta & basil pizza", 
                    "Wild mushroom, burrata, truffle pesto base, mozzarella & basil pizza", "Tuscan pork fennel sausage, broccoli pesto base, mozzarella and Franco & Cantarelli Grana pizza", 
                     "Yellowfin tuna, plum tomato, black olive, pepper salad", "Roasted butternut squash, artichoke, plum tomato, goat cheese & walnut salad", "Mixed leaves, cucumber & plum tomato side salad", 
                     "Mixed leaves, cucumber, plum tomato & black olive side salad", "Organic tomato, garlic, basil & organo pizza GF base", "Organic tomato, garlic & basil pizza GF base", 
                     "Traditional halloumi D.O.P cheese, roasted courgettes, mozzarella & baby plum tomato pizza GF base", "Roasted cured ham, mozzarella, ricotta & wild mushrroms pizza GF base", 
                     "Organic tomato, garlic, oregano, capers, olives, anchovies & mozzarella pizza GF base", "Organic tomato, cured natural and Iberico chorizo & mozzarella pizza GF base",
                     "Lightly smoked beechwood spicy salami, tomato, mozzarella & onion pizza GF base", "Slow-cooked beef ragu, tomato, mozzarella, cheese, pancetta & basil pizza GF base",
                     "Wild mushroom, burrata, truffle pesto base, mozzarella & basil pizza GF base", "Tuscan pork fennel sausage, broccoli pesto base, mozzarella and Franco & Cantarelli Grana pizza GF base",
                     ],
        "nuts": ["Seasonal pesto dip", "Roasted butternut squash, artichoke, plum tomato, goat cheese & walnut salad", "Mixed leaves, cucumber & plum tomato side salad",
                  "Mixed leaves, cucumber, plum tomato & black olive side salad", "Caramel pecan cheesecake", "Chocolate & hazelnut cake with ice cream", "Homemade tiramisu",
                  ],
        "peanuts": ["Caramel pecan cheesecake", "Chocolate & hazelnut cake with ice cream",],
        "sesame seeds": ["Roasted butternut squash, artichoke, plum tomato, goat cheese & walnut salad", "Mixed leaves, cucumber & plum tomato side salad", "Mixed leaves, cucumber, plum tomato & black olive side salad", 
                         "Caramel pecan cheesecake", ],
        "soya": ["Sharer Platter", "Cured meats", "Sourdough pizza bread with salt & rosemary", "Garlic bread with a light tomato base", "Garlic bread with mozzarella", 
                 "Burrata on toasted sourdough pizza bread bites", "Beef ragu al forno bites", "Tuscan pork fennel sausage & buffalo mozzarella bruschetta", "Organic tomato, garlic, basil & organo pizza", 
                 "Organic tomato, garlic & basil pizza", "Traditional halloumi D.O.P cheese, roasted courgettes, mozzarella & baby plum tomato pizza", "Roasted cured ham, mozzarella, ricotta & wild mushrroms pizza", 
                 "Organic tomato, garlic, oregano, capers, olives, anchovies & mozzarella pizza", "Organic tomato, cured natural and Iberico chorizo & mozzarella pizza", 
                 "Lightly smoked beechwood spicy salami, tomato, mozzarella & onion pizza", "Slow-cooked beef ragu, tomato, mozzarella, cheese, pancetta & basil pizza", 
                 "Wild mushroom, burrata, truffle pesto base, mozzarella & basil pizza", "Tuscan pork fennel sausage, broccoli pesto base, mozzarella and Franco & Cantarelli Grana pizza", 
                 "Roasted butternut squash, artichoke, plum tomato, goat cheese & walnut salad", "Mixed leaves, cucumber & plum tomato side salad", "Mixed leaves, cucumber, plum tomato & black olive side salad", 
                  "Organic tomato, garlic, basil & organo pizza GF base", "Organic tomato, garlic & basil pizza GF base", "Traditional halloumi D.O.P cheese, roasted courgettes, mozzarella & baby plum tomato pizza GF base", 
                  "Roasted cured ham, mozzarella, ricotta & wild mushrroms pizza GF base", "Organic tomato, garlic, oregano, capers, olives, anchovies & mozzarella pizza GF base", "Organic tomato, cured natural and Iberico chorizo & mozzarella pizza GF base",
                 "Lightly smoked beechwood spicy salami, tomato, mozzarella & onion pizza GF base", "Slow-cooked beef ragu, tomato, mozzarella, cheese, pancetta & basil pizza GF base",
                   "Wild mushroom, burrata, truffle pesto base, mozzarella & basil pizza GF base", "Tuscan pork fennel sausage, broccoli pesto base, mozzarella and Franco & Cantarelli Grana pizza GF base",
                   "Caramel pecan cheesecake", "Chocolate & hazelnut cake with ice cream", "Homemade tiramisu", ],
        "sulphur dioxide": ["Sharer Platter", "Beef ragu al forno bites", "Organic tomato, garlic, oregano, capers, olives, anchovies & mozzarella pizza", "Lightly smoked beechwood spicy salami, tomato, mozzarella & onion pizza",
                            "Slow-cooked beef ragu, tomato, mozzarella, cheese, pancetta & basil pizza", "Tuscan pork fennel sausage, broccoli pesto base, mozzarella and Franco & Cantarelli Grana pizza", 
                            "Scotch bonnet chilli dip",  "Yellowfin tuna, plum tomato, black olive, pepper salad", "Roasted butternut squash, artichoke, plum tomato, goat cheese & walnut salad", 
                            "Mixed leaves, cucumber & plum tomato side salad", "Mixed leaves, cucumber, plum tomato & black olive side salad", "Lightly smoked beechwood spicy salami, tomato, mozzarella & onion pizza GF base", 
                            "Slow-cooked beef ragu, tomato, mozzarella, cheese, pancetta & basil pizza GF base", "Tuscan pork fennel sausage, broccoli pesto base, mozzarella and Franco & Cantarelli Grana pizza GF base",
                            "Insolia: Tenute Normanno (wine)", "Pinot Grigio: Nativo (wine)", "Trebbiano: Francesco Cirelli (wine)", "Grillo: Della Mora (wine)", "Nero d'Avola: Tenute Normanno (wine)", "Nero d'Avola: Tenute Normanno (wine)", "Sangiovese: Nativo (wine)", "Montepulciano : Francesco Cirelli (wine)",
                            "Syrah: Della Mora (wine)", "Extra dry Prosecco (wine)", "Aperol spritz", "Negroni", "Negroni Sbagliato", "Gin & Tonic", ],
    },
    "tags": [],
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
    "tags": [],
}
