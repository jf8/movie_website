import webbrowser


class Movie():
    """Creates instances of a movie."""

    def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube, year):
        """Initianize class variables for movie title, storyline, poster
           image, Youtube trailer, and year."""
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_url = trailer_youtube
        self.year = year

    def show_trailer(self):
        """Opens movie trailer URL."""
        webbrowser.open(self.trailer_url)