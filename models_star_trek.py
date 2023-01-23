"""This module contains the Star Trek models for the database."""

from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy() 


class Animal(db.Model):
    """Creates an instance of animal for the table in the database"""

    __tablename__ = "animals"
    
    uid = db.Column(db.Text, primary_key=True)
    
    name = db.Column(db.Text, nullable=False)
    
    earthAnimal = db.Column(db.Boolean, nullable=False)
    
    earthInsect = db.Column(db.Boolean, nullable=False)
    
    avian = db.Column(db.Boolean, nullable=False)
    
    canine = db.Column(db.Boolean, nullable=False)
    
