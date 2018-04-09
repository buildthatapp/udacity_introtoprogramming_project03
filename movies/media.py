import webbrowser


class Movie():
    """This class will create a movie object which can store a movie's title,
    storyline, poster, and youtube trailer.

    This class has two public attributes. __init__ serves as a constructor
    that accepts parameters. Show_trailer serves as a public attribute that
    will open a movie object's youtube trailer by calling webbrowser.open
    on the movie object's youtube trailer url.

    Attributes:
        __init__ (obj, str, str, str,str): Default constructor.
        show_trailer(obj): Opens trailer_youtube.url in webbrowser.

    """
    def __init__(self, movie_title, movie_storyline,
    	         poster_image, trailer_youtube):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
