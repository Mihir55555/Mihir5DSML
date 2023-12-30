# 2.Create a Flask app that consumes data from external APIs and displays it to users.

from flask import Flask, render_template
import requests

app = Flask(__name__)

def get_external_data():
    url = 'https://restcountries.com/v3.1/all'
    response = requests.get(url)
    data = response.json()
    return data

@app.route('/')
def index():
    data = get_external_data()
    return render_template('index.html', data=data)

if __name__=="__main__":
    app.run(host="0.0.0.0",port=5002)
