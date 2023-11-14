# models.py
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    # Define other User fields

class Food(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    # Define other Food fields
