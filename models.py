"""This module contains the models for the database, user, post, tag, post_tag."""
# *Importing the required modules
from flask_sqlalchemy import SQLAlchemy

# *Intialize db connection

db = SQLAlchemy()
def connect_db(app):
    """Connection to the database that is called in app.py for the Flask app to use."""
    db.app = app
    db.init_app(app)
    
class User():
    """Creates a user model for the database."""
    __tablename__ = "users"
    
    