## 2.Build a Flask app with static HTML pages and navigate between them

from flask import Flask , render_template, request
import requests 

app = Flask(__name__)

@app.route("/Hello")
def home_page():
    return (render_template("index1.html"))

@app.route("/Second",methods=["post"])
def second():
    username=request.form["username"]
    return "username is " +username

if __name__=="__main__":
    app.run(host="0.0.0.0", port = 5003)
