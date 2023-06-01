import pyrebase

config = {
    "apiKey": "AIzaSyBtnDvZYWimGywQYQ-vvFpU5bVz2o3dmBg",
    "authDomain": "allergenius-84e72.firebaseapp.com",
    "databaseURL": "https://allergenius-84e72-default-rtdb.europe-west1.firebasedatabase.app",
    "projectId": "allergenius-84e72",
    "storageBucket": "allergenius-84e72.appspot.com",
    "messagingSenderId": "652605483025",
    "appId": "1:652605483025:web:320cce73e5a10fb33869b0",
    "measurementId": "G-4GL14PE1B4"
}

firebase = pyrebase.initialize_app(config)
db = firebase.database()


def add_user(data):
    db.child("user").push(data)


def add_restaurant(data):
    db.child("Restaurant").push(data)


def get_values(ref, limit=10):
    for record in ref.get().each():
        print(record.val())


def delete_values(ref):
    for record in ref.get().each():
        key = record.key()
        ref.child(key).remove()


def example():
    add_user({"firstName": "Brett", "lastName": "Conway", "Age": 20})
    add_user({"firstName": "Brett", "lastName": "Conroute", "Age": 20})
    add_user({"firstName": "Brett", "lastName": "Connection", "Age": 20})

    get_values(db.child("user"))

    # delete_values(db.child("user"))
    db.child("user").remove()

example()

# data = {"Age": 21, "Name": "Brett", "Likes Pizza": True}
#
# db.push(data)
# db.child("unique branch").child("unique ID").set(data)

# records = db.child("field").get()
# for r in records.each():
#     print(r.val())
#     print(r.key())
#     if (r.val()['fieldA'] == "value1"):
#         key = r.key()
#
# db.child("field").child(key).update({"fieldB": "value2"})
# db.child("field").child(key).child("fieldB").remove()
