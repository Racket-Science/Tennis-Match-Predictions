#!/usr/bin/env python
# coding: utf-8

# # This is the helper file for the modeling section of the final report. 

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

# Modeling
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import LogisticRegression

# Ignore Warnings
import warnings
warnings.filterwarnings("ignore")

# Remove Limits On Viewing Dataframes
pd.set_option('display.max_columns', None)


# In[2]:


df = prepare_atp()


# In[3]:


df = clean_for_model(df)


# In[4]:


train, validate, test = train_validate_test_split(df)


# In[5]:


def model_prep(train,validate,test):
    '''This function: 
    prepares the data for modeling'''

    # drop unused columns 
    drop_cols = ['tourney_id', 'draw_size', 'tourney_level', 'best_of', 'player_1', 'player_2',
       'player_1_age', 'player_2_age', 'player_1_hand', 'player_2_hand', 'surface',
       'player_1_ht', 'player_2_ht', 'player_1_ioc', 'player_2_ioc',
        'player1_rank', 'player2_rank',
       'player2_rankpoints',
       'round_ER', 'round_F', 'round_QF', 'round_R128', 'round_R16',
       'round_R32', 'round_R64', 'round_RR', 'round_SF', 'tourney_level_A', 'tourney_level_D',
       'tourney_level_F', 'tourney_level_G', 'tourney_level_M',
       'Carpet', 'Grass', 'Hard',
       'ht_diff', 'age_diff', 'rank_points_diff', 'winner_rank', 'loser_rank', 'winner', 'no_upset', 'year']

    train = train.drop(columns=drop_cols)
    validate = validate.drop(columns=drop_cols)
    test = test.drop(columns=drop_cols)
    
    # Split data into predicting variables (X) and target variable (y) and reset the index for each dataframe
    X_train = train.drop(columns='player_1_wins').reset_index(drop=True)
    y_train = train[['player_1_wins']].reset_index(drop=True)

    X_validate = validate.drop(columns='player_1_wins').reset_index(drop=True)
    y_validate = validate[['player_1_wins']].reset_index(drop=True)

    X_test = test.drop(columns='player_1_wins').reset_index(drop=True)
    y_test = test[['player_1_wins']].reset_index(drop=True)
    
    return X_train, X_validate, X_test, y_train, y_validate, y_test


# In[14]:


# X_train, X_validate, X_test, y_train, y_validate, y_test = model_prep(train,validate,test)


# In[15]:


# X_train.isnull().sum()


# In[8]:


def get_decision_tree(X_train, X_validate, y_train, y_validate):
    '''This function: 
    returns decision tree accuracy on train and validate data'''

    # create classifier object
    clf = DecisionTreeClassifier(max_depth=3, random_state=123)

    #fit model on training data
    clf = clf.fit(X_train, y_train)

    # print result
    print(f"Accuracy of Decision Tree on train data is {clf.score(X_train, y_train)}")
    print(f"Accuracy of Decision Tree on validate data is {clf.score(X_validate, y_validate)}")


# In[16]:


# get_decision_tree(X_train, X_validate, y_train, y_validate)


# In[10]:


def get_random_forest(X_train, X_validate, y_train, y_validate):
    '''This function: 
    returns random forest accuracy on train and validate data'''

    # create model object and fit it to training data
    rf = RandomForestClassifier(max_depth=13, min_samples_leaf=3, random_state=123)
    rf.fit(X_train, y_train)

    # print result
    print(f"Accuracy of Random Forest on train is {rf.score(X_train, y_train)}")
    print(f"Accuracy of Random Forest on validate is {rf.score(X_validate, y_validate)}")


# In[17]:


# get_random_forest(X_train, X_validate, y_train, y_validate)


# In[12]:


def get_log_reg(X_train, X_validate, y_train, y_validate):
    '''This function: 
    returns logistic regression accuracy on train and validate data'''

    # create model object and fit it to the training data
    logit = LogisticRegression(C=9, random_state=123)
    logit.fit(X_train, y_train)

    # print result
    print(f"Accuracy of Logistic Regression on train is {logit.score(X_train, y_train)}")
    print(f"Accuracy of Logistic Regression on validate is {logit.score(X_validate, y_validate)}")


# In[18]:


# get_log_reg(X_train, X_validate, y_train, y_validate)


# In[ ]:




