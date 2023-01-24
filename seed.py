import json

from models import db
from models_star_trek import Animal, Title
from app import app



db.drop_all()
db.create_all()
app.app_context().push()

Animal.query.delete()

# read the formatted_file.json
with open('data/animal.json') as json_file:
    data = json.load(json_file)
    for animal in data:
        if animal["feline"] == True:
            
            # animal["feline"] = True
            print(animal["name"])
        # print(type(animal))
        # db.session.add(animal)
        # db.session.commit()

with open('data/title.json') as json_file:
    data = json.load(json_file)
    for title in data:
        title = Title(**title)
        db.session.add(title)
        db.session.commit()
        



        

        
   
        







