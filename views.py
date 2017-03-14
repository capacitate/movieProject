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


@app.route('/addMovie', methods=['POST'])
def getTest():
    # Get form input.
    newTitle = request.form['title']
    newMovie_storyline = request.form['movie_storyline']
    newPoster_image_url = request.form['poster_image_url']
    newTrailer_youtube_url = request.form['trailer_youtube_url']
    newMovie = Movie(
        title=newTitle, movie_storyline=newMovie_storyline,
        poster_image_url=newPoster_image_url,
        trailer_youtube_url=newTrailer_youtube_url)

    # Check if the text box is empty or not.
    # All four rows are required.
    if not newTitle:
        return 'No movie title!'

    if not newMovie_storyline:
        return 'No movie storyline'

    if not newPoster_image_url:
        return 'No movie poster image url'

    if not newTrailer_youtube_url:
        return 'No movie trailer url'

    # Check duplicate movie title.
    isNewMovie = session.query(Movie).filter_by(title=newMovie.title).first()
    if isNewMovie:
        return 'Duplicate movie!'

    session.add(newMovie)
    session.commit()

    movies = session.query(Movie).all()
    fresh_tomatoes.open_movies_page(movies)
    return 'OK'

if __name__ == '__main__':
    app.debug = True
    app.run(host='localhost', port=5004)

