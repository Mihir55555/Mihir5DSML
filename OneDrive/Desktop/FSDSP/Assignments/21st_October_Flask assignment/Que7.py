## 7. Integrate a SQLite database with Flask to perform CRUD operations on a list of items.

from flask import Flask,render_template,request
import sqlite3 as sql

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index7.html")

@app.route("/add")
def add():
    return render_template("add7.html")

@app.route("/submit",methods =["POST","GET"])
def save_detail():
    if request.method == "POST" :
        try :
            Id =request.form["Id"]
            name =request.form["name"]
            address =request.form["address"]

            with sql.connect("sql.db") as con:
                cursor =con.cursor()
                cursor.execute("INSERT INTO student(id,name,address)values(?,?,?)",(Id,name,address))
                con.commit()
                msg ="record added in database"
        except :
            
            con.rollback()
            msg ="Error in insert"
        
        finally:
            con.close()
            return render_template("success7.html",msg=msg)

@app.route("/display")
def display():
    con =sql.connect("sql.db")
    con.row_factory = sql.Row  
    cursor = con.cursor()  
    cursor.execute("SELECT * FROM student")  
    rows = cursor.fetchall()  
    return render_template("display7.html",rows = rows) 

if __name__=="__main__":
    app.run(host="0.0.0.0", port = 5003)