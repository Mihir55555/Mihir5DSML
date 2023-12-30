## 3. Develop a Flask app that uses URL parameters to display dynamic content.

from flask import Flask, redirect, url_for

app = Flask(__name__)

@app.route("/")
def welcome():
    return "welcome to my app"

@app.route("/success/<int:score>")
def success(score):
    return "The student passed in the exam and score is "+ str(score)

@app.route("/fail/<int:score>")
def fail(score):
    return "The student failed in the exam and score is "+ str(score)

@app.route("/results/<int:marks>")
def results(marks):
    result=""
    if marks<33:
        result="fail"
    else:
        result="success"
        return redirect(url_for(result,score=marks))

if __name__=="__main__":
    app.run(host="0.0.0.0", port = 5002)
