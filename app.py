from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def main():
    return render_template("index.html")
    
@app.route('/filter')
def filter():
    return render_template('filter.html')

if __name__ == '__main__':
    app.run()



