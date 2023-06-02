from flask import render_template, request
from src import app
from src.firebase import db


@app.route('/')
def home():
    query = db.child("user").get()
    return render_template('index.html', title='Home', data=query)


@app.route('/about')
def about():
    return render_template('about.html', title='About', name='Passed by variable')


@app.route('/user_profile/<user>')
def user_profile(user):  # put application's code here
    return render_template('user.html', title='User page', name=user)


@app.route('/calc')
def calc():
    a = int(request.args.get('a'))
    b = int(request.args.get('b'))
    return str(sum_two(a, b))


def sum_two(a, b):
    return a + b
