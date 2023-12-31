# 1.Build a Flask app that scrapes data from multiple websites and displays it on your site.

from flask import Flask, render_template
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/scrape')
def scrape():
    # Scraping YouTube data
    youtube_url = 'https://www.youtube.com'
    youtube_response = requests.get(youtube_url)
    youtube_soup = BeautifulSoup(youtube_response.text, 'html.parser')
    youtube_data = youtube_soup.title.text

    # Scraping Amazon data
    amazon_url = 'https://www.amazon.com'
    amazon_response = requests.get(amazon_url)
    amazon_soup = BeautifulSoup(amazon_response.text, 'html.parser')
    amazon_data = amazon_soup.title.text

    return render_template('scrape.html', youtube_data=youtube_data, amazon_data=amazon_data)

if __name__=="__main__":
    app.run(host="0.0.0.0",port=5003)