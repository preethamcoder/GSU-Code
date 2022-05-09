import flask
from flask_sqlalchemy import SQLAlchemy

app = flask.Flask(__name__)
db = SQLAlchemy(app)


class Rating(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    rating = db.Column(db.Integer)
    username = db.Column(db.String(80))
    timestamp = db.Column(
        db.Integer
    )  # this is NOT how you would typically store a timestamp in a database, but let's keep things simple for this example. A larger int is a more recent timestamp.


def undo_last_review():
    """
    Pops out the most recent review and deletes it from the DB. Returns the review object that was just removed.
    """

    user_ratings = Rating.query.all()
    most_recent = max(
        user_ratings, key=lambda x: x.timestamp
    )  # concise Python way of finding the element with the largest timestamp attribute in a list
    db.session.delete(most_recent)
    db.session.commit()
    return most_recent

