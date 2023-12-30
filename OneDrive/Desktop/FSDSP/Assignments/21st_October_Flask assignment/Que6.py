## 6. Build a Flask app that allows users to upload files and display them on the website.

from flask import Flask ,request ,render_template 
from flask_wtf import FlaskForm
from wtforms import FileField ,SubmitField
from werkzeug.utils import secure_filename
import os
from wtforms.validators import InputRequired

app = Flask(__name__)

app.config['SECRET_KEY'] ="abcd"
app.config['UPLOAD_FOLDER'] = 'static/file'

class uploadfile(FlaskForm):
    file = FileField("File", validators=[InputRequired()])
    submit = SubmitField("Upload file")

@app.route("/", methods=["POST", "GET"])

@app.route("/Home", methods=["POST", "GET"])
def home_page():
    form = uploadfile()
    if form.validate_on_submit():
        file = form.file.data
        file.save(os.path.join(os.path.abspath(os.path.dirname(__file__)),app.config['UPLOAD_FOLDER'],secure_filename(file.filename)))
        return "File has been uploaded."
    return render_template("index6.html",form = form)

if __name__=="__main__":
    app.run(host="0.0.0.0", port = 5004)