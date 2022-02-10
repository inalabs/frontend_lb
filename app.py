from flask import Flask
from flask import render_template
app = Flask(__name__)

@app.route('/')
def hello_world():
    message = "Welcome"
    return render_template('index.html', message=message)

@app.route('/secret')
def secret_route():
    return 'now you find it'
