from flask import Flask, request

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


@app.route('/calc')
def calc():
    a = int(request.args.get('a'))
    b = int(request.args.get('b'))
    return str(sum_two(a, b))


def sum_two(a, b):
    return a + b


if __name__ == '__main__':
    app.run()
