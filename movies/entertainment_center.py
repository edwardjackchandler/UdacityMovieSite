import media
import fresh_tomatoes
import requests
import tmdbsimple as tmdb
import json

tmdb.API_KEY = "030f4b9077820a1b72901fa807812b03"
endOfCollection = 0

collectionURL = "https://api.themoviedb.org/3/collection/10194?language=en-US&api_key=030f4b9077820a1b72901fa807812b03"

res = requests.get(collectionURL)

payload = "{}"
response = requests.request("GET", collectionURL, data=payload)

collection = json.loads(response.text)

movies = []

for movie in collection['parts']:

    fullPosterPath = "https://image.tmdb.org/t/p/w1280" + movie['poster_path']
    movies.append((media.Movie(movie['title'], movie['overview'],
                               fullPosterPath,
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc")))

fresh_tomatoes.open_movies_page(movies)
