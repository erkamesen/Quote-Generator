from flask import Flask, render_template, url_for, jsonify
from models import db, Quotes


app = Flask(__name__)

""" CONFIG """
app.config.from_pyfile("config.py")

db.init_app(app=app)

@app.route("/", methods = ['GET', 'POST'])
def index():
    return render_template("index.html")


@app.route("/quotes")
def quotes():
    return jsonify(Quotes.get_all_quotes())


@app.route("/random-quote")
def random_quote():
    return jsonify(Quotes.random_quote())