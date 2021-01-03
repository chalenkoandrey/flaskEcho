from flask import Flask
from flask import render_template
app = Flask(__name__)
import mysql.connector

mydb = mysql.connector.connect(
  host="database-1.cepq1lphbhoy.eu-west-1.rds.amazonaws.com",
  user="admin",
  password="12345678"
)

mycursor = mydb.cursor()

mycursor.execute("select version()")

res=mycursor.fetchall()
@app.route('/')
@app.route('/index')
def hello():
   return render_template("index.html",version=res)


if __name__ == "__main__":
    app.run(host='0.0.0.0')