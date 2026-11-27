from flask import Flask
import pymysql

app = Flask(__name__)

@app.route("/")
def hello_world():
    db = pymysql.connect(host="mydb", user="root", password="my-secret-pw")
    cursor = db.cursor()
    cursor.execute("SELECT VERSION()")
    version = cursor.fetchone()[0]
    db.close()
    return f"Hello World from Arte's container! MySQL version: {version}"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5002)
