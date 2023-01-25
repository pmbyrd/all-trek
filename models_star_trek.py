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
    
    worldSeries = db.Column(db.Boolean, nullable=True)
    
    photonicTechnology = db.Column(db.Boolean, nullable=False)
    
    phaserTechnology = db.Column(db.Boolean, nullable=False)
    
    mirror = db.Column(db.Boolean, nullable=False)
    
    alternateReality = db.Column(db.Boolean, nullable=False)


class Food(db.Model):
    """Creates an instance of a food for the database."""
    
    uid = db.Column(db.String, primary_key=True)
    
    name = db.Column(db.Text, nullable=False)
    
    earthlyOrigin = db.Column(db.Boolean, nullable=False)
    
    dessert = db.Column(db.Boolean, nullable=False)
    
    fruit = db.Column(db.Boolean, nullable=False)
    
    herbOrSpice = db.Column(db.Boolean, nullable=False)
    
    sauce = db.Column(db.Boolean, nullable=False)
    
    soup = db.Column(db.Boolean, nullable=False)
    
    beverage = db.Column(db.Boolean, nullable=False)
    
    alcoholicBeverage = db.Column(db.Boolean, nullable=False)
    
    juice = db.Column(db.Boolean, nullable=False)
    
    tea = db.Column(db.Boolean, nullable=False)
    

class Technology(db.Model):
    """Creates an instance of a technology for the database."""
    
    uid = db.Column(db.String, primary_key=True)
    
    name = db.Column(db.Text, nullable=False)
    
    borgTechnology = db.Column(db.Boolean, nullable=False)
    
    borgComponent = db.Column(db.Boolean, nullable=False)
    
    communicationsTechnology = db.Column(db.Boolean, nullable=False)
    
    computerTechnology = db.Column(db.Boolean, nullable=False)
    
    computerProgramming = db.Column(db.Boolean, nullable=False)
    
    subroutine = db.Column(db.Boolean, nullable=False)
    
    database = db.Column(db.Boolean, nullable=False)
    
    energyTechnology = db.Column(db.Boolean, nullable=False)
    
    fictionalTechnology = db.Column(db.Boolean, nullable=False)
    
    holographicTechnology = db.Column(db.Boolean, nullable=False)
    
    identificationTechnology = db.Column(db.Boolean, nullable=False)
    
    lifeSupportTechnology = db.Column(db.Boolean, nullable=False)
    
    sensorTechnology = db.Column(db.Boolean, nullable=False)
    
    shieldTechnology = db.Column(db.Boolean, nullable=False)
    
    tool = db.Column(db.Boolean, nullable=False)
    
    culinaryTool = db.Column(db.Boolean, nullable=False)
    
    engineeringTool = db.Column(db.Boolean, nullable=False)
    
    householdTool = db.Column(db.Boolean, nullable=False)
    
    medicalEquipment = db.Column(db.Boolean, nullable=False)
    
    transporterTechnology = db.Column(db.Boolean, nullable=False)


class Company(db.Model):
    """Creates an instance of a company for the database."""
    
    uid = db.Column(db.String, primary_key=True)
    
    name = db.Column(db.Text, nullable=False)

    broadcaster  = db.Column(db.Boolean, nullable=False)

    collectibleCompany = db.Column(db.Boolean, nullable=False)

    conglomerate = db.Column(db.Boolean, nullable=False)

    digitalVisualEffectsCompany = db.Column(db.Boolean, nullable=False)

    distributor = db.Column(db.Boolean, nullable=False)

    gameCompany = db.Column(db.Boolean, nullable=False)

    filmEquipmentCompany = db.Column(db.Boolean, nullable=False)

    makeUpEffectsStudio = db.Column(db.Boolean, nullable=False)

    mattePaintingCompany = db.Column(db.Boolean, nullable=False)

    modelAndMiniatureEffectsCompany = db.Column(db.Boolean, nullable=False)

    postProductionCompany = db.Column(db.Boolean, nullable=False)

    productionCompany = db.Column(db.Boolean, nullable=False)

    propCompany = db.Column(db.Boolean, nullable=False)

    recordLabel = db.Column(db.Boolean, nullable=False)

    specialEffectsCompany = db.Column(db.Boolean, nullable=False)

    tvAndFilmProductionCompany = db.Column(db.Boolean, nullable=False)

    videoGameCompany = db.Column(db.Boolean, nullable=False)

class Staff(db.Model):
    """Creates an instace of a staff member for the database."""
    
    uid = db.Column(db.String, primary_key=True)
    
    name = db.Column(db.Text, nullable=False)
    
    birthName = db.Column(db.Text, nullable=True)
    
    gender = db.Column(db.Text, nullable=True)
    
    dateOfBirth = db.Column(db.Text, nullable=True)
    
    placeOfBirth = db.Column(db.Text, nullable=True)
    
    dateOfDeath = db.Column(db.Text, nullable=True)
    
    placeOfDeath = db.Column(db.Text, nullable=True)
    
    artDepartment = db.Column(db.Boolean, nullable=False)
    
    artDirector = db.Column(db.Boolean, nullable=False)
    
    productionDesigner = db.Column(db.Boolean, nullable=False)
    
    cameraAndElectricalDepartment = db.Column(db.Boolean, nullable=False)

    cinematographer  = db.Column(db.Boolean, nullable=False)

    castingDepartment = db.Column(db.Boolean, nullable=False)

    costumeDepartment = db.Column(db.Boolean, nullable=False)

    costumeDesigner = db.Column(db.Boolean, nullable=False)

    director = db.Column(db.Boolean, nullable=False)

    assistantOrSecondUnitDirector = db.Column(db.Boolean, nullable=False)

    exhibitAndAttractionStaff = db.Column(db.Boolean, nullable=False)

    filmEditor = db.Column(db.Boolean, nullable=False)

    linguist = db.Column(db.Boolean, nullable=False)

    locationStaff = db.Column(db.Boolean, nullable=False)

    makeupStaff = db.Column(db.Boolean, nullable=False)

    musicDepartment = db.Column(db.Boolean, nullable=False)

    composer = db.Column(db.Boolean, nullable=False)

    personalAssistant = db.Column(db.Boolean, nullable=False)

    producer = db.Column(db.Boolean, nullable=False)

    productionAssociate = db.Column(db.Boolean, nullable=False)

    productionStaff = db.Column(db.Boolean, nullable=False)

    publicationStaff = db.Column(db.Boolean, nullable=False)

    scienceConsultant = db.Column(db.Boolean, nullable=False)

    soundDepartment = db.Column(db.Boolean, nullable=False)

    specialAndVisualEffectsStaff = db.Column(db.Boolean, nullable=False)

    author = db.Column(db.Boolean, nullable=False)

    audioAuthor = db.Column(db.Boolean, nullable=False)

    calendarArtist = db.Column(db.Boolean, nullable=False)

    comicArtist = db.Column(db.Boolean, nullable=False)

    comicAuthor = db.Column(db.Boolean, nullable=False)

    comicColorArtist = db.Column(db.Boolean, nullable=False)

    comicInteriorArtist = db.Column(db.Boolean, nullable=False)

    comicInkArtist = db.Column(db.Boolean, nullable=False)

    comicPencilArtist = db.Column(db.Boolean, nullable=False)

    comicLetterArtist = db.Column(db.Boolean, nullable=False)

    comicStripArtist = db.Column(db.Boolean, nullable=False)

    gameArtist = db.Column(db.Boolean, nullable=False)

    gameAuthor = db.Column(db.Boolean, nullable=False)

    novelArtist = db.Column(db.Boolean, nullable=False)

    novelAuthor = db.Column(db.Boolean, nullable=False)

    referenceArtist = db.Column(db.Boolean, nullable=False)

    referenceAuthor = db.Column(db.Boolean, nullable=False)

    publicationArtist = db.Column(db.Boolean, nullable=False)

    publicationDesigner = db.Column(db.Boolean, nullable=False)

    publicationEditor = db.Column(db.Boolean, nullable=False)

    publicityArtist = db.Column(db.Boolean, nullable=False)

    cbsDigitalStaff = db.Column(db.Boolean, nullable=False)

    ilmProductionStaff = db.Column(db.Boolean, nullable=False)

    specialFeaturesStaff = db.Column(db.Boolean, nullable=False)

    storyEditor = db.Column(db.Boolean, nullable=False)

    studioExecutive = db.Column(db.Boolean, nullable=False)

    stuntDepartment = db.Column(db.Boolean, nullable=False)

    transportationDepartment = db.Column(db.Boolean, nullable=False)

    videoGameProductionStaff = db.Column(db.Boolean, nullable=False)

    writer = db.Column(db.Boolean, nullable=False)
    

class Species(db.Model):
    """Creates an instance of a species from the Star Trek universe for the database"""
    # *homeworld must reference a planet in the Planets table, quadrant must also be a referenced to the astronomical quadrant of the planet
    
    uid = db.Column(db.String, primary_key=True)
    
    name = db.Column(db.Text, nullable=False)
    
    homeworld = db.Column(db.JSON, nullable=True)
    
    quadrant = db.Column(db.JSON, nullable=True)
    
    extinctSpecies = db.Column(db.Boolean, nullable=False)
    
    warpCapableSpecies = db.Column(db.Boolean, nullable=False)
    
    extraGalacticSpecies = db.Column(db.Boolean, nullable=False)
    
    humanoidSpecies = db.Column(db.Boolean, nullable=False)
    
    reptilianSpecies = db.Column(db.Boolean, nullable=False)
    
    nonCorporealSpecies = db.Column(db.Boolean, nullable=False)
    
    shapeshiftingSpecies = db.Column(db.Boolean, nullable=False)
    
    spaceborneSpecies = db.Column(db.Boolean, nullable=False)
    
    telepathicSpecies = db.Column(db.Boolean, nullable=False)
    
    transDimensionalSpecies = db.Column(db.Boolean, nullable=False)
    
    unnamedSpecies = db.Column(db.Boolean, nullable=False)
    
    alternateReality = db.Column(db.Boolean, nullable=False)
    
    # *homeworld and quadrant must be referenced to the astronomicalObjects table when not null it is a foreign key the data is json and must handle the reading the data from the json object
    astronomicalObects_uid = db.Column(db.String, db.ForeignKey('astronomicalObjects.uid'), nullable=True)
    
    

class Organization(db.Model):
    """Creates an instance of an organization from the Star Trek universe for the database"""
    
    uid = db.Column(db.String, primary_key=True)
    
    name = db.Column(db.Text, nullable=False)
    
    government = db.Column(db.Boolean, nullable=False)
    
    intergovernmentalOrganization = db.Column(db.Boolean, nullable=False)
    
    researchOrganization = db.Column(db.Boolean, nullable=False)
    
    sportOrganization = db.Column(db.Boolean, nullable=False)
    
    medicalOrganization = db.Column(db.Boolean, nullable=False)
    
    militaryOrganization = db.Column(db.Boolean, nullable=False)
    
    militaryUnit = db.Column(db.Boolean, nullable=False)
    
    governmentAgency = db.Column(db.Boolean, nullable=False)
    
    lawEnforcementAgency = db.Column(db.Boolean, nullable=False)
    
    prisonOrPenalColony = db.Column(db.Boolean, nullable=False)
    
    mirror = db.Column(db.Boolean, nullable=False)
    
    alternateReality = db.Column(db.Boolean, nullable=False)
    

class Occupation(db.Model):
    """Creates an instance of an occupation from the Star Trek universe for the database"""
    
    uid = db.Column(db.String, primary_key=True)
    
    name = db.Column(db.Text, nullable=False)
    
    legalOccupation = db.Column(db.Boolean, nullable=False)
    
    medicalOccupation = db.Column(db.Boolean, nullable=False)
    
    scientificOccupation = db.Column(db.Boolean, nullable=False)
    

# class SpacecraftClass(db.Model):
#     """Creates an instance of a spacecraft class from the Star Trek universe for the database these classes are used to create the spacecraft table"""
    
    
    

# class Spacecraft(db.Model):
#     """Creates an instance of a spacecraft from the Star Trek universe for the database"""
    
    
    
    
    
    
    


    
    
    
    

    


    
    
    
    
     
     
    
    