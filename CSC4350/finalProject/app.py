"""This is includes database setup"""
import os
import flask
from flask_sqlalchemy import SQLAlchemy
from dotenv import find_dotenv, load_dotenv

load_dotenv(find_dotenv())

app = flask.Flask(__name__)
database = os.getenv("DATABASE_URL")
if database.startswith("postgres://"):
    database = database.replace("postgres://", "postgresql://", 1)
app.config["SQLALCHEMY_DATABASE_URI"] = database
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.secret_key = b"Nothing in here, this is to protect from de-frauding"

db = SQLAlchemy(app)
