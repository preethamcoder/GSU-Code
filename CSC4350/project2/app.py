# pylint: disable=no-member
'''This app interacts with the TMDB and Wikipedia APIS to allow user to search
and review specific movies. The image and the name of movie is displayed.'''

import os
from flask import Flask, render_template, request, redirect, flash
from flask_sqlalchemy import SQLAlchemy
import requests
from flask_login import (
    LoginManager,
    login_required,
    login_user,
    current_user,
    UserMixin,
)
from dotenv import find_dotenv, load_dotenv
from werkzeug.security import generate_password_hash, check_password_hash

load_dotenv(find_dotenv())

API_KEY = os.getenv("API_KEY")
movie_search = f"https://api.themoviedb.org/3/search/movie?api_key={API_KEY}"
param = {}
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("database")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "/"
app.secret_key = bytes(os.getenv("session_key"), "utf8")


class User(db.Model, UserMixin):
    '''Creating an instance of the user and a table with that name.'''
    __tablename__: "User"
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(150), unique=True, nullable=False)
    passwd = db.Column(db.String(350), nullable=False)

    def __repr__(self):
        return f"<{self.id}:{self.first_name}>"

    def hash_pwd(self, passw):
        '''This hashes the password, thereby encrypting it'''
        self.passwd = generate_password_hash(passw)

    def check_password(self, passw):
        '''This validates the password and returns if it is right'''
        return check_password_hash(self.passwd, passw)


class Reviews(db.Model):
    '''This creates an instance of the movie reivew and lets us create a table with that name'''
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    title = db.Column(db.String(50), nullable=False)
    user_id = db.Column(db.Integer, nullable=False)
    rating = db.Column(db.Float)
    review = db.Column(db.String(280), nullable=False)

    def __repr__(self):
        return f"<{self.movie_id}:{self.user_id}>"

    def comment(self):
        '''Returns the review from user'''
        return self.review

db.create_all()

@app.route("/")
def index():
    '''Home page with login option'''
    return render_template("login_page.html")

@login_manager.user_loader
def load_da_user(user_id):
    '''Creates an instance of the user!'''
    return db.session.query(User).get(user_id)

@app.route("/validate", methods=["POST", "GET"])
def validate_form():
    '''This method checks for authentication and other sign on errors.'''
    if request.method == "GET":
        return redirect("/")
    info = request.form
    passwd = info["password"]
    email = info["email"]
    query = User.query.filter_by(email=email)
    user = query.first()
    if user is not None and user.check_password(passwd):
        user_id = load_da_user(user.id)
        login_user(user_id)
        return redirect("/search")
    else:
        flash("Authentication error!")
        return redirect("/")


@app.route("/signup")
def signup():
    '''This function renders the sign up page.'''
    return render_template("signup.html")


@app.route("/newuser", methods=["POST", "GET"])
def adduser():
    '''This method cheks if a user exists and adds him/her if there is no account.'''
    if request.method == "POST":
        info = request.form
        e_m = info["email"]
        query = User.query.filter_by(email=e_m)
        user = query.first()
        if user is None:
            info = request.form
            pwd = info["password"]
            f_n = info["fname"]
            l_n = info["lname"]
            user = User(first_name=f_n, last_name=l_n, email=e_m)
            user.hash_pwd(pwd)
            db.session.add(user)
            db.session.commit()
            return render_template("login_page.html")
        flash(f"{user.email} is already hooked to an account!")
        return redirect("/newuser")
    return render_template("login_page.html")


@app.route("/search", methods=["POST", "GET"])
@login_required
def form():
    '''This method renders a page to let you search for movies'''
    return render_template("form.html")


@app.route("/home", methods=["POST", "GET"])
def home():
    '''This method processes the information for each movie and sends it to index.html'''
    form_info = ""
    if request.method == "POST":
        form_info = request.form["movie"]
        param["query"] = form_info
        resp = requests.get(movie_search, params=param)
        res = resp.json()["results"]
        poster = []
        titles = []
        images = []
        wiki = []
        links = []
        for num, information in enumerate(res):
            poster.append(res[num - 1]["poster_path"])
            titles.append(res[num - 1]["title"])
            wiki.append(get_wiki(titles[num]))
            links.append(query_gen(name=titles[num]))
            if titles[num - 1] is not None:
                images.append(
                    f"http://image.tmdb.org/t/p/w500{res[num-1]['poster_path']}"
                )
            else:
                break
    return render_template(
            "index.html",
            search=form_info,
            length=len(images),
            image=images,
            title=titles,
            wlink=wiki,
            route=links,
        )


@app.route("/review", methods=["POST", "GET"])
@login_required
def display_reviews():
    '''This method renders all the reviews and ratings of the movie and pushes to review.html'''
    name = request.args.get("name")
    path = request.args.get("path")
    redir = f"/review?name={name}&path={path}"
    if request.method == "POST":
        form_data = request.form
        rating = form_data["rating"]
        comments = form_data["comments"]
        query = Reviews.query.filter_by(title=name, user_id=current_user.id).first()
        if query is None:
            rec = Reviews(
                title=name,
                user_id=current_user.id,
                rating=float(rating),
                review=comments,
            )
            db.session.add(rec)
        else:
            query.rating = int(rating)
            query.review = comments
        db.session.commit()
    query = Reviews.query.filter_by(title=name).all()
    reviews = []
    score = 0
    cter = 1
    for rec in query:
        reviews.append(
            f"{cter}. According to {current_user.first_name}, '{rec.review}'"
        )
        cter += 1
        score += rec.rating
    if len(query) != 0:
        score /= len(query)
    return render_template(
        "review.html",
        name=name,
        redirect_back=redir,
        score=score,
        comments=reviews,
        path=path,
    )

def query_gen(name):
    '''This method returns the path to redirect'''
    return f"/review?name={name}"

def get_wiki(movie_name):
    '''This method returns Wikipedia page of movie.'''
    wiki_url = "https://en.wikipedia.org/w/api.php"
    wiki_params = {
        "action": "query",
        "titles": movie_name,
        "format": "json",
    }
    output = requests.get(wiki_url, wiki_params)
    pageid = list(output.json()["query"]["pages"])[0]
    if pageid != -1:
        return f"http://en.wikipedia.org/?curid={pageid}"
    return None

if __name__ == "__main__":
    app.run(os.getenv("IP", "0.0.0.0"), port=int(os.getenv("PORT", "8080")), debug=True)
