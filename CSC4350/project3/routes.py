'''Author: Preetham Thelluri
This app allows user to edit past ratings left on movies. The user can also delete old reviews.
'''
from app import app, db
import random
import flask
from flask_login import login_user, current_user, LoginManager, logout_user
from flask_login.utils import login_required
from models import User, Rating

from wikipedia import get_wiki_link
from tmdb import get_movie_data

login_manager = LoginManager()
login_manager.login_view = "login"
login_manager.init_app(app)

bp = flask.Blueprint(
    "bp",
    __name__,
    template_folder="./static/react",
)

@login_manager.user_loader
def load_user(user_name):
    '''Loads user information'''
    return User.query.get(user_name)


@app.route("/signup")
def signup():
    '''Tenders the signup template'''
    return flask.render_template("signup.html")

@app.route("/signup", methods=["POST"])
def signup_post():
    '''Allows the user to sign up'''
    username = flask.request.form.get("username")
    user = User.query.filter_by(username=username).first()
    if user:
        pass
    else:
        user = User(username=username)
        db.session.add(user)
        db.session.commit()

    return flask.redirect(flask.url_for("login"))


@app.route("/login")
def login():
    '''Defualt page of the app'''
    return flask.render_template("login.html")


@app.route("/login", methods=["POST"])
def login_post():
    '''Lets the user login or sign up based on need'''
    username = flask.request.form.get("username")
    user = User.query.filter_by(username=username).first()
    if user:
        login_user(user)
        return flask.redirect(flask.url_for("index"))
    else:
        return flask.jsonify({"status": 401, "reason": "Your credentials are inaccurate!"})


MOVIE_IDS = [
    157336, 20453, 14756, 14757, 449924
]

@app.route("/rate", methods=["POST"])
def rate():
    '''Adds rating to the movie'''
    data = flask.request.form
    rating = data.get("rating")
    comment = data.get("comment")
    movie_id = data.get("movie_id")

    new_rating = Rating(
        username=current_user.username,
        rating=rating,
        comment=comment,
        movie_id=movie_id,
    )

    db.session.add(new_rating)
    db.session.commit()
    return flask.redirect("comments")

@app.route("/")
def landing():
    '''This authenticates the user and lets him/her in if valid'''
    if current_user.is_authenticated:
        return flask.redirect("comments")
    return flask.redirect("login")

@app.route("/logout")
def logout():
    '''This helps user to log out'''
    logout_user()
    return flask.redirect("login")

@app.route("/comments")
@login_required
def index():
    '''This method shows ratings on the movie page'''
    movie_id = random.choice(MOVIE_IDS)

    # API calls
    (title, tagline, genre, poster_image) = get_movie_data(movie_id)
    wikipedia_url = get_wiki_link(title)

    ratings = Rating.query.filter_by(movie_id=movie_id).all()

    return flask.render_template(
        "comments.html",
        title=title,
        tagline=tagline,
        genre=genre,
        poster_image=poster_image,
        wiki_url=wikipedia_url,
        ratings=ratings,
        movie_id=movie_id,
    )

@bp.route("/coms")
def rend():
    '''This method renders the intial pages and communicates with js.'''
    return flask.render_template("index.html")

@app.route("/revs", methods=["GET", "POST"])
def rem():
    '''This method displays all ratings on the page'''
    reviews = Rating.query.filter_by(username=current_user.username).all()
    revs = []
    for each in reviews:
        data = {}
        data['rev_id'] = each.id
        data['rating'] = each.rating
        data['reviews'] = each.comment
        data['username'] = current_user.username
        revs.append(data)
    return flask.jsonify(revs)

@bp.route("/update", methods=["GET", "POST", "PUT"])
def updatedata():
    '''This method updates ratings given by a user.'''
    user_info = Rating.query.filter_by(username=current_user.username).all()
    for each in user_info:
        id_s = flask.request.get_json("newchange")
        each.rating = int(id_s)
        db.session.commit()
    return flask.render_template("index.html")

@bp.route("/del", methods=["GET", "POST"])
def deletedata():
    '''This method deletes a specific rating'''
    id_s = flask.request.get_json("deleteme")
    all_ids = id_s["rev_id"]
    current_rate = Rating.query.filter_by(id=all_ids).first()
    db.session.delete(current_rate)
    db.session.commit()
    return flask.render_template("index.html")

app.register_blueprint(bp)

if __name__ == "__main__":
    app.run(
        debug=True
    )