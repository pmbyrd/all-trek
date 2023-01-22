
# *Configure imports
# !
# !Double check that all imports are correct
# !
from flask import Flask, render_template, request, redirect, url_for, flash, sessions, g, jsonify
import os
import json




app = Flask(__name__)

app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', "will change later")
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL','postgresql:///trek')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = False
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0 #!don't know if this is necessary
app.config['API_KEY'] = os.environ.get('API_KEY', "/config.json") #!don't know if this is configured correctly
app.config.from_file("config.json", load=json.load)


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
