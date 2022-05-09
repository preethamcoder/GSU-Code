# pylint: disable=trailing-whitespace
# pylint: disable=no-member
"""These are the routes of the app, which help us navigate through it with different endpoints"""
import os
from flask import (
    Blueprint,
    render_template,
    flash,
    redirect,
    url_for,
    jsonify,
    request,
)
from flask_login import (
    LoginManager,
    login_user,
    login_required,
    current_user,
    logout_user,
)
from app import db, app
from models import User, Reviews, Playlists

login_manager = LoginManager()
login_manager.init_app(app)

bp = Blueprint(
    "bp",
    __name__,
    template_folder="./static/react",
)


@login_manager.user_loader
def load_user(user_id):
    """This function will load user"""
    return User.query.get(user_id)


@app.route("/")
def index():
    """This function will render the index page"""
    return render_template("index.html")


@app.route("/login")
def login():
    """This displays the login page"""
    return render_template("login.html")


@app.route("/register")
def register():
    """Displays the sign up page"""
    return render_template("register.html")


@bp.route("/login", methods=["POST"])
def login_form():
    """This form checks if user is already a member"""
    user = request.form.get("username")
    password = request.form.get("password")
    user_query = User.query.filter_by(user_name=user).first()

    if user_query and user_query.verify_password(password):
        login_user(user_query)
        return render_template("index.html")
    flash("username or password incorrect")
    return render_template("login.html")


@app.route("/userLoggedIn")
def user_logged_in():
    """This method returns if the user is logged in"""
    return jsonify({"logged_in": current_user.is_authenticated})


@app.route("/addComment", methods=["GET", "POST"])
def comment_it():
    """This adds a comment to the database for the specific video"""
    info = request.json
    video_title = info["videoTitle"][:100]
    success = current_user.is_authenticated
    if request.method == "POST" and success:
        record = Reviews(
            video_title=video_title,
            user_id=current_user.id,
            review=info["comment"][:280],
            video_id=info["videoId"],
        )
        db.session.add(record)
    db.session.commit()
    comments = Reviews.query.filter_by(video_id=info["videoId"]).all()
    comment_list = []
    for comment in comments:
        comment_list.append(
            {
                "user": User.query.filter_by(id=comment.user_id).first().user_name,
                "text": comment.review,
            }
        )

    return jsonify({"comment_list": comment_list})


@app.route("/getComments", methods=["GET", "POST"])
def render_comments():
    """This gets all the comments back from the database"""

    comments = Reviews.query.filter_by(video_id=request.args.get("videoId")).all()

    comment_list = []
    for comment in comments:
        comment_list.append(
            {
                "user": User.query.filter_by(id=comment.user_id).first().user_name,
                "text": comment.review,
            }
        )

    return jsonify({"comment_list": comment_list})


@app.route("/register", methods=["POST"])
def register_form():
    """Signs up new user"""
    user = request.form.get("username")
    pwd = request.form.get("password")
    new_user = User(user_name=user, password=pwd)
    user_query = User.query.filter_by(user_name=user).first()
    if user_query:
        flash("Sorry... username taken")
        return redirect(url_for("register"))
    db.session.add(new_user)
    db.session.commit()
    return redirect(url_for("login"))


@bp.route("/logout")
def logout():
    """Logs the user out of the app, redirects him/her to the login page"""
    logout_user()
    return render_template("login.html")


@app.route("/addPlaylist", methods=["GET", "POST"])
def append_playlist():
    """This adds the saved playlist to the user's name in the database"""
    data = request.json
    user_id = current_user.id
    playlist_title = data["title"]
    playlist = str(data["playlist"])
    if request.method == "POST":
        record = Playlists(
            user_id=user_id, playlist_title=playlist_title, playlist=playlist
        )
        db.session.add(record)
    db.session.commit()
    saved = Playlists.query.filter_by(user_id=user_id).all()
    saved_playlists = []
    for each in saved:
        saved_playlists.append(
            {
                "playlistTitle": each.playlist_title,
                "playlist": each.playlist,
            }
        )

    return jsonify({"savedPlaylists": saved_playlists})


@app.route("/getPlaylist", methods=["GET", "POST"])
@login_required
def get_playlist():
    """This brings all the comments from the database to the front end"""

    playlists = Playlists.query.filter_by(user_id=current_user.id).all()
    saved_playlists = []
    for each in playlists:
        saved_playlists.append(
            {
                "playlistTitle": each.playlist_title,
                "playlist": each.playlist,
            }
        )

    return jsonify({"savedPlaylists": saved_playlists})


app.register_blueprint(bp)

if __name__ == "__main__":
    app.run(os.getenv("IP", "0.0.0.0"), port=int(os.getenv("PORT", "8080")), debug=True)
