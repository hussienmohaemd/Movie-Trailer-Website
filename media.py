import webbrowser
'''this file contain the main class of movies that all films represent it
and called instances'''


class Movie():
	
	    """ Relevant information for a single movie to display
    Attributes:
        title: movie title
        poster_image_url: the url of the poster image
        trailer_youtube_url: the youtube trailer url
    """

    def __init__(self, movie_title, poster_image, trailer_youtube):
        self.title = movie_title
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
