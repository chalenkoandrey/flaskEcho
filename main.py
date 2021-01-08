from flask import Flask
from flask import render_template
import os
import mysql.connector
app = Flask(__name__)
host=os.getenv("HOSTDB")
try:
  mydb = mysql.connector.connect(
    host=os.getenv("HOSTDB"),
    user=os.getenv("LOGIN"),
    password=os.getenv("PASSWORD")
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