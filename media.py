import webbrowser

class Movie():
	""" This class has store movie information. """
	VALID_RATINGS = ["G", "PG", "PG-13", "R"]

	def __init__(self, movie_title, movie_storyline, poster_image_url, trailer_youtube_url):
		self.title = movie_title
		self.movie_storyline = movie_storyline
		self.poster_image_url = poster_image_url
		self.trailer_youtube_url = trailer_youtube_url

	def show_trailer(self):
		webbrowser.open(self.trailer_youtube)

class FavoriteMovie(Movie):
	""" This class indicate favorite movie information. """
	def __init__(self, movie_title, movie_storyline, poster_image_url, trailer_youtube_url, ratings):
		Movie.__init__(self, movie_title, movie_storyline, poster_image_url, trailer_youtube_url)
		self.ratings = ratings
		