from flask import Flask
from flask import render_template
import os
import mysql.connector
app = Flask(__name__)
host="database-2.cyo3bhhkjl95.ca-central-1.rds.amazonaws.com"
try:
  mydb = mysql.connector.connect(
    host="database-2.cyo3bhhkjl95.ca-central-1.rds.amazonaws.com",
    user="admin",
    password="12345678"
  )
  mycursor = mydb.cursor()

  mycursor.execute("select version()")

  res=mycursor.fetchall()
  version=res
except:
   print("No connect to db")
   version="No_connect_to_db"

@app.route('/')
@app.route('/index')
def hello():
   return render_template("index.html",version=version,host=host)


if __name__ == "__main__":
    app.run(host='0.0.0.0')