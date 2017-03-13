from models import Base, Movie
import fresh_tomatoes

from sqlalchemy import create_engine
from sqlalchemy.orm import relationship, sessionmaker

engine = create_engine('sqlite:///movie.db')

Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()

toy_story = Movie(title = "Toy Story",
	movie_storyline = "A cowboy doll is profoundly threatened and jealous when a new spaceman figure supplants him as top toy in a boy's room.",
	poster_image_url = "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
	trailer_youtube_url = "https://www.youtube.com/watch?v=KYz2wyBy3kc")

avatar = Movie(title = "Avatar",
	movie_storyline = "A paraplegic marine dispatched to the moon Pandora on a unique mission becomes torn between following his orders and protecting the world he feels is his home.",
	poster_image_url = "https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",
	trailer_youtube_url = "https://www.youtube.com/watch?v=aVdO-cx-McA")

civial_war = Movie(title = "Civil war",
	movie_storyline = "Political interference in the Avengers' activities causes a rift between former allies Captain America and Iron Man.",
	poster_image_url = "https://upload.wikimedia.org/wikipedia/en/5/53/Captain_America_Civil_War_poster.jpg",
	trailer_youtube_url = "https://www.youtube.com/watch?v=dKrVegVI0Us")

fabricated_city = Movie(title = "Fabricated city",
	movie_storyline = "In real life, Kwon Yoo (Ji Chang-wook) is unemployed, but in the virtual world he is recognized as a top gamer with no rival.",
	poster_image_url = "https://upload.wikimedia.org/wikipedia/en/4/47/Fabricated_City_Poster.jpg",
	trailer_youtube_url = "https://www.youtube.com/watch?v=2CfVL6WLvUg")

the_intern = Movie(title = "The Intern",
	movie_storyline = "70-year-old widower Ben Whittaker has discovered that retirement isn't all it's cracked up to be. Seizing an opportunity to get back in the game, he becomes a senior intern at an online fashion site, founded and run by Jules Ostin.", 
	poster_image_url = "https://upload.wikimedia.org/wikipedia/en/c/c9/The_Intern_Poster.jpg",
	trailer_youtube_url = "https://www.youtube.com/watch?v=ZU3Xban0Y6A")

you_are_the_apple_of_my_eye = Movie(title = "You are the apple of my eye",
	movie_storyline = "A group of close friends who attend a private school all have a debilitating crush on the sunny star pupil, Shen Jiayi. The only member of the group who claims not to is Ke Jingteng, but he ends up loving her as well.",
	poster_image_url = "https://upload.wikimedia.org/wikipedia/en/a/aa/You_Are_the_Apple_of_My_Eye_film_poster.jpg",
	trailer_youtube_url = "https://www.youtube.com/watch?v=FyRysi1Vovs")

movies = [toy_story, avatar, civial_war, fabricated_city, the_intern, you_are_the_apple_of_my_eye]

# Put default movie list on database.
# If default movie lists are already in database, then read db and show to the user.
for movie in movies:
	isNewMovie = session.query(Movie).filter_by(title = movie.title).first()	
	if not isNewMovie:
		session.add(movie)
		session.commit()
	else:
		movies = session.query(Movie).all()
		break

fresh_tomatoes.open_movies_page(movies)
