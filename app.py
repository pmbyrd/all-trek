
# *Configure imports
# !
# !Double check that all imports are correct
# !
from flask import Flask, render_template, request, redirect, url_for, flash, session, g, jsonify
from models import db, connect_db
from star_trek_models import Movie, Actor, Character
import os
import json
from trek_blueprints.movies.routes import movie_bp
from trek_blueprints.admin.routes import admin_bp





app = Flask(__name__)

app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', "will change later")
# app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///trek'
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL','postgresql:///trek')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = False
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0 #!don't know if this is necessary
app.config['API_KEY'] = os.environ.get('API_KEY', "/config.json") #!don't know if this is configured correctly
app.config.from_file("config.json", load=json.load)



with app.app_context().push():
    db.init_app(app)
    db.create_all()


connect_db(app)




# register the blueprints
app.register_blueprint(movie_bp)
app.register_blueprint(admin_bp)


@app.route('/api_key')
def api_key():
    """Gets the api key from config.json"""
    with open('config.json', 'r') as f:
        config = json.load(f)
    api_key = config['API_KEY']
    
    return jsonify(api_key=api_key)

@app.route('/')
def root():
    """Root route"""
    return redirect('/home')

@app.route('/home')
def home():
    """Home route"""
    return render_template('index.html')
