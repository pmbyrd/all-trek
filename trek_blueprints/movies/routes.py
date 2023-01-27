"""Handles routes for the movies blueprint."""

from flask import Flask, Blueprint, render_template, request, redirect, url_for
# import os, sys; sys.path.append(os.path.dirname(os.path.realpath(__file__)))




movie_bp = Blueprint(
    'movies', __name__, 
    template_folder='templates',
    static_folder='static',
    static_url_path='/movies/static'
)

@movie_bp.route('/movies')
def show_movies():
    """Show all movies."""
    # *here the we pass over the movie titles to be queried and return as json to the front end
    # *the frontend will query the api and display the movies
   
    # return render_template('movies.html')
    return render_template('movies.html')

@movie_bp.route('/movies/all')
def show_all_movies():
    """Show all movies."""
    # *here the we pass over the movie titles to be queried and return as json to the front end
    # *the frontend will query the api and display the movies
    # return render_template('movies.html')
    return f"Here are all the movies. ENJOY!!!!"