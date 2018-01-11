from flask import Flask, render_template, jsonify , g
from random import sample
import models

DEBUG = True
PORT = 8000
HOST = "0.0.0.0"

app=  Flask(__name__)

@app.before_request
def before_request():
    """Connect to the database"""
    g.db= models.DATABASE
    g.db.connect()

@app.after_request
def after_request(response):
        """Close to the database"""
        g.db.close()
        return response

@app.route('/')
def index():
    return render_template('chart.html')

@app.route("/data")
def data():
    return jsonify({"results" : sample(range(1,10),5) })
""" JSON String from vote.db"""

@app.route("/smile")
def smile():
    votes= models.Vote.select().limit(5)
    return render_template("stream.html", votes = votes)
""" Show the votes from vote.db"""

if (__name__) == "__main__":
    models.initialize()
    app.run(debug = DEBUG, host= HOST, port=PORT)
