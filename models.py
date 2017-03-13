from flask_sqlalchemy import SQLAlchemy

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column,Integer,String
from sqlalchemy import create_engine

Base = declarative_base()

class Movie(Base):
	__tablename__ = 'Movie'
	id = Column(Integer, primary_key = True)
	title = Column(String, unique=True, nullable=False)
	movie_storyline = Column(String, nullable=False)
	poster_image_url = Column(String, nullable=False)
	trailer_youtube_url = Column(String, nullable=False)
	@property
	def serialize(self):
		return {
			'title': self.title,
			'story': self.movie_storyline,
			'poster': self.poster_image_url,
			'trailer_youtube_url': self.trailer_youtube_url
		}

	def show_trailer(self):
		webbrowser.open(self.trailer_youtube)

engine = create_engine('sqlite:///movie.db')

Base.metadata.create_all(engine)