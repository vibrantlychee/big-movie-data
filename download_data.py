from tmdb import get_movie, get_movies_long

import pandas as pd

# assume March 10th, 2022
DATE = "03_10_2022"

# path to daily export file (list of valid movie IDs)
filepath = "raw-data/movie_ids_" + DATE + ".json"

# load export file as dataframe
with open(filepath) as f:
    export_list = pd.read_json(f, lines=True)

# sort by popularity
export_list.sort_values(by="popularity", ascending=False,inplace=True)

# we restrict to 5000 most popular movies as the TMDB API slows down after ~5000 calls
top_5000 = export_list[0:5000]
# random sample should contain mostly movies that you have heard of
# print(top_5000.sample(10))

# get list of movie IDs
ls_of_ids = list(top_5000["id"])

# request all metadata, credits data, and keyword data for every movie in ls_of_ids
all_data = get_movies_long(ls_of_ids)

# write data into csv form
all_data.to_csv("raw-data/20220310.csv", index=False)