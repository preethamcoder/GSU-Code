# pylint: disable=no-member
# pylint: disable=too-few-public-methods
"""This helps us create instances of information to database"""
from flask_login import UserMixin
from app import db


class User(db.Model, UserMixin):
    """Creates a user object"""

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)


class Rating(db.Model):
    """Creates a rating object"""

    id = db.Column(db.Integer, primary_key=True)
    rating = db.Column(db.Integer)
    comment = db.Column(db.String(200))
    username = db.Column(db.String(80))
    movie_id = db.Column(db.Integer)


db.create_all()
