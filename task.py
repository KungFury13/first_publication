
from flask import Flask, render_template, request, make_response
import sqlite3

DBFILE = "sqlite.db"
app = Flask(__name__)

def getemployee():
    conn = sqlite3.connect(DBFILE)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM employee")
    results = cursor.fetchall()
    conn.close()
    return results

@app.route("/")
def index():

    employee = getemployee()
    print(employee)
    return render_template("index.html", usr=employee)

if __name__ == "__main__":
    app.run()
