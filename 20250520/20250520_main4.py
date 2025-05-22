#flask 모듈
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "<h1>Hello World!</h1> <h2>My name is minwoo</h2>"