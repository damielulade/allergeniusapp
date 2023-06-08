from flask import Flask
from firebase import add_user, get_values, db

app = Flask(__name__, static_folder="../build", static_url_path='/')

@app.route('/')
def index():
    return app.send_static_file('index.html')

# @app.errorhandler(404)
# def not_found(e):
#     return app.send_static_file('index.html')

@app.route('/data')
def example():
    add_user({"firstName": "Brett", "lastName": "Conway", "Age": 20})
    add_user({"firstName": "Brett", "lastName": "Conroute", "Age": 20})
    add_user({"firstName": "Brett", "lastName": "Connection", "Age": 20})
    return get_values(db.child("user"))
    # assert(false)
    
if __name__ == '__main__':
    app.run(debug=True)