import media
import fresh_tomatoes

toy_story = media.Movie("Toy Story",
	"A cowboy doll is profoundly threatened and jealous when a new spaceman figure supplants him as top toy in a boy's room.",
	"https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
	"https://www.youtube.com/watch?v=KYz2wyBy3kc")

avatar = media.Movie("Avatar",
	"A paraplegic marine dispatched to the moon Pandora on a unique mission becomes torn between following his orders and protecting the world he feels is his home.",
	"https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",
	"https://www.youtube.com/watch?v=aVdO-cx-McA")

civial_war = media.Movie("Civil war",
	"Political interference in the Avengers' activities causes a rift between former allies Captain America and Iron Man.",
	"https://upload.wikimedia.org/wikipedia/en/5/53/Captain_America_Civil_War_poster.jpg",
	"https://www.youtube.com/watch?v=dKrVegVI0Us")

fabricated_city = media.Movie("Fabricated city",
	"In real life, Kwon Yoo (Ji Chang-wook) is unemployed, but in the virtual world he is recognized as a top gamer with no rival.",
	"https://upload.wikimedia.org/wikipedia/en/4/47/Fabricated_City_Poster.jpg",
	"https://www.youtube.com/watch?v=2CfVL6WLvUg")

the_intern = media.Movie("The Intern",
	"70-year-old widower Ben Whittaker has discovered that retirement isn't all it's cracked up to be. Seizing an opportunity to get back in the game, he becomes a senior intern at an online fashion site, founded and run by Jules Ostin.", 
	"https://upload.wikimedia.org/wikipedia/en/c/c9/The_Intern_Poster.jpg",
	"https://www.youtube.com/watch?v=ZU3Xban0Y6A")

you_are_the_apple_of_my_eye = media.Movie("You are the apple of my eye",
	"A group of close friends who attend a private school all have a debilitating crush on the sunny star pupil, Shen Jiayi. The only member of the group who claims not to is Ke Jingteng, but he ends up loving her as well.",
	"https://upload.wikimedia.org/wikipedia/en/a/aa/You_Are_the_Apple_of_My_Eye_film_poster.jpg",
	"https://www.youtube.com/watch?v=FyRysi1Vovs")

movies = [toy_story, avatar, civial_war, fabricated_city, the_intern, you_are_the_apple_of_my_eye]
fresh_tomatoes.open_movies_page(movies)
