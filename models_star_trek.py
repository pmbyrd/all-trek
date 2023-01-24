"""This module contains the Star Trek models for the database."""

from flask_sqlalchemy import SQLAlchemy
from models import db


class Animal(db.Model):
    """Creates an instance of animal for the table in the database"""

    __tablename__ = "animals"
    
    
    name = db.Column(db.Text, nullable=False)
    
    uid = db.Column(db.Text, primary_key=True)
    
    earthAnimal = db.Column(db.Boolean, nullable=False) 
    
    earthInsect = db.Column(db.Boolean, nullable=False)
    
    avian = db.Column(db.Boolean, nullable=False)    
    
    canine = db.Column(db.Boolean, nullable=False)
    
    feline = db.Column(db.Boolean, nullable=False)
    

class AstronomicalObject(db.Model):
    """Creates an instance of an astronomical object for the database."""
    
    __tablename__ = "astronomicalObjects"

    uid = db.Column(db.Text, primary_key=True)
    
    name = db.Column(db.Text, nullable=False)
    
    astronomicalObjectType = db.Column(db.Text, nullable=True)
    
    location = db.Column(db.JSON)
    

class Character(db.Model):
    """Creates an instance of a character for the database."""
    
    __tablename__ = "characters"
    
    uid = db.Column(db.Text, primary_key=True)
    
    name = db.Column(db.Text, nullable=False)
    
    gender = db.Column(db.Text, nullable=True)
    
    yearOfBirth = db.Column(db.Integer, nullable=True)
    
    monthOfBirth = db.Column(db.Integer, nullable=True)
    
    dayOfBirth = db.Column(db.Integer, nullable=True)
    
    placeOfBirth = db.Column(db.Text, nullable=True)
    
    yearOfDeath = db.Column(db.Integer, nullable=True)
    
    monthOfDeath = db.Column(db.Integer, nullable=True)
    
    dayOfDeath = db.Column(db.Integer, nullable=True)
    
    placeOfDeath = db.Column(db.Text, nullable=True)
    
    height = db.Column(db.Integer, nullable=True)
    
    weight = db.Column(db.Integer, nullable=True)
    
    deceased = db.Column(db.Boolean, nullable=True)
    
    bloodType = db.Column(db.Text, nullable=True)
    
    maritalStatus= db.Column(db.Text, nullable=True)
    
    serialNumber = db.Column(db.Text, nullable=True)
    
    hologramActivationDate = db.Column(db.Integer, nullable=True)
    
    hologramStatus = db.Column(db.Text, nullable=True)
    
    hologram = db.Column(db.Boolean, nullable=True)
    
    fictionalCharacter = db.Column(db.Boolean, nullable=True)
    
    mirror = db.Column(db.Boolean, nullable=True)
    
    alternateReality = db.Column(db.Boolean, nullable=True)
    
    hologramDateStatus = db.Column(db.Integer, nullable=True)
    
    
class Performer(db.Model):
    """Creates an instance of a performer for the database."""
    
    __tablename__ = "performers"
    
    uid = db.Column(db.Text, primary_key=True)
    
    name = db.Column(db.Text, nullable=False)
    
    birthName = db.Column(db.Text, nullable=True)
    
    gender = db.Column(db.Text, nullable=True)
    
    dateOfBirth = db.Column(db.Text, nullable=True)
    
    placeOfBirth = db.Column(db.Text, nullable=True)
    
    dateOfDeath = db.Column(db.Text, nullable=True)
    
    placeOfDeath  = db.Column(db.Text, nullable=True)
        
    animalPerformer = db.Column(db.Boolean, nullable=False)
    
    disPerformer = db.Column(db.Boolean, nullable=False)
    
    ds9Performer = db.Column(db.Boolean, nullable=False)
    
    entPerformer = db.Column(db.Boolean, nullable=False)
    
    filmPerformer = db.Column(db.Boolean, nullable=False)
    
    standInPerformer = db.Column(db.Boolean, nullable=False)
    
    stuntPerformer = db.Column(db.Boolean, nullable=False)
    
    tasPerformer = db.Column(db.Boolean, nullable=False)
    
    tngPerformer = db.Column(db.Boolean, nullable=False)
    
    tosPerformer = db.Column(db.Boolean, nullable=False)
    
    videoGamePerformer  = db.Column(db.Boolean, nullable=False)
    
    voicePerformer  = db.Column(db.Boolean, nullable=False)
    
    voyPerformer = db.Column(db.Boolean, nullable=False)
    	

    
    
    

class Title(db.Model):
    """Creates an instance of a title for the database."""
    
    uid = db.Column(db.String, primary_key=True)
    
    name = db.Column(db.Text, nullable=False)
    
    militaryRank = db.Column(db.Boolean, nullable=False)
    
    fleetRank = db.Column(db.Boolean, nullable=False)
    
    religiousTitle = db.Column(db.Boolean, nullable=False)
    
    position = db.Column(db.Boolean, nullable=False)
    
    mirror = db.Column(db.Boolean, nullable=False)


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
    
    
class Conflict(db.Model):
    """Creates an instance of a conflict for the database."""
    
    uid = db.Column(db.String, primary_key=True)
    
    name = db.Column(db.Text, nullable=False)
    
    yearFrom = db.Column(db.Integer, nullable=True)
    
    yearTo = db.Column(db.Integer, nullable=True)
    
    earthConflict = db.Column(db.Boolean, nullable=False)
    
    federationWar = db.Column(db.Boolean, nullable=False)
    
    klingonWar = db.Column(db.Boolean, nullable=False)
    
    dominionWarBattle = db.Column(db.Boolean, nullable=False)
    
    alternateReality = db.Column(db.Boolean, nullable=False)
    
    
class Element(db.Model):
    """Creates an instance of an element found in the Star Trek universe for the database."""
    
    uid = db.Column(db.String, primary_key=True)
    
    name = db.Column(db.Text, nullable=False)
    
    symbol = db.Column(db.Text, nullable=True)
    
    atomicNumber = db.Column(db.Integer, nullable=True)
    
    atomicWeight = db.Column(db.Integer, nullable=True)
    
    transuranium = db.Column(db.Boolean, nullable=False)
    
    gammaSeries = db.Column(db.Boolean, nullable=False)
    
    hypersonicSeries = db.Column(db.Boolean, nullable=False)
    
    megaSeries = db.Column(db.Boolean, nullable=False)
    
    omegaSeries = db.Column(db.Boolean, nullable=False)
    
    transonicSeries = db.Column(db.Boolean, nullable=False)
    
    worldSeries = db.Column(db.Boolean, nullable=False)
    
    
class Weapon(db.Model):
    """Creates an instance of a weapon for the database."""
    
    uid = db.Column(db.String, primary_key=True)
    
    name = db.Column(db.Text, nullable=False)
    
    handHeldWeapon = db.Column(db.Boolean, nullable=False)
    
    laserTechnology = db.Column(db.Boolean, nullable=False)
    
    plasmaTechnology = db.Column(db.Boolean, nullable=False)
    
    worldSeries = db.Column(db.Boolean, nullable=False)
    
    photonicTechnology = db.Column(db.Boolean, nullable=False)
    
    phaserTechnology = db.Column(db.Boolean, nullable=False)
    
    mirror = db.Column(db.Boolean, nullable=False)
    
    alternateReality = db.Column(db.Boolean, nullable=False)
    
        
    
    
    
    
     
     
    
    