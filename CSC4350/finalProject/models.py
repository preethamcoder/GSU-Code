# pylint: disable=no-member

"""This is the main driver for the app, it has the database models and the routes"""
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from app import db


class User(db.Model, UserMixin):
    """This is the database table for the User"""

    id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(350), nullable=False)

    def __repr__(self):
        """Represents the user currently logged in"""
        return f"<{self.id}:{self.user_name}>"

    def __init__(self, password, user_name):
        """Initializes a user object to add to the database"""
        self.user_name = user_name
        self.password = generate_password_hash(password)

    def verify_password(self, pwd):
        """Checks if the user has the right password entered"""
        return check_password_hash(self.password, pwd)


class Reviews(db.Model):
    """This is the database table for the reviews that are left on each video/playlist"""

    id = db.Column(db.Integer, primary_key=True, nullable=False)
    video_title = db.Column(db.String(100), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    review = db.Column(db.String(280), nullable=False)
    video_id = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        """Represents the video commented and the user id"""
        return f"<{self.video_id}:{self.user_id}>"

    def reviews(self):
        """Returns the comment entered"""
        return self.review


class Playlists(db.Model):
    """This is the database table where the saved playlists are stored"""

    id = db.Column(db.Integer, primary_key=True, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    playlist_title = db.Column(db.String(150), nullable=False)
    playlist = db.Column(db.String(), nullable=False)

    def __repr__(self):
        """Represents the playlist saved by the user"""
        return f"<{self.user_id}:{self.playlist_title}>"

    def playlists(self):
        """Returns the saved playlist"""
        return self.playlist

db.create_all()
