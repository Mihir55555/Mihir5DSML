## 5. Implement user sessions in a Flask app to store and display user-specific data.

from flask import Flask ,request ,render_template ,redirect ,url_for,session

app = Flask(__name__)


app.config['SECRET_KEY'] ="abcd"
app.config['SESSION_TYPE'] = 'filesystem'

@app.route("/")
def index():
    if not session.get("name"):
        return redirect("/login")
    return render_template('index5.html')

@app.route("/login", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        session["name"] = request.form.get("name")
        return redirect("/")
    return render_template("Login.html")

@app.route("/logout")
def logout():
    session["name"] = None
    return redirect("/")

if __name__ =="__main__" :
    app.run(debug=True ,host ="0.0.0.0",port = 5003)