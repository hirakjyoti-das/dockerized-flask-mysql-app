from flask import Flask
import os
import mysql.connector

app = Flask(__name__)

@app.route("/health")
def health():
    return {"status": "ok"}

@app.route("/db")
def db_check():
    connection = mysql.connector.connect(
        host=os.getenv("DB_HOST"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        database=os.getenv("DB_NAME")
    )
    return {"db": "connected"}

@app.route("/")
def home():
    return {"message": "Welcome to Dockerized Flask App"}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
