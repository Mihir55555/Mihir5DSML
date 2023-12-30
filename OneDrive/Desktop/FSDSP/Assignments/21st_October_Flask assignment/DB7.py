import sqlite3

con =sqlite3.connect("sql.db")
print("Data base Opened sucessfull")
con.execute("create table student(Id int ,name Text ,address Text)")
print("table created sucess fully")
con.close()