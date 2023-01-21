
# *Configure imports
# !
# !Double check that all imports are correct
# !
from flask import Flask, render_template, request, redirect, url_for, flash, sessions, g, jsonify
import os

app = Flask(__name__)

app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', "will change later")
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL','postgresql:///trek')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = False
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0 #!don't know if this is necessary

@app.route('/')
def root():
    """Root route"""
    return render_template('index.html')

@app.route('/home')
def home():
    """Home route"""
    return render_template('index.html')
