import requests
import json

import pandas as pd
import numpy as np

# Authentication details
API_KEY_V3 = "?api_key=a7a2e525605101bd1d5d5ebb64f9baa1"
API_READ_ACCESS_TOKEN_V4 = "eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJhN2EyZTUyNTYwNTEwMWJkMWQ1ZDVlYmI2NGY5YmFhMSIsInN1YiI6IjYyMmY0MjI0OThmMWYxMDA3ODA4NzkzYSIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.YWIfwRRCzEnpJN9bfnSyCRFhbf7l4qs3q3eoP5_yVHE"

# api request structure
sample_url = "https://api.themoviedb.org/3/movie/550?api_key=5508d6f139fd30407092694bbf4d30e0"

# domain (root url) used for all API requests
ROOT_URL_V3 = "https://api.themoviedb.org/3"

# get essential metadata on a single movie
def get_movie(movie_id: int):
    """
    INPUTS:
        id:     (Integer) an integer representing the unique ID of a movie
    
    OUTPUTS:
                (pandas Series) a series of essential data associated with the movie
    """
    url = ROOT_URL_V3 + "/movie/" + str(movie_id) + API_KEY_V3
    
    r = requests.get(url)

    return pd.Series(r.json())
    
# get essential metadata on a list of movies
def get_movie_list(ls: list):
    """
    INPUTS:
        ls:     (List) a list containing movie IDs
    
    OUTPUTS:
                (pandas DataFrame) tabulated data of each movie in ls
    """

    movies = []
    for id in ls:
        movies.append(get_movie(id))
    
    return pd.DataFrame(movies)

# get credits data on a single movie
def get_credits(movie_id: int):
    """
    INPUTS:
        id:     (Integer) an integer representing the unique ID of a movie
    
    OUTPUTS:
                (pandas Series) a series of credits data associated with the movie
    """
    url = ROOT_URL_V3 + "/movie/" + str(movie_id) + "/credits" + API_KEY_V3

    r = requests.get(url)

    return pd.Series(r.json())

# get credits data on a list of movies
def get_credits_list(ls: list):
    """
    INPUTS:
        ls:     (List) a list containing movie IDs
    
    OUTPUTS:
                (pandas DataFrame) tabulated credits data of each movie in ls
    """

    movie_credits = []
    for id in ls:
        movie_credits.append(get_credits(id))

    return pd.DataFrame(movie_credits)

def get_movie_long(movie_id: int):
    """
    INPUTS:
        id:     (Integer) an integer representing the unique ID of a movie
    
    OUTPUTS:
                (pandas Series) the metadata, credits, and keywords associated with the movie
    """
    # we make use of the append_to_response feature as described in docs
    # https://developers.themoviedb.org/3/getting-started/append-to-response

    url = ROOT_URL_V3 + "/movie/" + str(movie_id) + API_KEY_V3 + "&append_to_response=credits,keywords&language=en"

    r = requests.get(url)

    return pd.Series(r.json())

def get_movies_long(ls: list):
    """
    INPUTS:
        ls:     (List) a list containing movie IDs
    
    OUTPUTS:
                (pandas DataFrame) tabulated data (metadata, credits, keywords) of each movie in ls
    """

    i = 0
    movies = []
    for id in ls:
        print("Downloading Data (Line {})".format(i))
        movies.append(get_movie_long(id))
        i += 1
    
    return pd.DataFrame(movies)