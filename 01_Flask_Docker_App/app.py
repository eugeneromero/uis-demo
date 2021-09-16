from flask import Flask
import datetime

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<h1>Hello, World!</h1>"

@app.route("/time")
def get_time():
    time = datetime.datetime.now()
    return "<h1>It is " + time.strftime("%H:%M:%S") + " on " + time.strftime("%d/%m/%Y") + "</h1>"
