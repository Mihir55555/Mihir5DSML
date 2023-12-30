## 4. Create a Flask app with a form that accepts user input and displays it.

from flask import Flask , render_template, request,url_for
import requests 

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("form4.html")

@app.route("/submit",methods =["POST" ,"GET"])
def index2():
    name =request.form['name']
    surname =request.form['surname']
    city =request.form['city']
    country =request.form['country']
    return render_template("data4.html",name = name, surname = surname , city = city , country = country)


if __name__=="__main__":
    app.run(host="0.0.0.0", port = 5001)