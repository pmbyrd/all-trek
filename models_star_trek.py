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
    
# Astronomical Object	
# uid	str, PK
# name	str
# AstronomicalObjectType	str
# location	FK, location
# !CRITICAL TO HAVE A FOREIGN KEY FOR LOCATION, without it the data will not be able to be called from the database.
class AstronomicalObject(db.Model):
    """Creates an instance of an astronomical object for the database."""
    
    __tablename__ = "astronomicalObjects"

    uid = db.Column(db.Text, primary_key=True)
    
    name = db.Column(db.Text, nullable=False)
    
    astronomicalObjectType = db.Column(db.Text, nullable=True)
    
    location = db.Column(db.JSON)
    
# Characters	
# uid	str, PK
# name	str
# gender	str
# yearOfBirth	int
# monthOfBirth	int
# dayOfBirth	int
# placeOfBirth	str
# yearOfDeath	int
# monthOfDeath	int
# dayOfDeath	int
# placeOfDeath	str
# height	int
# weight	int
# decease	bool
# bloodtype	str
# martialStatus	str
# hologramActivationDate	int
# hologramStatus	str
# hologram	bool
# fictionalCharacter	bool
# mirror	bool
# alternateReality	bool
# hologramDateStatus	int

class Character(db.Model):
    """Creates an instance of a character for the database."""
    
    __tablename__ = "characters"
    
    uid = db.Column(db.Text, primary_key=True)
    
    name = db.Column(db.Text, nullable=False)
    
    gender = db.Column(db.Text, nullable=False)
    
    yearOfBirth = db.Column(db.Integer, nullable=False)
    
    monthOfBirth = db.Column(db.Integer, nullable=False)
    
    dayOfBirth = db.Column(db.Integer, nullable=False)
    
    placeOfBirth = db.Column(db.Text, nullable=False)
    
    yearOfDeath = db.Column(db.Integer, nullable=False)
    
    monthOfDeath = db.Column(db.Integer, nullable=False)
    
    dayOfDeath = db.Column(db.Integer, nullable=False)
    
    placeOfDeath = db.Column(db.Text, nullable=False)
    
    height = db.Column(db.Integer, nullable=False)
    
    weight = db.Column(db.Integer, nullable=False)
    
    deceased = db.Column(db.Boolean, nullable=False)
    
    bloodtype = db.Column(db.Text, nullable=False)
    
    martialStatus = db.Column(db.Text, nullable=False)
    
    hologramActivationDate = db.Column(db.Integer, nullable=False)
    
    hologramStatus = db.Column(db.Text, nullable=False)
    
    hologram = db.Column(db.Boolean, nullable=False)
    
    fictionalCharacter = db.Column(db.Boolean, nullable=False)
    
    mirror = db.Column(db.Boolean, nullable=False)
    
    alternateReality = db.Column(db.Boolean, nullable=False)
    
    hologramDateStatus = db.Column(db.Integer, nullable=False)
    
    
    
    
    
    

class Title(db.Model):
    """Creates an instance of a title for the database."""
    
    uid = db.Column(db.String, primary_key=True)
    
    name = db.Column(db.Text, nullable=False)
    
    militaryRank = db.Column(db.Boolean, nullable=False)
    
    fleetRank = db.Column(db.Boolean, nullable=False)
    
    religiousTitle = db.Column(db.Boolean, nullable=False)
    
    position = db.Column(db.Boolean, nullable=False)
    
    mirror = db.Column(db.Boolean, nullable=False)
    
# locations	
# uid	str, PK
# name	str 
# earthlyLocation	bool
# fictionalLocaltion	bool
# religiousLocation	bool
# geographicalLocation	bool
# bodyOfWater	bool
# country	bool
# subnationalEntity	bool
# settlement	bool
# usSettlement	bool
# bajoranSettlement	bool
# colony	bool
# landform	bool
# landmark	bool
# road	bool
# structure	bool
# shipyard	bool
# buildingInterior	bool
# establishment	bool
# medicalEstablishmen	bool
# ds9Establishment	bool
# school	bool
# mirror	bool
# alternateReality	bool
class Location(db.Model):
    """Creates an instance of a location for the database."""
    
    uid = db.Column(db.String, primary_key=True)
    
    name = db.Column(db.Text, nullable=False)
    
    earthlyLocation = db.Column(db.Boolean, nullable=False)
    
    fictionalLocation = db.Column(db.Boolean, nullable=False)
    
    religiousLocation = db.Column(db.Boolean, nullable=False)
    
    geographicalLocation = db.Column(db.Boolean, nullable=False)
    
    bodyOfWater = db.Column(db.Boolean, nullable=False)
    
    country = db.Column(db.Boolean, nullable=False)
    
    subnationalEntity = db.Column(db.Boolean, nullable=False)
    
    settlement = db.Column(db.Boolean, nullable=False)
    
    usSettlement = db.Column(db.Boolean, nullable=False)
    
    bajoranSettlement = db.Column(db.Boolean, nullable=False)
    
    colony = db.Column(db.Boolean, nullable=False)
    
    landform = db.Column(db.Boolean, nullable=False)
    
    landmark =  db.Column(db.Boolean, nullable=False)
    
    road = db.Column(db.Boolean, nullable=False)
    
    structure = db.Column(db.Boolean, nullable=False)
    
    shipyard = db.Column(db.Boolean, nullable=False)
    
    buildingInterior = db.Column(db.Boolean, nullable=False)
    
    establishment = db.Column(db.Boolean, nullable=False)
    
    medicalEstablishment = db.Column(db.Boolean, nullable=False)
    
    ds9Establishment = db.Column(db.Boolean, nullable=False)
    
    school = db.Column(db.Boolean, nullable=False)
    
    mirror = db.Column(db.Boolean, nullable=False)
    
    alternateReality = db.Column(db.Boolean, nullable=False)
    
    