from flask import render_template, request
from src import app, APP_ROOT


@app.route('/')
def home():
    return render_template('index.html', title='Home')


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
