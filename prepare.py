import pandas as pd
import numpy as np


def prepare_atp():

    # read .csv into a dataframe
    df = pd.read_csv('ATPMain.csv', index_col = 0)

    # set index to the tournament start date
    df = df.set_index('tourney_date')

    # convert index to datetime object and sort in ascending order
    df.index = pd.to_datetime(df.index, format = '%Y%m%d')
    df = df.sort_index(ascending = True)

    # drop all walkovers (no useful stats) and best of 1 matches (extremely rare format)
    df = df.drop(df[df.score == 'W/O'].index)
    df = df.drop(df[df.best_of == 1].index)

    return df

