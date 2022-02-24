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

    # set dataframe to years 1999-2019 (21 years of recent data minus corona years)
    df = df['1999-01-01':'2020-01-01']

    # create target variable 
    df['player_1_wins'] = np.where(df['winner'] == df['player_1_name'], True, False)
    
    # drop all walkovers (no useful stats) and best of 1 matches (extremely rare format)
    df = df.drop(df[df.score == 'W/O'].index)
    df = df.drop(df[df.best_of == 1].index)

    # drop janky records
    df = df[df['player_1_first_serve_%'].notnull()]
    df = df[df['player_2_first_serve_%'].notnull()]

    # gather all players in two sets
    players = set(list(df.player_1.unique()))
    players2 = set(list(df.player_2.unique()))

    # combine, drop duplicates, convert set to list type and sort for fun 
    players = players.union(players2)
    players = list(players)
    players.sort()

    # set an empty list to fill
    less_than_50 = []

    # use a for-loop to run through the list of players
    for player in players:
        # set up if-conditional to see if the length of records where a player shows up in the dataframe is less than 50
        if len(df[(df.player_1 == player) | (df.player_2 == player)]) < 50:
            # if there are less than 50 records, add the player's name to the list
            less_than_50.append(player)
    # sort list
    less_than_50.sort()

    # run through loop of list of players with less than 50 matches
    for player in less_than_50:
        # set dataframe to records where these players are not present
        df = df[df.player_1 != player]
        df = df[df.player_2 != player]

    df_clean = df = df.dropna(subset=['player_1_aces'])

    # create dummy columns for surface, level, hand, and round 
    dummy_df = pd.get_dummies(df[['surface', 'tourney_level', 'player_1_hand', 'player_2_hand', 'round']], dummy_na=False, drop_first=[False])
    # concat dummy columns to df
    df = pd.concat([df, dummy_df], axis=1)
    
    return df

def split_data(df):
    from sklearn.model_selection import train_test_split
    '''
    Takes in a dataframe and returns train, validate, and test subset dataframes. 
    '''
    train, test = train_test_split(df, test_size = .2, random_state = 123)
    train, validate = train_test_split(train, test_size = .3, random_state = 123)
    
    return train, validate, test

def calculate_column_nulls(df):

    '''
    This function  defines one parameter, a dataframe, and returns a dataframe that holds data regarding null values and ratios (pertaining to the whole column) 
    in the original frame.
    '''   
    
    output = []    # set an empty list
    df_columns = df.columns.to_list()   # gather columns

    for column in df_columns:   # commence for-loop
        missing = df[column].isnull().sum()    # assign variable to number of rows that have null values
        ratio = missing / len(df)   # assign variable to ratio of rows with null values to overall rows in column
        # assign a dictionary for your dataframe to accept       
        r_dict = {'nulls': missing,
                  'null_ratio': round(ratio, 5),
                  'null_percentage': f'{round(ratio * 100, 2)}%'
                 }
        output.append(r_dict)   # add dictonaries to list

    column_nulls = pd.DataFrame(output, index = df_columns)    # design frame
    column_nulls = column_nulls.sort_values('nulls', ascending = False)    # sort

    return column_nulls

def calculate_row_nulls(df):

    '''
    This function  defines one parameter, a dataframe, and returns a dataframe that holds data regarding null values and ratios (pertaining to the whole row) 
    in the original frame.
    '''   
    
    output = []    # create an empty list
    nulls = df.isnull().sum(axis = 1)   # gather values in a series
    for n in range(len(nulls)):    # commence 4 loop
        missing = nulls[n]     # assign variable to nulls
        ratio = missing / len(df.columns)   # assign variable to ratio
        # assign a dictionary for your dataframe to accept
        r_dict = {'nulls': missing,
                  'null_ratio': round(ratio, 5),
                  'null_percentage': f'{round(ratio * 100)}%'
                 }
        output.append(r_dict)   # add dictonaries to list

    row_nulls = pd.DataFrame(output, index = df.index)    # design frame
    row_nulls = row_nulls.sort_values('nulls', ascending = False)   # sort

    return row_nulls 