import pandas as pd

# to store methods to prepare data for running models

# # creates a new one-hot encoded dataframe based on any column
# def one_hot(df: pd.DataFrame, col: str):
#     """
#     INPUTS:
#         df:     (pd.DataFrame) a dataframe
#         col:    (str) the name of a column in df
#     OUTPUTS:
#                 (pd.DataFrame) a dataframe one-hot encoded according to col
#     """
#     # flatten data on col
#     flat_df = flatten(df, col)
    
#     # compute one hot encoding using str.get_dummies
#     return flat_df.set_index("movie_id")[col + "_name"].str.get_dummies().groupby(level=0).sum()
    
# creates a flat dataframe based on any column (except cast or crew)
def flatten(df: pd.DataFrame, cols: list):
    """
    INPUTS:
        df:     (pd.DataFrame) a dataframe
        cols:   (list) list of column names in df
    OUTPUTS:
                (pd.DataFrame) a dataframe flattened according to cols
    """

    for col in cols:
        df = df.explode(col)
    
    return df

# # creates a flat dataframe based on any column
def flatten_people(df: pd.DataFrame, col: str):
    """
    INPUTS:
        df:     (pd.DataFrame) a dataframe
        col:    (str) cast or crew
    OUTPUTS:
                (pd.DataFrame) a dataframe flattened according to col
    """

    ls_of_temps = []
    for i in range(0, df.shape[0], 1):
        temp_df = pd.json_normalize(df[col][i])
        temp_df["movie_id"] = df["id"][i]
        temp_df["movie_title"] = df["title"][i]

        temp_df.columns = [col + "_tmdb_" + x if x == "id" else x for x in temp_df.columns]
        temp_df.columns = [col + "_" + x if x == "name" else x for x in temp_df.columns]
        
        ls_of_temps.append(temp_df)
    
    return pd.concat(ls_of_temps)


# creates a new one-hot encoded dataframe based on any column
def one_hot(df: pd.DataFrame, cols: list):
    """
    INPUTS:
        df:     (pd.DataFrame) a dataframe
        cols:   (list) list of column names in df
    OUTPUTS:
                (pd.DataFrame) a dataframe one-hot encoded according to cols
    """
    # flatten data on col
    flat_df = flatten(df, cols)
    
    # one-hot encode flat_df using pd.get_dummies()
    return pd.get_dummies(flat_df, columns=cols).groupby(flat_df.index).max()
    
