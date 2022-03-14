from matplotlib import lines
from tmdb import get_movie, get_movies_long

import pandas as pd

# assume March 10th, 2022
DATE = "03_10_2022"

# path to daily export file (list of valid movie IDs)
filepath = "raw-data/movie_ids_" + DATE + ".json"

# load export file as dataframe
with open(filepath) as f:
    export_list = pd.read_json(f, lines=True)

# get list of valid movie IDs (~686k)
ls_of_ids = list(export_list["id"])

# request all metadata, credits data, and keyword data for every movie in ls_of_ids
all_data = get_movies_long(ls_of_ids)

# write data into csv form
all_data.to_csv("raw-data/20220310.csv", index=False)