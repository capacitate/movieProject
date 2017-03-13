from flask import Flask, request, jsonify
from models import Base, Movie
from sqlalchemy import create_engine
from sqlalchemy.orm import relationship, sessionmaker

import fresh_tomatoes

engine = create_engine('sqlite:///movie.db')

Base.metadata.bind = engine
DBsession = sessionmaker(bind=engine)
session = DBsession()

app = Flask(__name__)

# Check the user input is appropriate
# Maybe I can use HTML error code to indicate something wrong
# All four rows are required
@app.route('/addMovie', methods=['POST'])
def getTest():
	# Get form input. 
	newTitle = request.form['title']
	newMovie_storyline = request.form['movie_storyline']
	newPoster_image_url = request.form['poster_image_url']
	newTrailer_youtube_url = request.form['trailer_youtube_url']
	newMovie = Movie(title = newTitle,
	movie_storyline = newMovie_storyline,
	poster_image_url = newPoster_image_url,
	trailer_youtube_url = newTrailer_youtube_url)

	# Check if the text box is empty or not.
	isNewMovie = session.query(Movie).filter_by(title = newMovie.title).first()	
	if not isNewMovie:
		print (newTitle)
		session.add(newMovie)
		session.commit()
	
	movie_items = session.query(Movie).all()
	fresh_tomatoes.open_movies_page(movie_items)
	return 'OK'


@app.route('/')
def reloadDB():
	movies = session.query(Movie).all()
	# Wrap with movie object from media.
	print (movies)
	# allMovies = []
	# for movie in movies:
	# 	allMovies.extend()
	fresh_tomatoes.open_movies_page()

if __name__ == '__main__':
	app.debug = True
	app.run(host='localhost', port=5004)