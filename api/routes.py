from flask import render_template, request
from api.api import app #, APP_ROOT
from api.firebase import db


# @app.route("/")
# def main():
#     return render_template("index.html", title = 'Allergenius - Home')

@app.route('/filter')
def filter():
    return render_template('filter.html', title = 'Allergenius - Filter by Allergen')

@app.route('/search')
def search():
    return render_template('search.html', title = 'Allergenius - Search for Restaurant')

@app.route('/account')
def account():
    return render_template('account.html', title = 'Allergenius - Account Page')

@app.route('/friends')
def friends():
    return render_template('friends.html', title = 'Allergenius - Friends')

@app.route('/american')
def american():
    query = db.child("restaurant").child("american").get()
    return render_template('american.html', title = 'Allergenius - American', data=query)

@app.route('/calc')
def calc():
    a = int(request.args.get('a'))
    b = int(request.args.get('b'))
    return str(sum_two(a, b))


def sum_two(a, b):
    return a + b
