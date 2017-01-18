import media
import fresh_tomatoes
import requests
import tmdbsimple as tmdb
import json

#Api Key for The Movie DB
tmdb.API_KEY = "030f4b9077820a1b72901fa807812b03"

#URL for a 'collection' (A group of movies on the TMDB website - eg. Star Wars movies, Indiana Jones films etc.)
collectionURL = "https://api.themoviedb.org/3/collection/10194?language=en-US&api_key=030f4b9077820a1b72901fa807812b03"

#Use requests to get a response from
response = requests.request("GET", collectionURL)

collection = json.loads(response.text)

movies = []

#In the JSON object collection, 'parts' contains a list of movies.
#Loop through these movies and add an instance of the class Movie for each JSON object
for movie in collection['parts']:

    fullPosterPath = "https://image.tmdb.org/t/p/w1280" + movie['poster_path']
    movies.append((media.Movie(movie['title'], movie['overview'],
                               fullPosterPath,
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc")))

#Fresh Tomatoes do your thang
fresh_tomatoes.open_movies_page(movies)
