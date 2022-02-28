#!/usr/bin/env python
# coding: utf-8

# # Helper Files for the Explore Section

# ### imports

# In[1]:


# imports

import pandas as pd
import numpy as np
import regex as re

# Custom Helper Files
from prepare import *

# Stats
from scipy import stats

# Visualize
import matplotlib.pyplot as plt
import seaborn as sns

# Split 
from sklearn.model_selection import train_test_split

# Ignore Warnings
import warnings
warnings.filterwarnings("ignore")

# Remove Limits On Viewing Dataframes
pd.set_option('display.max_columns', None)


# In[2]:


df = prepare_atp()


# In[26]:


# df.head(1)


# In[29]:


# Remove Limits On Viewing Dataframes
# pd.set_option('display.max_rows', None)


# In[27]:


df = clean_for_model(df)


# In[28]:


# df.head(1)


# In[7]:


train, validate, test = train_validate_test_split(df)


# In[10]:


# player_1_rank_points, player_1_hand_R, player_1_hand_L, surface_Clay.


# In[8]:


def get_ttest_rank_points(train):
    '''This function: 
    returns rusults of chi-square for player_1_wins and player_1_rank_points'''

    t, p = stats.ttest_1samp(train.player_1_wins, train.player_1_rank_points.mean())

    print(f't = {t:.3f}')
    print(f'p = {p:.3f}')


# In[30]:


# get_ttest_rank_points(train)


# In[11]:


def get_winning_player_rank_points(train):
    '''This function: 
     gets graph of average player ranking points for train'''

    # create axis object
    fig, (ax1,ax2) = plt.subplots(1,2)
    
    # assign values and labels for ax1
    values = [train.player_1_rank_points[(train.player_1_wins == True)].mean(), train.player_1_rank_points[(train.player_1_wins == False)].mean()]
    labels = ['Wins','Losses']

    # generate and display graph
    ax1.bar(height=values, x=labels, color=['#dfff4f', '#3C638E'])
    ax1.title.set_text("Player 1's Mean Rank Points")
   
    # assign values and labels for ax2
    values = [train.player_2_rank_points[(train.player_1_wins == False)].mean(), train.player_2_rank_points[(train.player_1_wins == True)].mean()]
    labels = ['Wins','Losses']

    # generate and display graph
    ax2.bar(height=values, x=labels, color=['#dfff4f', '#3C638E'])
    ax2.title.set_text("Player 2's Mean Rank Points")
   
    # display plot
    plt.tight_layout()
    plt.show()


# In[31]:


# get_winning_player_rank_points(train)


# In[17]:


def get_chi_right_hand(train):
    '''This function: 
    returns rusults of chi-square for player_1_wins and player_1_rank_points'''

    observed = pd.crosstab(train.player_1_hand_R, train.player_1_wins)
    chi2, p, degf, expected = stats.chi2_contingency(observed)
    p

    print(f'chi^2 = {chi2:.4f}')
    print(f'p = {p:.4f}')


# In[32]:


# get_chi_right_hand(train)


# In[19]:


def get_chi_left_hand(train):
    '''This function: 
    returns rusults of chi-square for player_1_wins and player_1_rank_points'''

    observed = pd.crosstab(train.player_1_hand_L, train.player_1_wins)
    chi2, p, degf, expected = stats.chi2_contingency(observed)
    p

    print(f'chi^2 = {chi2:.4f}')
    print(f'p = {p:.4f}')


# In[33]:


# get_chi_left_hand(train)


# In[22]:


def get_pie_surface(train):
    '''get pie chart of player win percentage for clay surface type'''

    # activate subplots objects
    fig, axs = plt.subplots(2, 2, figsize=(10,8))

    # list of charts to be generated
    surfaces = ['Clay', 'Hard', 'Grass', 'Carpet']

    # generate graphs and assign them to subplots
    for surface, ax in zip(surfaces, axs.ravel()):
        
        values = [len(train.player_1_wins[(train.player_1_wins == True) & (train.surface == surface)]), len(train.player_1_wins[(train.player_1_wins == False) & (train.surface == surface)])] 
        labels = ['Player1 Wins','Player 2 Wins']
        
        ax.pie(values, labels=labels, autopct='%.0f%%', colors=['#dfff4f', '#3C638E'])
        ax.set_title(f'Win Percentage for surface {surface}')
    
    # display chart
    plt.tight_layout()
    plt.show()


# In[34]:


# get_pie_surface(train)


# In[24]:


def get_chi_clay(train):
    '''This function: 
    returns rusults of chi-square for player_1_wins and player_1_rank_points'''

    observed = pd.crosstab(train.surface_Clay, train.player_1_wins)
    chi2, p, degf, expected = stats.chi2_contingency(observed)
    p

    print(f'chi^2 = {chi2:.4f}')
    print(f'p = {p:.4f}')


# In[35]:


# get_chi_clay(train)


# In[ ]:




