"""
    This file is used to the database with the data from the json files.
    
    1. Drop all tables
    2. Create all tables
    3. Use helper functions to read the json files and add the data to the database
   
"""
import json

from models import db
from models_star_trek import Animal, Title, Location, AstronomicalObject, Character
from app import app




db.drop_all()
db.create_all()
app.app_context().push()

Animal.query.delete()



with open('data/animal.json') as json_file:
    data = json.load(json_file)
    for animal in data:
        animal = Animal(**animal)
        db.session.add(animal)
        db.session.commit()
        # close the json file
        json_file.close()
        

with open('data/title.json') as json_file:
    data = json.load(json_file)
    for title in data:
        title = Title(**title)
        db.session.add(title)
        db.session.commit()
        json_file.close()
        
with open('data/astronomicalObject.json') as json_file:
    data = json.load(json_file)
    for astronomicalObject in data:
        astronomicalObject = AstronomicalObject(**astronomicalObject)
        print(astronomicalObject.location)
        db.session.add(astronomicalObject)
        db.session.commit()
        json_file.close()

with open('data/location.json') as json_file:
    data = json.load(json_file)
    for location in data:
        location = Location(**location)
        db.session.add(location)
        db.session.commit()
        json_file.close()

with open('data/character.json') as json_file:
    data = json.load(json_file)
    for character in data:
        character = Character(**character)
        db.session.add(character)
        db.session.commit()
        json_file.close()

    

        



        

        
   
        







