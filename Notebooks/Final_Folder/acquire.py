import numpy as np
import seaborn as sns
import json
import os
import codecs
import csv
import glob
import pandas as pd


################# Loop to pull all the ATP matches #################
fds = []
for f in glob.glob("../atp_matches/atp_matches*.csv"):
    fds.append(pd.read_csv(f))

df = pd.concat(fds)
df.to_csv('ATPTotal')

################# Function inspired by nickdevin/Tennis_Predicting code #################
WL_extensions = ['age', 'entry', 'hand', 'ht', 'id', 'ioc', 'name', 'rank', 'rank_points', 'seed',
                'aces' ,'double_faults', 'service_points', 'first_serves_in', 
                'first_serve_points_won', 'second_serve_points_won','service_game_total', 'break_points_saved',
                'break_points_faced']

def obscure_features(DF):
    '''
    We replace 'winner' and 'loser' with 'player_1' and 'player_2' (not necessarily in that order)
    'player_1' replaces the name of the player that comes first alphabetically
    The purpose of this is to predict the winner of a match without the data being tied to
    the known winner or loser.
    '''
    DF['player_1'] = pd.concat([DF['winner_name'], DF['loser_name']], axis = 1).min(axis = 1)
    DF['player_2'] = pd.concat([DF['winner_name'], DF['loser_name']], axis = 1).max(axis = 1)
    
    for ext in WL_extensions:
        p1_feature = np.where(DF['player_1'] == DF['winner_name'],
                    DF['winner_' + ext],
                    DF['loser_' + ext])
    
        p2_feature = np.where(DF['player_2'] == DF['winner_name'],
                    DF['winner_' + ext],
                    DF['loser_' + ext])
    
        DF['player_1_' + ext] = p1_feature
        DF['player_2_' + ext] = p2_feature
        
    winner_cols = list(filter(lambda x: x.startswith('winner'), DF.columns))
    loser_cols = list(filter(lambda x: x.startswith('loser'), DF.columns))
    cols_to_drop = winner_cols + loser_cols
    
    target = DF['winner_name']
    
    DF.drop(cols_to_drop, axis = 1, inplace = True)
    
    DF['winner'] = target
    
    return DF
################# Rename columns for function to work #######
columns_to_rename = {
                    'winner_id' : 'winner_id',
                    'winner_seed': 'winner_seed',
                    'winner_entry': 'winner_entry',
                    'winner_name': 'winner_name',
                    'winner_hand': 'winner_hand',
                    'winner_ht': 'winner_ht',
                    'winner_ioc': 'winner_ioc',
                    'winner_age': 'winner_age',
                    'loser_id': 'loser_id',
                    'loser_seed': 'loser_seed',
                    'loser_entry': 'loser_entry',
                    'loser_name': 'loser_name',
                    'loser_hand': 'loser_hand',
                    'loser_ht': 'loser_ht',
                    'loser_ioc': 'loser_ioc',
                    'loser_age': 'loser_age',
                    'w_aces': "winner_aces",
                    'w_double_faults': 'winner_double_faults',
                    'w_service_points': 'winner_service_points',
                    'w_first_serves_in': 'winner_first_serves_in',
                    'w_first_serve_points_won': 'winner_first_serve_points_won',
                    'w_second_serve_points_won': 'winner_second_serve_points_won',
                    'w_second_serve_points_won': 'winner_second_serve_points_won',
                    'w_service_game_total': 'winner_service_game_total',
                    'w_break_points_saved': 'winner_break_points_saved',
                    'w_break_points_faced': 'winner_break_points_faced',
                    'l_aces': "loser_aces",
                    'l_double_faults': 'loser_double_faults',
                    'l_service_points': 'loser_service_points',
                    'l_first_serves_in': 'loser_first_serves_in',
                    'l_first_serve_points_won': 'loser_first_serve_points_won',
                    'l_second_serve_points_won': 'loser_second_serve_points_won',
                    'l_second_serve_points_won': 'loser_second_serve_points_won',
                    'l_service_game_total': 'loser_service_game_total',
                    'l_break_points_saved': 'loser_break_points_saved',
                    'l_break_points_faced': 'loser_break_points_faced',
                    'winner_rank': 'winner_rank',
                    'winner_rank_points': 'winner_rank_points',
                    'loser_rank': 'loser_rank',
                    'loser_rank_points': 'loser_rank_points'}

df = df.rename(columns = columns_to_rename)
#df = df.rename(columns = columns_to_rename)

df.head(1)

###### Function applied to df #####

df = obscure_features(df)

####### Feature engineering ######
df['player_1_first_serve_%'] = df['player_1_first_serves_in'] / df['player_1_service_points']
df['player_2_first_serve_%'] = df['player_2_first_serves_in'] / df['player_2_service_points']


df['player_1_first_serve_win_%'] = df['player_1_first_serve_points_won'] / df['player_1_first_serves_in']
df['player_2_first_serve_win_%'] = df['player_2_first_serve_points_won'] / df['player_2_first_serves_in']

df['player_1_break_points_won'] = df['player_2_break_points_faced']- df['player_2_break_points_saved']
df['player_2_break_points_won'] = df['player_1_break_points_faced']- df['player_1_break_points_saved']


########### SAVE DF TO NEW ATP FILE #########

df.to_csv('ATPMain.csv')
