"""This module contains the models for the database, user, post, tag, post_tag."""
# *Importing the required modules
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
# from star_trek_models import *
# from user_models import *

# *Intialize db connection

db = SQLAlchemy()
def connect_db(app):
    """Connection to the database that is called in app.py for the Flask app to use."""
    db.app = app
    db.init_app(app)
    

    



   

    
    
    
    
    
    

    
    
    
    
    


    
    
    
    

    
    