import json

from models import db
from models_star_trek import Animal
from app import app



db.drop_all()
db.create_all()
app.app_context().push()

# Animal.query.delete()

# read the formatted_file.json
with open('data/animal.json') as json_file:
    data = json.load(json_file)
    for animal in data:
        animal = Animal(
        uid = animal['uid'],
        name = animal['name'],
        earthAnimal = animal['earthAnimal'],
        earthInsect = animal['earthInsect'],
        avian = animal['avian'],
        canine = animal['canine']
        )
   
        







