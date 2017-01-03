#!/usr/bin/env python
import webbrowser


class Movie():
    """This is a Movie class with title, story line, poster image and
    youtube trailer url. It contains one method to show trailer."""

    VALID_RATINGS = ['G', 'PG', 'PG-13', 'R']

    def __init__(
            self,
            movie_title,
            movie_story_line,
            poster_image,
            trailer_youtube):
        self.title = movie_title
        self.story_line = movie_story_line
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
