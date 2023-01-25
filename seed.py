"""
    This file is used to the database with the data from the json files.
    
    1. Drop all tables
    2. Create all tables
    3. Use helper functions to read the json files and add the data to the database
   
"""
import json

from models import db
from models_star_trek import Animal, Title, Location, AstronomicalObject, Character, Performer, Element, Conflict, Weapon, Food, Technology, Company, Staff, Species, Organization, Occupation, SpacecraftClass, Spacecraft
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
        json_file.close()

print("Animal added to database.")
        

with open('data/title.json') as json_file:
    data = json.load(json_file)
    for title in data:
        title = Title(**title)
        db.session.add(title)
        db.session.commit()
        json_file.close()

print("Title added to database.")
        
        
with open('data/astronomicalObject.json') as json_file:
    data = json.load(json_file)
    for astronomicalObject in data:
        astronomicalObject = AstronomicalObject(**astronomicalObject)
        db.session.add(astronomicalObject)
        db.session.commit()
        json_file.close()

print("Astronomical Object added to database.")
        

with open('data/location.json') as json_file:
    data = json.load(json_file)
    for location in data:
        location = Location(**location)
        db.session.add(location)
        db.session.commit()
        json_file.close()

print("Location added to database.")
        

with open('data/character.json') as json_file:
    data = json.load(json_file)
    for character in data:
        character = Character(**character)
        db.session.add(character)
        db.session.commit()
        json_file.close()

print("Character added to database.")
        
        
with open ('data/performer.json') as json_file:
    data = json.load(json_file)
    for performer in data:
        performer = Performer(**performer)
        db.session.add(performer)
        db.session.commit()
        json_file.close()

print("Performer added to database.")
        
        
with open('data/element.json') as json_file:
    data = json.load(json_file)
    for element in data:
        element = Element(**element)
        db.session.add(element)
        db.session.commit()
        json_file.close()
          
print("Element added to database.")


with open('data/conflict.json') as json_file:
    data = json.load(json_file)
    for conflict in data:
        conflict = Conflict(**conflict)
        db.session.add(conflict)
        db.session.commit()
        json_file.close()
    
print("Conflict added to database.")


with open('data/weapon.json') as json_file:
    data = json.load(json_file)
    for weapon in data:
        weapon = Weapon(**weapon)
        db.session.add(weapon)
        db.session.commit()
        json_file.close()
        
print("Weapon added to database.")
        
        
with open('data/food.json') as json_file:
    data = json.load(json_file)
    for food in data:
        food = Food(**food)
        db.session.add(food)
        db.session.commit()
        json_file.close()
        
print("Food added to database.")


with open('data/technology.json') as json_file:
    data = json.load(json_file)
    for technology in data:
        technology = Technology(**technology)
        db.session.add(technology)
        db.session.commit()
        json_file.close()
        
print("Technology added to database.")


with open('data/company.json') as json_file:
    data = json.load(json_file)
    for company in data:
        company = Company(**company)
        db.session.add(company)
        db.session.commit()
        json_file.close()
        
print("Company added to database.")


with open('data/staff.json') as json_file:
    data = json.load(json_file)
    for staff in data:
        staff = Staff(**staff)
        db.session.add(staff)
        db.session.commit()
        json_file.close()

print("Staff added to database.")

with open('data/species.json') as json_file:
    data = json.load(json_file)
    for species in data:
        species_obj = Species(**species)
        db.session.merge(species_obj)
    db.session.commit()
    json_file.close()

        
print("Species added to database.")


with open('data/organization.json') as json_file:
    data = json.load(json_file)
    for organization in data:
        organization = Organization(**organization)
        db.session.add(organization)
        db.session.commit()
        json_file.close()
        
print("Organization added to database.")


with open('data/occupation.json') as json_file:
    data = json.load(json_file)
    for occupation in data:
        occupation = Occupation(**occupation)
        db.session.add(occupation)
        db.session.commit()
        json_file.close()
        
print("Occupation added to database.")


with open('data/spacecraftClass.json') as json_file:
    data = json.load(json_file)
    for spacecraftClass in data:
        spacecraftClass = SpacecraftClass(**spacecraftClass)
        db.session.add(spacecraftClass)
        db.session.commit()
        json_file.close()
   
with open('data/spacecraft.json') as json_file:
    data = json.load(json_file)
    for spacecraft in data:
        spacecraft = Spacecraft(**spacecraft)
        db.session.add(spacecraft)
        db.session.commit()
        json_file.close()
        








