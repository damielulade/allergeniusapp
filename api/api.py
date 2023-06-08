from flask import Flask
from flask_cors import CORS, cross_origin
from firebase import add_user, get_values, db
import json

app = Flask(__name__, static_folder="../build", static_url_path='/')
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

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
    return json.dumps(get_values(db.child("user")))
    # assert(false)
    
@app.route('/collectData', methods=["GET"])
@cross_origin()
def foo():
    return db.child("user").get().val()
    
if __name__ == '__main__':
    app.run(debug=True)