from flask import Flask, render_template, request
import os
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("database")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)

class Movie(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(50), nullable = False)
db.create_all()

@app.route("/", methods = ["POST", "GET"])
def home():
    if request.method == "POST":
        form_dat = request.form
        for actt in form_dat:
            if actt == "add" and len(form_dat["add"]) != 0:
                name = form_dat["add"]
                query = Movie.query.filter_by(name = name)
                if len(list(query)) == 0:
                    movie = Movie(name = name)
                    db.session.add(movie)
            elif actt == "delete":
                act = form_dat["delete"]
                query = Movie.query.filter_by(name = act)
                for item in query:
                    db.session.delete(item)
        db.session.commit()
    movie_instances = Movie.query.all()
    movies = []
    for boxer in movie_instances:
        movies.append(boxer.name)
    return render_template("index.html", movies_list = movies, num = len(movies))
app.run(debug = True)

