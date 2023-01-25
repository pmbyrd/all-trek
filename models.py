"""This module contains the flask models for the database."""
# *Importing the required modules

from flask_sqlalchemy import SQLAlchemy
from flask_assets import Environment, Bundle
from flask import Flask
import json


# *Intialize db connection

db = SQLAlchemy()

assets = Environment()

def connect_db(app):
    """Connection to the database that is called in app.py for the Flask app to use."""
    db.app = app
    db.init_app(app)
    
def get_api_key():
    """Gets the api key from config.json"""
    with open('config.json', 'r') as f:
        config = json.load(f)
    api_key = config['API_KEY']
    
    return api_key

def create_app():
    app = Flask(__name__)
    assets.init_app(app)
    return app

def register_assets(assets, asset_path):
    js = Bundle('js/jquery-3.5.1.min.js', 'js/bootstrap.min.js', 'js/main.js', filters='jsmin', output='gen/packed.js')
    assets.register('js_all', js)
    
    




   

    
    
    
    
    
    

    
    
    
    
    


    
    
    
    

    
    