import pandas as pd
import numpy as np
import seaborn as sns
import json
import os
import glob
import codecs
import csv
import matplotlib.pyplot as plt
import seaborn as sns
import re
from sklearn.model_selection import train_test_split
import prepare
pd.set_option("display.max_columns", None)


############### ACQUIRE & PREPARE###############
df = pd.read_csv('ATPMain.csv')
df = prepare.prepare_atp()

############### Further Prepare ###############
def clean_for_model(df):

#     df = df[['tourney_id', 'draw_size', 'winner', 'surface',
#        'tourney_level', 'best_of', 'player_1', 'player_2', 'player_1_age',
#        'player_2_age', 'player_1_hand',
#        'player_2_hand', 'player_1_ht', 'player_2_ht', 'player_1_ioc', 'player_2_ioc', 'player_1_name',
#        'player_2_name', 'player_1_rank', 'player_2_rank',
#        'player_1_rank_points', 'player_2_rank_points', 'player_1_wins', 'round_ER', 'round_F', 'round_QF', 'round_R128', 'round_R16', 'round_R32', 'round_R64', 'round_RR', 'round_SF', 'player_1_hand_R', 'player_1_hand_L', 
#        'tourney_level_A', 'tourney_level_D', 'tourney_level_F', 'tourney_level_G', 'tourney_level_M', 'surface_Carpet', 'surface_Clay',
#        'surface_Grass', 'surface_Hard']].copy(0)
#     # drop null rows in specific columns
#     df = df[df.player_1_ht.notnull()]
#     df = df[df.player_2_ht.notnull()]

    # winner and loser rank columns
    df['winner_rank'] = np.where(df['winner'] == df['player_1_name'], df['player_1_rank'], df['player_2_rank'])
    df['loser_rank'] = np.where(df['winner'] == df['player_2_name'], df['player_1_rank'], df['player_2_rank'])

    # Calculate the difference in stats between player1 and playeer2. Save to new column. 
    df['ht_diff'] = df.player_1_ht - df.player_2_ht
    df['age_diff'] = df.player_1_age - df.player_2_age
    df['rank_diff'] = df.player_1_rank - df.player_2_rank
    df['rank_points_diff'] = df.player_1_rank_points - df.player_2_rank_points

    # upset column
    df['no_upset'] = df['winner_rank'] < df['loser_rank']

    # year column
    df['year'] = (df['tourney_id'].str[0:4]).astype(int)

    return df

######### Run Cleaning #########
df = clean_for_model(df)



############# Federer vs Murray #############


Murray_Federer = df[df.player_1 == 'Andy Murray']
#Player 2 will be Roger
Murray_Federer = Murray_Federer[Murray_Federer.player_2 == 'Roger Federer']
#creating year column
Murray_Federer['year'] = (Murray_Federer['tourney_id'].str[0:4]).astype(int)


##### pie wins
def get_pie_wins_mur_fed():
    '''get pie chart for percent of wins'''

    Murray_Federer = df[df.player_1 == 'Andy Murray']
    #Player 2 will be Roger
    Murray_Federer = Murray_Federer[Murray_Federer.player_2 == 'Roger Federer']
    #creating year column
    Murray_Federer['year'] = (Murray_Federer['tourney_id'].str[0:4]).astype(int)

    # set values and labels for chart
    values = [len(Murray_Federer.player_1_wins[Murray_Federer.player_1_wins == True]), len(Murray_Federer.player_1_wins[Murray_Federer.player_1_wins == False])] 
    labels = ['Murray Wins','Federer Wins', ] 

    # generate and show chart
    plt.pie(values, labels=labels, autopct='%.0f%%', colors=['#dfff4f', '#3C638E'])
    plt.title('Games Ending in Federer winning Represents 1/2 of the time in the last 20 years')
    plt.show()


#### bar graphs by year
def rod_mur_bar():
    years = [i for i in range(2004, 2019)]
    fedwins = [0 for i in range(2004, 2019)]
    murwins = [0 for i in range(2004, 2019)]

    for index, row in Murray_Federer.iterrows():
        if row['winner'] == "Andy Murray":
            murwins[row['year'] - 2004] += 1
        elif row['winner'] == "Roger Federer":
            fedwins[row['year'] - 2004] += 1
    plt.figure(figsize=(12,8))

    #barwith and position
    barWidth = 0.4
    r1 = np.arange(len(fedwins))
    r2 = [x + barWidth for x in r1]

    # Make the plot
    plt.bar(r1, fedwins, color='#3C638E', width=barWidth, edgecolor='white', label='Federer wins')
    plt.bar(r2, murwins, color='#dfff4f', width=barWidth, edgecolor='white', label='Murray wins')

    # Add xticks on the middle of the group bars
    plt.title('Plotting Roger Federer vs Andy Murray over the years', fontweight='bold')
    plt.xticks([r + barWidth - 0.2 for r in range(len(fedwins))], [i for i in range(2004, 2019)])
    plt.xlabel("Year")
    plt.ylabel("# of Wins")

    # Create legend & Show graphic
    plt.legend()

###### Building out for the next (Chloe's code)
fed_v_mur1 = df[df.player_1.isin(['Andy Murray']) & df.player_2.isin(['Roger Federer'])] 
Roger_Federer1 = df[df.player_1.isin(['Roger Federer'])] 
Roger_Federer2 = df[df.player_2.isin(['Roger Federer'])] 
Andy_rodray1 = df[df.player_1.isin(['Andy Murray'])]
Andy_rodray2 = df[df.player_2.isin(['Andy Murray'])] 


##### pie upsets
def get_pies_upsets_fed_mur():
    "create pie charts showing upset percentage for having and not having the first move"

    fed_v_mur1 = df[df.player_1.isin(['Andy Murray']) & df.player_2.isin(['Roger Federer'])] 
    Roger_Federer1 = df[df.player_1.isin(['Roger Federer'])] 
    Roger_Federer2 = df[df.player_2.isin(['Roger Federer'])] 
    Andy_rodray1 = df[df.player_1.isin(['Andy Murray'])]
    Andy_rodray2 = df[df.player_2.isin(['Andy Murray'])] 
    # create axis object
    fig, (ax1,ax2) = plt.subplots(1,2)
    
    # create pie chart and assign to axis object
    values = [len(fed_v_mur1.no_upset[(fed_v_mur1.player_1_wins == True) & (fed_v_mur1.no_upset == True)]),
            len(fed_v_mur1.no_upset[(fed_v_mur1.player_1_wins == True) & (fed_v_mur1.no_upset == False)])]
    labels = ['Murray Wins', 'Federer Wins']

    ax1.pie(values, labels=labels, autopct='%.0f%%', colors=['#dfff4f', '#3C638E'])
    ax1.title.set_text('High Ranked Player Wins')

    # create pie chart and and assign to axis object
    values = [len(fed_v_mur1.no_upset[(fed_v_mur1.player_1_wins == False) & (fed_v_mur1.no_upset == True)]),
            len(fed_v_mur1.no_upset[(fed_v_mur1.player_1_wins == False) & (fed_v_mur1.no_upset == False)])]
    labels = ['Murray Wins', 'Federer Wins'] 

    ax2.pie(values, labels=labels, autopct='%.0f%%', colors=['#dfff4f', '#3C638E'])
    ax2.title.set_text('Lower Ranked Player Wins')

    # display charts
    plt.tight_layout()
    plt.show()

######### pie tourney 
def get_pie_tourney_level_fed_mur():
    '''get pie chart of player win percentage for each tourney level'''

    fed_v_mur1 = df[df.player_1.isin(['Andy Murray']) & df.player_2.isin(['Roger Federer'])] 
    Roger_Federer1 = df[df.player_1.isin(['Roger Federer'])] 
    Roger_Federer2 = df[df.player_2.isin(['Roger Federer'])] 
    Andy_rodray1 = df[df.player_1.isin(['Andy Murray'])]
    Andy_rodray2 = df[df.player_2.isin(['Andy Murray'])] 
    # activate subplots objects
    fig, axs = plt.subplots(2, 2, figsize=(10,8))

    # list of charts to be generated
    levels = ['A', 'F', 'G', 'M']

    # generate graphs and assign them to subplots
    for level, ax in zip(levels, axs.ravel()):
        
        values = [len(fed_v_mur1.player_1_wins[(fed_v_mur1.player_1_wins == True) & (fed_v_mur1.tourney_level == level)]), len(fed_v_mur1.player_1_wins[(fed_v_mur1.player_1_wins == False) & (fed_v_mur1.tourney_level == level)])] 
        labels = ['Murray Wins','Federer Wins']
        
        ax.pie(values, labels=labels, autopct='%.0f%%', colors=['#dfff4f', '#3C638E'])
        ax.set_title(f'Win Percentage for tourney {level}')
    
    # display chart
    plt.tight_layout()
    plt.show()


################################
# RODDICK VS FEDERER
################################

#Player 1 is always alphabetically first - Andy
Rodrick_Federer = df[df.player_1 == 'Andy Roddick']
#Player 2 will be Roger
Rodrick_Federer = Rodrick_Federer[Rodrick_Federer.player_2 == 'Roger Federer']
Rodrick_Federer['year'] = (Rodrick_Federer['tourney_id'].str[0:4]).astype(int)

####################################

#### bar graphs by year

def rod_fed_bar():
    
    #Player 1 is always alphabetically first - Andy
    Rodrick_Federer = df[df.player_1 == 'Andy Roddick']
    #Player 2 will be Roger
    Rodrick_Federer = Rodrick_Federer[Rodrick_Federer.player_2 == 'Roger Federer']
    Rodrick_Federer['year'] = (Rodrick_Federer['tourney_id'].str[0:4]).astype(int)

    years = [i for i in range(1999, 2014)]
    fedwins = [0 for i in range(1999, 2014)]
    rodwins = [0 for i in range(1999, 2014)]

    for index, row in Rodrick_Federer.iterrows():
        if row['winner'] == "Andy Roddick":
            rodwins[row['year'] - 1999] += 1
        elif row['winner'] == "Roger Federer":
            fedwins[row['year'] - 1999] += 1
    plt.figure(figsize=(12,8))

    #barwith and position
    barWidth = 0.4
    r1 = np.arange(len(fedwins))
    r2 = [x + barWidth for x in r1]

    # Make the plotdfff4f
    plt.bar(r1, fedwins, color='#3C638E', width=barWidth, edgecolor='white', label='Federer wins')
    plt.bar(r2, rodwins, color='#dfff4f', width=barWidth, edgecolor='white', label='Roddick wins')

    # Add xticks on the middle of the group bars
    plt.title('Plotting Roger Federer vs Andy Roddick over the years', fontweight='bold')
    plt.xticks([r + barWidth - 0.2 for r in range(len(fedwins))], [i for i in range(1999, 2014)])
    plt.xlabel("Year")
    plt.ylabel("# of Wins")

    # Create legend & Show graphic
    plt.legend()

####################################

    #### pie wins
def get_pie_wins_rod_fed():
    '''get pie chart for percent of wins'''
    #Player 1 is always alphabetically first - Andy
    Rodrick_Federer = df[df.player_1 == 'Andy Roddick']
    #Player 2 will be Roger
    Rodrick_Federer = Rodrick_Federer[Rodrick_Federer.player_2 == 'Roger Federer']
    Rodrick_Federer['year'] = (Rodrick_Federer['tourney_id'].str[0:4]).astype(int)

    # set values and labels for chart
    values = [len(Rodrick_Federer.player_1_wins[Rodrick_Federer.player_1_wins == True]), len(Rodrick_Federer.player_1_wins[Rodrick_Federer.player_1_wins == False])] 
    labels = ['Rodrick Wins','Federer Wins', ] 

    # generate and show chart
    plt.pie(values, labels=labels, autopct='%.0f%%', colors=['#dfff4f', '#3C638E'])
    plt.title('Games Ending in Federer winning Represents 1/2 of the time in the last 20 years')
    plt.show()

    ####################################
fed_v_rod1 = df[df.player_1.isin(['Andy Roddick']) & df.player_2.isin(['Roger Federer'])] 
Roger_Federer1 = df[df.player_1.isin(['Roger Federer'])] 
Roger_Federer2 = df[df.player_2.isin(['Roger Federer'])] 
Andy_rodray1 = df[df.player_1.isin(['Andy Roddick'])]
Andy_rodray2 = df[df.player_2.isin(['Andy Roddick'])] 


def get_pies_upsets_fed_rod():
    "create pie charts showing upset percentage for having and not having the first move"

    fed_v_rod1 = df[df.player_1.isin(['Andy Roddick']) & df.player_2.isin(['Roger Federer'])] 
    Roger_Federer1 = df[df.player_1.isin(['Roger Federer'])] 
    Roger_Federer2 = df[df.player_2.isin(['Roger Federer'])] 
    Andy_rodray1 = df[df.player_1.isin(['Andy Roddick'])]
    Andy_rodray2 = df[df.player_2.isin(['Andy Roddick'])] 

    # create axis object
    fig, (ax1,ax2) = plt.subplots(1,2)
    
    # create pie chart and assign to axis object
    values = [len(fed_v_rod1.no_upset[(fed_v_rod1.player_1_wins == True) & (fed_v_rod1.no_upset == True)]),
            len(fed_v_rod1.no_upset[(fed_v_rod1.player_1_wins == True) & (fed_v_rod1.no_upset == False)])]
    labels = ['Roddick Wins', 'Federer Wins']

    ax1.pie(values, labels=labels, autopct='%.0f%%', colors=['#dfff4f', '#3C638E'])
    ax1.title.set_text('High Ranked Player Wins')

    # create pie chart and and assign to axis object
    values = [len(fed_v_rod1.no_upset[(fed_v_rod1.player_1_wins == False) & (fed_v_rod1.no_upset == True)]),
            len(fed_v_rod1.no_upset[(fed_v_rod1.player_1_wins == False) & (fed_v_rod1.no_upset == False)])]
    labels = ['Roddick Wins', 'Federer Wins'] 

    ax2.pie(values, labels=labels, autopct='%.0f%%', colors=['#dfff4f', '#3C638E'])
    ax2.title.set_text('Lower Ranked Player Wins')

    # display charts
    plt.tight_layout()
    plt.show()


def get_pie_tourney_level_fed_rod():
    '''get pie chart of player win percentage for each tourney level'''

    fed_v_rod1 = df[df.player_1.isin(['Andy Roddick']) & df.player_2.isin(['Roger Federer'])] 
    Roger_Federer1 = df[df.player_1.isin(['Roger Federer'])] 
    Roger_Federer2 = df[df.player_2.isin(['Roger Federer'])] 
    Andy_rodray1 = df[df.player_1.isin(['Andy Roddick'])]
    Andy_rodray2 = df[df.player_2.isin(['Andy Roddick'])] 

    # activate subplots objects
    fig, axs = plt.subplots(2, 2, figsize=(10,8))

    # list of charts to be generated
    levels = ['A', 'F', 'G', 'M']

    # generate graphs and assign them to subplots
    for level, ax in zip(levels, axs.ravel()):
        
        values = [len(fed_v_rod1.player_1_wins[(fed_v_rod1.player_1_wins == True) & (fed_v_rod1.tourney_level == level)]), len(fed_v_rod1.player_1_wins[(fed_v_rod1.player_1_wins == False) & (fed_v_rod1.tourney_level == level)])] 
        labels = ['Roddick Wins','Federer Wins']
        
        ax.pie(values, labels=labels, autopct='%.0f%%', colors=['#dfff4f', '#3C638E'])
        ax.set_title(f'Win Percentage for tourney {level}')
    
    # display chart
    plt.tight_layout()
    plt.show()

####################################
# NADAL VS FEDERER
####################################

#Player 1 is always alphabetically first - Rafae
Nadal_Federer = df[df.player_1 == 'Rafael Nadal']
#Player 2 will be Roger
Nadal_Federer = Nadal_Federer[Nadal_Federer.player_2 == 'Roger Federer']
Nadal_Federer['year'] = (Nadal_Federer['tourney_id'].str[0:4]).astype(int)

####################################

#### bar graphs by year

def rod_nad_bar():
    years = [i for i in range(2003, 2020)]
    fedwins = [0 for i in range(2003, 2020)]
    nadwins = [0 for i in range(2003, 2020)]

    for index, row in Nadal_Federer.iterrows():
        if row['winner'] == "Rafael Nadal":
            nadwins[row['year'] - 2003] += 1
        elif row['winner'] == "Roger Federer":
            fedwins[row['year'] - 2003] += 1
    plt.figure(figsize=(12,8))

    #barwith and position
    barWidth = 0.4
    r1 = np.arange(len(fedwins))
    r2 = [x + barWidth for x in r1]

    # Make the plot
    plt.bar(r1, fedwins, color='#3C638E', width=barWidth, edgecolor='white', label='Federer wins')
    plt.bar(r2, nadwins, color='#dfff4f', width=barWidth, edgecolor='white', label='Nadal wins')

    # Add xticks on the middle of the group bars
    plt.title('Plotting Roger Federer vs Rafael Nadal over the years', fontweight='bold')
    plt.xticks([r + barWidth - 0.2 for r in range(len(fedwins))], [i for i in range(2003, 2020)])
    plt.xlabel("Year")
    plt.ylabel("# of Wins")

    # Create legend & Show graphic
    plt.legend()

#### PIE CHARTS ### 

def get_pie_wins_nad_fed():
    '''get pie chart for percent of wins'''

    # set values and labels for chart
    values = [len(Nadal_Federer.player_1_wins[Nadal_Federer.player_1_wins == True]), len(Nadal_Federer.player_1_wins[Nadal_Federer.player_1_wins == False])] 
    labels = ['Nadal Wins','Federer Wins', ] 

    # generate and show chart
    plt.pie(values, labels=labels, autopct='%.0f%%', colors=['#dfff4f', '#3C638E'])
    plt.title('Games Ending in Federer winning Represents 1/2 of the time in the last 20 years')
    plt.show()

###### Building out for the next (Chloe's code)
fed_v_nad1 = df[df.player_1.isin(['Rafael Nadal']) & df.player_2.isin(['Roger Federer'])] 
Roger_Federer1 = df[df.player_1.isin(['Roger Federer'])] 
Roger_Federer2 = df[df.player_2.isin(['Roger Federer'])] 
Andy_rodray1 = df[df.player_1.isin(['Rafael Nadal'])]
Andy_rodray2 = df[df.player_2.isin(['Rafael Nadal'])]

#### PIE UPSETS ###

def get_pies_upsets_fed_nad():
    "create pie charts showing upset percentage for having and not having the first move"

    # create axis object
    fig, (ax1,ax2) = plt.subplots(1,2)
    
    # create pie chart and assign to axis object
    values = [len(fed_v_nad1.no_upset[(fed_v_nad1.player_1_wins == True) & (fed_v_nad1.no_upset == True)]),
            len(fed_v_nad1.no_upset[(fed_v_nad1.player_1_wins == True) & (fed_v_nad1.no_upset == False)])]
    labels = ['Nadal Wins', 'Federer Wins']

    ax1.pie(values, labels=labels, autopct='%.0f%%', colors=['#dfff4f', '#3C638E'])
    ax1.title.set_text('High Ranked Player Wins')

    # create pie chart and and assign to axis object
    values = [len(fed_v_nad1.no_upset[(fed_v_nad1.player_1_wins == False) & (fed_v_nad1.no_upset == True)]),
            len(fed_v_nad1.no_upset[(fed_v_nad1.player_1_wins == False) & (fed_v_nad1.no_upset == False)])]
    labels = ['Nadal Wins', 'Federer Wins'] 

    ax2.pie(values, labels=labels, autopct='%.0f%%', colors=['#dfff4f', '#3C638E'])
    ax2.title.set_text('Lower Ranked Player Wins')

    # display charts
    plt.tight_layout()
    plt.show()

##### PIE TOURNEY LEVEL #####
def get_pie_tourney_level_fed_nad():
    '''get pie chart of player win percentage for each tourney level'''

    # activate subplots objects
    fig, axs = plt.subplots(2, 2, figsize=(10,8))

    # list of charts to be generated
    levels = ['A', 'F', 'G', 'M']

    # generate graphs and assign them to subplots
    for level, ax in zip(levels, axs.ravel()):
        
        values = [len(fed_v_nad1.player_1_wins[(fed_v_nad1.player_1_wins == True) & (fed_v_nad1.tourney_level == level)]), len(fed_v_nad1.player_1_wins[(fed_v_nad1.player_1_wins == False) & (fed_v_nad1.tourney_level == level)])] 
        labels = ['Nadal Wins','Federer Wins']
        
        ax.pie(values, labels=labels, autopct='%.0f%%', colors=['#dfff4f', '#3C638E'])
        ax.set_title(f'Win Percentage for tourney {level}')
    
    # display chart
    plt.tight_layout()
    plt.show()


####################################
# NADAL VS Djokovic
####################################
#Player 1 is always alphabetically first - Novak
Djokovic_Federer = df[df.player_1 == 'Novak Djokovic']
#Player 2 will be Roger
Djokovic_Federer = Djokovic_Federer[Djokovic_Federer.player_2 == 'Roger Federer']
Djokovic_Federer['year'] = (Djokovic_Federer['tourney_id'].str[0:4]).astype(int)


##### Bar Graph By Year
def fed_djo_bar():
    years = [i for i in range(2004, 2020)]
    fedwins = [0 for i in range(2004, 2020)]
    djowins = [0 for i in range(2004, 2020)]

    for index, row in Djokovic_Federer.iterrows():
        if row['winner'] == "Novak Djokovic":
            djowins[row['year'] - 2004] += 1
        elif row['winner'] == "Roger Federer":
            fedwins[row['year'] - 2004] += 1
    plt.figure(figsize=(12,8))

    #barwith and position
    barWidth = 0.4
    r1 = np.arange(len(fedwins))
    r2 = [x + barWidth for x in r1]

    # Make the plot
    plt.bar(r1, fedwins, color='#3C638E', width=barWidth, edgecolor='white', label='Federer wins')
    plt.bar(r2, djowins, color='#dfff4f', width=barWidth, edgecolor='white', label='Djokovic wins')

    # Add xticks on the middle of the group bars
    plt.title('Plotting Roger Federer vs Novak Djokovic over the years', fontweight='bold')
    plt.xticks([r + barWidth - 0.2 for r in range(len(fedwins))], [i for i in range(2004, 2020)])
    plt.xlabel("Year")
    plt.ylabel("# of Wins")

    # Create legend & Show graphic
    plt.legend()

##### Pie Graph Distribution
def get_pie_wins_djo_fed():
    '''get pie chart for percent of wins'''

    # set values and labels for chart
    values = [len(Djokovic_Federer.player_1_wins[Djokovic_Federer.player_1_wins == True]), len(Djokovic_Federer.player_1_wins[Djokovic_Federer.player_1_wins == False])] 
    labels = ['Djokovic Wins','Federer Wins', ] 

    # generate and show chart
    plt.pie(values, labels=labels, autopct='%.0f%%', colors=['#dfff4f', '#3C638E'])
    plt.title('Games Ending in Federer winning Represents 1/2 of the time in the last 20 years')
    plt.show()



###### Building out for the next (Chloe's code)
fed_v_djo1 = df[df.player_1.isin(['Novak Djokovic']) & df.player_2.isin(['Roger Federer'])] 
Roger_Federer1 = df[df.player_1.isin(['Roger Federer'])] 
Roger_Federer2 = df[df.player_2.isin(['Roger Federer'])] 
Andy_djoray1 = df[df.player_1.isin(['Novak Djokovic'])]
Andy_djoray2 = df[df.player_2.isin(['Novak Djokovic'])] 

#### PIE UPSETS ###
def get_pies_upsets_djo_fed():
    "create pie charts showing upset percentage for having and not having the first move"
    fed_v_djo1 = df[df.player_1.isin(['Novak Djokovic']) & df.player_2.isin(['Roger Federer'])] 
    Roger_Federer1 = df[df.player_1.isin(['Roger Federer'])] 
    Roger_Federer2 = df[df.player_2.isin(['Roger Federer'])] 
    Andy_djoray1 = df[df.player_1.isin(['Novak Djokovic'])]
    Andy_djoray2 = df[df.player_2.isin(['Novak Djokovic'])] 

    # create axis object
    fig, (ax1,ax2) = plt.subplots(1,2)
    
    # create pie chart and assign to axis object
    values = [len(fed_v_djo1.no_upset[(fed_v_djo1.player_1_wins == True) & (fed_v_djo1.no_upset == True)]),
            len(fed_v_djo1.no_upset[(fed_v_djo1.player_1_wins == True) & (fed_v_djo1.no_upset == False)])]
    labels = ['Djokovic Wins', 'Federer Wins']

    ax1.pie(values, labels=labels, autopct='%.0f%%', colors=['#dfff4f', '#3C638E'])
    ax1.title.set_text('High Ranked Player Wins')

    # create pie chart and and assign to axis object
    values = [len(fed_v_djo1.no_upset[(fed_v_djo1.player_1_wins == False) & (fed_v_djo1.no_upset == True)]),
            len(fed_v_djo1.no_upset[(fed_v_djo1.player_1_wins == False) & (fed_v_djo1.no_upset == False)])]
    labels = ['Djokovic Wins', 'Federer Wins'] 

    ax2.pie(values, labels=labels, autopct='%.0f%%', colors=['#dfff4f', '#3C638E'])
    ax2.title.set_text('Lower Ranked Player Wins')

    # display charts
    plt.tight_layout()
    plt.show()


##### PIE TOURNEY LEVEL #####
def get_pie_tourney_level_fed_djo():
    '''get pie chart of player win percentage for each tourney level'''

    fed_v_djo1 = df[df.player_1.isin(['Novak Djokovic']) & df.player_2.isin(['Roger Federer'])] 
    Roger_Federer1 = df[df.player_1.isin(['Roger Federer'])] 
    Roger_Federer2 = df[df.player_2.isin(['Roger Federer'])] 
    Andy_djoray1 = df[df.player_1.isin(['Novak Djokovic'])]
    Andy_djoray2 = df[df.player_2.isin(['Novak Djokovic'])] 

    # activate subplots objects
    fig, axs = plt.subplots(2, 2, figsize=(10,8))

    # list of charts to be generated
    levels = ['A', 'F', 'G', 'M']

    # generate graphs and assign them to subplots
    for level, ax in zip(levels, axs.ravel()):
        
        values = [len(fed_v_djo1.player_1_wins[(fed_v_djo1.player_1_wins == True) & (fed_v_djo1.tourney_level == level)]), len(fed_v_djo1.player_1_wins[(fed_v_djo1.player_1_wins == False) & (fed_v_djo1.tourney_level == level)])] 
        labels = ['Djokovic Wins','Federer Wins']
        
        ax.pie(values, labels=labels, autopct='%.0f%%', colors=['#dfff4f', '#3C638E'])
        ax.set_title(f'Win Percentage for tourney {level}')
    
    # display chart
    plt.tight_layout()
    plt.show()