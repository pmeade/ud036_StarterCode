import fresh_tomatoes


class Movie:
    """
    class to hold movie data. This is a little weird since the class fields are
    really defined by their usage in fresh_tomatoes
    """
    def __init__(self, title, box_art_url, trailer_url):
        """This method creates a new movie
        :param title: title
        :type title: str

        :param box_art_url: URL of the box art
        :type box_art_url: str

        :param trailer_url: URL to the Youtube trailer
        :type trailer_url: str
        """
        self.title = title
        self.poster_image_url = box_art_url
        self.trailer_youtube_url = trailer_url

# instantiate three movies
highlander = Movie("Highlander",
                   "https://images-na.ssl-images-amazon.com/images/M/MV5BMjc3YmU3MzQtNTA4OC00ZjljLWFmODAtZDU1YzY5ZTNkZDU3XkEyXkFqcGdeQXVyNTAyODkwOQ@@._V1_.jpg",  # noqa
                   "https://www.youtube.com/watch?v=dQw4w9WgXcQ")
local_hero = Movie("Local Hero", "https://images-na.ssl-images-amazon.com/images/M/MV5BODhiMmM3YzQtZjMwNy00YTdkLTkwOTItZDhjYWE1ZTVlNmExXkEyXkFqcGdeQXVyMjI4MjA5MzA@._V1_.jpg",  # noqa
                   "https://www.youtube.com/watch?v=MQ8u4ytzPdA")
c_o_f_d = Movie("Cave of Forgotten Dreams",
                "https://images-na.ssl-images-amazon.com/images/M/MV5BMTYxNDExMzUwMl5BMl5BanBnXkFtZTcwNjM2MzYwNQ@@._V1_SY1000_CR0,0,674,1000_AL_.jpg",  # noqa
                "https://www.youtube.com/watch?v=kULwsoCEd3g")

# Store the movies in a list
movie_col = [highlander, local_hero, c_o_f_d]

# Pass the list to fresh_tomatoes to display as html
fresh_tomatoes.open_movies_page(movie_col)
