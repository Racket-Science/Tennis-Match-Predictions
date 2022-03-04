import numpy as np
import pandas as pd


def prepare_atp():

    # read .csv into a dataframe
    df = pd.read_csv('ATPMain.csv', index_col = 0)

    # sort your life out, m8
    df = df.sort_values(by = ['tourney_date', 'tourney_id', 'match_num'])
    df = df.reset_index().drop(columns = 'index')

    # make tourney date a datetime object
    df.tourney_date = pd.to_datetime(df.tourney_date, format = '%Y%m%d')

    # set dataframe to years 1999-2019 (21 years of recent data minus corona years)
    df = df[(df.tourney_date > '1998-12-31') & (df.tourney_date < '2020-01-01')]
    df = df.reset_index().drop(columns = 'index')

    # drop all walkovers (no useful stats) and best of 1 matches (extremely rare format)
    df = df.drop(df[df.score == 'W/O'].index)
    df = df.drop(df[df.best_of == 1].index)

    # drop player entry columns, verify
    df = df.drop(columns = ['player_1_entry', 'player_2_entry'])

    # drop janky records
    df = df[df['player_1_first_serve_%'].notnull()]
    df = df[df['player_2_first_serve_%'].notnull()]
    df = df[df['player_1_first_serve_win_%'].notnull()]
    df = df[df['player_2_first_serve_win_%'].notnull()]

    # assign variable to list of tourney ids that have missing minutes
    missing_minutes = list(df[df.minutes.isnull()].tourney_id.unique())
    # commence loop through list of tournaments with missing match lengths
    for tourney in missing_minutes:
        # assign mean match length for tournament to variable
        mean_match_length = df[df.tourney_id == tourney].minutes.mean()
        # locate index where there are mml for the tournament, fill values with average match length
        df.loc[df[df.tourney_id == tourney].minutes.isnull().index, 'minutes'] = mean_match_length

    ## generate subsets for data and group by match format and surface type
    # best of 3
    best_of_3_hard = df[(df.best_of == 3) & (df.surface == 'Hard')]
    best_of_3_clay = df[(df.best_of == 3) & (df.surface == 'Clay')]
    best_of_3_grass = df[(df.best_of == 3) & (df.surface == 'Grass')]
    best_of_3_carpet = df[(df.best_of == 3) & (df.surface == 'Carpet')]
    # best of 5
    best_of_5_hard = df[(df.best_of == 5) & (df.surface == 'Hard')]
    best_of_5_clay = df[(df.best_of == 5) & (df.surface == 'Clay')]
    best_of_5_grass = df[(df.best_of == 5) & (df.surface == 'Grass')]
    best_of_5_carpet = df[(df.best_of == 5) & (df.surface == 'Carpet')]

    # list subsets for a good ole fashion loop
    subsets = [
        best_of_3_hard,
        best_of_3_clay,
        best_of_3_grass,
        best_of_3_carpet,
        best_of_5_hard,
        best_of_5_clay,
        best_of_5_grass,
        best_of_5_carpet
    ]

    # loop through subsets
    for subset in subsets:
        # generate average match time length
        mean_match_length = subset.minutes.mean()
        # locate indexes where there are mtls
        ss_idx = subset[subset.minutes.isnull()].index
        # fill missing minutes
        df.loc[ss_idx, 'minutes'] = mean_match_length

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

    # love resets
    df = df.reset_index().drop(columns = 'index')

    # assign variable to index
    jd_p1_index = list(df[df.player_1 == 'Jared Donaldson'].index)
    # review index where Jared is player 2, assign to variable
    jd_p2_index = df[df.player_2 == 'Jared Donaldson'].index
    # fill all his heights with 188 cm
    df.loc[jd_p1_index, 'player_1_ht'] = 188
    # fill all his heights with 188
    df.loc[jd_p2_index, 'player_2_ht'] = 188

    # assign variable to index where AG is ready player1
    ag_p1_index = df[df.player_1 == 'Alejandro Gonzalez'].index
    # fill his heights 191
    df.loc[ag_p1_index, 'player_1_ht'] = 191
    # assign variable to indexes where AG is player2
    ag_p2_index = df[df.player_2 == 'Alejandro Gonzalez'].index
    # fill his heights 191
    df.loc[ag_p2_index, 'player_2_ht'] = 191

    # assign variables to indexes where Thomas is player 1 or player 2
    tf_p1_index = df[df.player_1 == 'Thomas Fabbiano'].index
    tf_p2_index = df[df.player_2 == 'Thomas Fabbiano'].index
    # fill his heights with 173 cm
    df.loc[tf_p1_index, 'player_1_ht'] = 173
    df.loc[tf_p2_index, 'player_2_ht'] = 173

    # if you kill it, fill it
    max_mar_idx = df[df.player_1 == 'Maximilian Marterer'].index
    max_mar_idx2 = df[df.player_2 == 'Maximilian Marterer'].index
    df.loc[max_mar_idx, 'player_1_ht'] = 188
    df.loc[max_mar_idx2, 'player_2_ht'] = 188

    # bjorn_frat_idx = df[df.player_1 == 'Bjorn Fratangelo'].index
    # bjorn_frat_idx2 = df[df.player_2 == 'Bjorn Fratangelo'].index
    # df.loc[bjorn_frat_idx, 'player_1_ht'] = 183
    # df.loc[bjorn_frat_idx2, 'player_2_ht'] = 183

    # fill rank points with 0, brand new players on the tour
    jg_rnull_idx = df[(df.player_1 == 'Justin Gimelstob') & (df.player_1_rank_points.isnull())].index
    df.loc[jg_rnull_idx, 'player_1_rank_points'] = 0
    jj_1rnull_idx = df[df.player_1 == 'Joachim Johansson'].index[0]
    df.loc[jj_1rnull_idx, 'player_1_rank_points'] = 0

    # fill rank points manually with inferred values
    jj_2rnull_idx = df[df.player_1 == 'Joachim Johansson'].index[-1]
    df.loc[jj_2rnull_idx, 'player_1_rank_points'] = 0
    jj_3rnull_idx = df[(df.player_2 == 'Joachim Johansson') & (df.player_2_rank_points.isnull())].index
    df.loc[jj_3rnull_idx, 'player_2_rank_points'] = 0
    kc_rnull_idx = df[(df.player_1 == 'Kenneth Carlsen') & (df.player_1_rank.isnull())].index
    df.loc[kc_rnull_idx, 'player_1_rank'] = 46
    df.loc[kc_rnull_idx, 'player_1_rank_points'] = 880

    # fill remaining rank point nulls with 0
    df.player_1_rank_points = df.player_1_rank_points.fillna(0)
    df.player_2_rank_points = df.player_2_rank_points.fillna(0)

    # infer ranks from last match plus pentalties 
    th_r2null_idx = df[(df.player_2 == 'Tommy Haas') & (df.player_2_rank.isnull())].index[:2]
    df.loc[th_r2null_idx, 'player_2_rank'] = 33
    th_r1null_idx = df[(df.player_1 == 'Tommy Haas') & (df.player_1_rank.isnull())].index
    df.loc[th_r1null_idx, 'player_1_rank'] = 33
    th_r3null_idx = df[(df.player_2 == 'Tommy Haas') & (df.player_2_rank.isnull())].index
    df.loc[th_r3null_idx, 'player_2_rank'] = 490

    # 'fix'
    mrp2_idx = df[df.player_2_rank.isnull()].index
    mrp1_idx = df[df.player_1_rank.isnull()].index
    df.loc[mrp2_idx, 'player_2_rank'] = 300
    df.loc[mrp1_idx, 'player_1_rank'] = 300

    # create columns (engineer categorical feature) to determine if players are seeded
    df['player_1_seeded'] = df.player_1_seed.apply(lambda x: x > 0)
    df['player_2_seeded'] = df.player_2_seed.apply(lambda x: x > 0)

    df_clean = df = df.dropna(subset=['player_1_aces'])

    # create dummy columns for surface, level, hand, and round 
    dummy_df = pd.get_dummies(df[['surface', 'tourney_level', 'player_1_hand', 'player_2_hand', 'round']], dummy_na = False, drop_first = False)
    # concat dummy columns to df
    df = pd.concat([df, dummy_df], axis = 1)

    # create a empty dataframe
    h2h_df = pd.DataFrame()

    # loop through each pair of players
    for players, winner in df.groupby(['player_1', 'player_2'])['winner']:
        num_matches = len(winner)
        p1 = 0
        p2 = 0
        temp_df = pd.DataFrame()
        for i in range(0, num_matches):
            if winner.iloc[i] == players[0]:
                p1 = p1 + 1
                temp_df = temp_df.append(pd.DataFrame([[players[0], players[1], p1, p2]], columns = ['player_1', 'player_2', 'h2h_1', 'h2h_2'], index = [winner.index[i]]))
            else:
                p2 = p2 + 1 
                temp_df = temp_df.append(pd.DataFrame([[players[0], players[1], p1, p2]], columns = ['player_1', 'player_2', 'h2h_1', 'h2h_2'], index = [winner.index[i]]))


        # shift the stats by 1 row so we're not cheating on h2h record a match early
        temp_df[['h2h_1', 'h2h_2']] = temp_df[['h2h_1', 'h2h_2']].shift(1).fillna(0)
        h2h_df = h2h_df.append(temp_df)

    # join h2h info with df
    df = df.join(h2h_df[['h2h_1', 'h2h_2']])

    # marginally reduce noise
    df.h2h_1 = df.h2h_1.astype(int)
    df.h2h_2 = df.h2h_2.astype(int)

    # reset index to tourney date
    df = df.set_index('tourney_date')
    df.index = pd.to_datetime(df.index, format = '%Y-%m-%d')

    return df


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

def clean_for_model(df):    
   
    df = df[['tourney_id', 'draw_size', 'winner', 'surface',
       'tourney_level', 'best_of', 'player_1', 'player_2', 'player_1_age',
       'player_2_age', 'player_1_hand',
       'player_2_hand', 'player_1_ht', 'player_2_ht', 'player_1_ioc', 'player_2_ioc', 'player_1_rank', 'player_2_rank',
       'player_1_rank_points', 'player_2_rank_points', 'player_1_wins', 'round_ER', 'round_F', 'round_QF', 'round_R128', 'round_R16', 'round_R32', 'round_R64', 'round_RR', 'round_SF', 'player_1_hand_R', 'player_1_hand_L', 
       'tourney_level_A', 'tourney_level_D', 'tourney_level_F', 'tourney_level_G', 'tourney_level_M', 'surface_Carpet', 'surface_Clay',
       'surface_Grass', 'surface_Hard']].copy(0)
    # drop null rows in specific columns
    df = df[df.player_1_hand.notnull()]
    df = df[df.player_2_hand.notnull()]
    df = df[df.player_1_ht.notnull()]
    df = df[df.player_2_ht.notnull()]
    df = df[df.player_1_rank.notnull()]
    df = df[df.player_2_rank.notnull()]
    df = df[df.player_1_rank_points.notnull()]
    df = df[df.player_2_rank_points.notnull()]
    
    # winner and loser rank columns
    df['winner_rank'] = np.where(df['winner'] == df['player_1'], df['player_1_rank'], df['player_2_rank'])
    df['loser_rank'] = np.where(df['winner'] == df['player_2'], df['player_1_rank'], df['player_2_rank'])
    
    # Calculate the difference in stats between player1 and playeer2. Save to new column. 
    df['ht_diff'] = df.player_1_ht - df.player_2_ht
    df['age_diff'] = df.player_1_age - df.player_2_age
    df['rank_diff'] = df.player_1_rank - df.player_2_rank
    df['rank_points_diff'] = df.player_1_rank_points - df.player_2_rank_points
    
    # upset column
    df['no_upset'] = df['winner_rank'] < df['loser_rank']
    
    # year column
    df['year'] = (df['tourney_id'].str[0:4]).astype(int)

    # rename columns to human readable names
    df.rename(columns={'player_1_rank': 'player1_rank', 'player_2_rank': 'player2_rank', 'player_1_rank_points': 'player1_rankpoints', 'player_2_rank_points': 'player2_rankpoints', 'surface_Carpet': 'Carpet', 'surface_Clay': 'Clay', 'surface_Grass': 'Grass', 'surface_Hard': 'Hard', 'player_1_hand_R': 'player1_righthand', 'player_2_hand_R': 'player2_righthand', 'player_1_hand_L': 'player1_lefthand', 'player_2_hand_L': 'player2_lefthand'}, inplace=True)
   
    return df

def train_validate_test_split(df):
    '''
    This function takes in a dataframe (df) and returns 3 dfs
    (train, validate, and test) split 20%, 24%, 56% respectively. 
    
    Also takes in a random seed for replicating results.  
    '''
    
    from sklearn.model_selection import train_test_split
     
    train_and_validate, test = train_test_split(
        df, test_size=0.2, random_state=123, stratify=df.player_1_wins
    )
    train, validate = train_test_split(
        train_and_validate,
        test_size=0.3,
        random_state=123,
        stratify=train_and_validate.player_1_wins,
    )
    return train, validate, test

# reference for splitting data (classification method)

# split_dat_strat defines two parameters, a clean dataframe (df) and my target variable (target), and returns my train, validate and test sets with the target variable stratified amongst them, whatever that means.
def split_data_strat(df, target):
    '''
    Takes in a dataset and returns the train, validate, and test subset dataframes.
    Dataframe size for my test set is .2 or 20% of the original data. 
    Validate data is 30% of my training set, which is 24% of the original data. 
    Training data is 70% of my original training set, which is 56% total of the original data.
    '''
    # import splitter
    from sklearn.model_selection import train_test_split
    
    # get my training and test data sets defined; stratify my target variable
    train, test = train_test_split(df, test_size = .2, random_state = 421, stratify = df[target])
    
    # get my validate set from the training set; stratify my target variable otra vez
    train, validate = train_test_split(train, test_size = .3, random_state = 421, stratify = train[target])
    
    # return the 3 dataframes
    return train, validate, test