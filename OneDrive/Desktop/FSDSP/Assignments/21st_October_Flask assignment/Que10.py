## 10. Design a Flask app with proper error handling for 404 and 500 errors.

from flask import Flask, render_template, redirect, url_for

app = Flask(__name__)

@app.route("/")
def home():
    return "Welcome to Flask project"

@app.errorhandler(404)
def Invalid_route(e):
    return "404 Error"

@app.errorhandler(500)
def internalerror(e):
    return "500 Error"

if __name__ == '__main__':
    app.run(host ="0.0.0.0",port =5001)