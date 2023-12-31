# 3.Implement OAuth2 authentication to allow users to log in using their Google or Facebook accounts.

from flask import Flask, redirect, url_for
from flask_dance.contrib.google import make_google_blueprint, google
from flask_dance.contrib.facebook import make_facebook_blueprint, facebook
from flask_dance.consumer import oauth_authorized, oauth_error

app = Flask(__name__)
app.secret_key = 'secret_key123'  # Change this to a secure secret key

# Configure Google OAuth
google_bp = make_google_blueprint(client_id='873294761826-icksskq6ic5487n6pmh34u5kior052oh.apps.googleusercontent.com',
                                   client_secret='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',
                                   redirect_to='google_login')
app.register_blueprint(google_bp, url_prefix='/google_login')


@app.route('/')
def home():
    if google.authorized:
        resp = google.get('/plus/v1/people/me')
        assert resp.ok, resp.text
        user_info = resp.json()
        return f'Hello, {user_info["displayName"]} (Google user)'


    return 'Welcome to the Flask OAuth2 Example!'

@app.route('/google_login')
def google_login():
    if not google.authorized:
        return redirect(url_for('google.login'))
    return redirect(url_for('home'))

if __name__=="__main__":
    app.run(host="0.0.0.0",port=5000)