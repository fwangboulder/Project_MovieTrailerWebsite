##########################################
# Project 1: Movie Website
# Date Started: 01/01/2017
# Date Completed: 01/02/2017
# Submitted by: Fang Wang
##########################################

######################################## Media File ####################################################
# Description: This file creates the class Movie to allow for instances of this class to be used in the
#              entertainment.py file. This definition of the class Movie was obtained through the course
########################################################################################################

#!/usr/bin/env python
import webbrowser


class Movie():

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
