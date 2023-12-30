##8. Implement user authentication and registration in a Flask app using Flask-Login.

from flask import Flask, render_template, redirect, url_for, request, flash
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'  

login_manager = LoginManager(app)
login_manager.login_view = 'login'

users = {'user_id': {'username': 'username', 'password': 'password'}}

class User(UserMixin):
    pass

@login_manager.user_loader
def load_user(user_id):
    if user_id in users:
        user = User()
        user.id = user_id
        return user
    return None

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user_id = authenticate_user(username, password)

        if user_id:
            user = User()
            user.id = user_id
            login_user(user)
            flash('Login successful!', 'success')
            return redirect(url_for('dashboard'))
        else:
            flash('Invalid username or password', 'danger')

    return render_template('login8.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You have been logged out', 'info')
    return redirect(url_for('login'))

@app.route('/dashboard')
@login_required
def dashboard():
    return f'Hello, {current_user.id}! This is your dashboard.'

def authenticate_user(username, password):
    for user_id, user_data in users.items():
        if user_data['username'] == username and user_data['password'] == password:
            return user_id
    return None

if __name__ == "__main__":
    app.run(host="0.0.0.0",port = 5004)
