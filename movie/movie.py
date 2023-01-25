

from flask import Blueprint, render_template, jsonify, request, redirect
from flask_assets import Environment

assets = Environment()



movie = Blueprint('movie', __name__, template_folder='templates', static_folder='static')




@movie.route('/all-movies')
def show_all_movies():
    """Shows all movies"""
    return render_template('all-movies.html')

