from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/users/<name>")
def greetings(name):
    return "<p>Hello, %s!</p>" % name