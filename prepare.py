import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split


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

    df_clean = df = df.dropna(subset=['player_1_aces'])
    
    return df

def split_data(df):
    '''
    Takes in a dataframe and returns train, validate, and test subset dataframes. 
    '''
    train, test = train_test_split(df, test_size = .2, random_state = 123)
    train, validate = train_test_split(train, test_size = .3, random_state = 123)
    
    return train, validate, test