"""This module contains the Star Trek models for the database."""

from flask_sqlalchemy import SQLAlchemy
from models import db
# db = SQLAlchemy() 


class Animal(db.Model):
    """Creates an instance of animal for the table in the database"""

    __tablename__ = "animals"
    
    uid = db.Column(db.Text, primary_key=True)
    
    name = db.Column(db.Text, nullable=False)
    
    earthAnimal = db.Column(db.Boolean, nullable=False)
    
    earthInsect = db.Column(db.Boolean, nullable=False)
    
    avian = db.Column(db.Boolean, nullable=False)
    
    canine = db.Column(db.Boolean, nullable=False)
    
    feline = db.Column(db.Boolean, nullable=False)
    

class Title(db.Model):
    """Creates an instance of a title for the database."""
    
    uid = db.Column(db.String, primary_key=True)
    
    name = db.Column(db.Text, nullable=False)
    
    militaryRank = db.Column(db.Boolean, nullable=False)
    
    fleetRank = db.Column(db.Boolean, nullable=False)
    
    religiousTitle = db.Column(db.Boolean, nullable=False)
    
    position = db.Column(db.Boolean, nullable=False)
    
    mirror = db.Column(db.Boolean, nullable=False)
    
