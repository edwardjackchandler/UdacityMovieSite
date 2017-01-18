import webbrowser


class Movie():

    def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube_url):
        """Represents a movie.

           Keyword arguments:
           movie_title -- the title
           movie_storyline -- the storyline
           psoter_image -- link to an image of the movie poster
           trailer_youtube_url -- url to the trailer of the movie on youtube
           """
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube_url

    def show_trailer(self):
        """Opens a webpage with the youtube trailer
        """
        webbrowser.open(self.trailer_youtube_url)