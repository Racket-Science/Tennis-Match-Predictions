import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime, timedelta

def get_lower_and_upper_bounds(series, multiplier = 1.5):
    '''
    This function defines two paramters, a series and a default multiplier (int or float will do), and returns 
    the upper and lower bounds according to the multipler and series range.
    '''
    
    q1, q3 = series.quantile([.25, .75])    # get quartiles
    iqr = q3 - q1    # calculate inter-quartile range
    inner_lower_fence = q1 - multiplier * iqr    # set lower fence
    inner_upper_fence = q3 + multiplier * iqr    # set upper fence

    return inner_lower_fence, inner_upper_fence  # return lower bound and then upper bound

def get_all_the_bounds(df, quant_vars, multiplier = 1.5):
    
    '''
    This function defines 3 paramaters, a dataframe, a list of variables, and a default multiplier.
    It returns the upper and lower bounds for each variable in the list according to the multipler
    and range of the variable listed.
    '''
    
    bounds = pd.DataFrame()   # set an frame to fill
    for var in quant_vars:     # loop through numeric varumns
        q1, q3 = df[var].quantile([.25, .75])    # get quartiles
        iqr = q3 - q1    # calculate inter-quartile range
        inner_lower_fence = q1 - multiplier * iqr    # set lower fence
        inner_upper_fence = q3 + multiplier * iqr    # set upper fence
        outlier_dict = {'lower_bound': inner_lower_fence,     # add values to dictionary
                        'upper_bound': inner_upper_fence,
                        'feature': var
                       }
        
        bounds = bounds.append(outlier_dict, ignore_index = True)    # design dataframe of bounds
    
    bounds = bounds.set_index('feature')
    
    return bounds    # return bounds in an easy-on-the-eyes dataframe

# this function is inspired by Brent Schriver
def get_out_of_bounds(df, quant_vars, multiplier = 1.5):
    
    '''
    This function defines 3 paramaters, a dataframe, a list of variables, and a default multiplier.
    It returns all of the outliers present in the specified dataframe in a new dataframe
    (outlier classification dependent on set/ default multiplier).
    '''
    
    outliers = pd.DataFrame()
    
    for var in quant_vars:     # loop through numeric varumns
        q1, q3 = df[var].quantile([.25, .75])    # get quartiles
        iqr = q3 - q1    # calculate inter-quartile range
        inner_lower_fence = q1 - multiplier * iqr    # set lower fence
        inner_upper_fence = q3 + multiplier * iqr    # set upper fence
        outliers = outliers.append(df[df[var] < inner_lower_fence])    # add lower outliers to df
        outliers = outliers.append(df[df[var] > inner_upper_fence])    # add upper outliers to df

    return outliers    # return outliers in an easy-on-the-eyes dataframe

def get_below_bounds(df, quant_vars, multiplier = 1.5):

    '''
    This function defines 3 paramaters, a dataframe, a list of variables, and a default multiplier.
    It returns all of the outliers below their respective lower bounds present in the specified dataframe
    in a new dataframe (outlier classification dependent on set/ default multiplier).
    '''
    
    below_ideal = pd.DataFrame()
    for var in quant_vars:
        q1, q3 = df[var].quantile([.25, .75])    # get quartiles
        iqr = q3 - q1    # calculate inter-quartile range
        lower_fence = q1 - multiplier * iqr    # set lower fence
        below_ideal = below_ideal.append(df[df[var] < lower_fence])    # add outliers to dataframe
    
    return below_ideal    # return lower outliers accumulated in a dataframe

def get_above_bounds(df, quant_vars, multiplier = 1.5):
    
    '''
    This function defines 3 paramaters, a dataframe, a list of variables, and a default multiplier.
    It returns all of the outliers above their respective upper bounds present in the specified dataframe
    in a new dataframe (outlier classification dependent on set/ default multiplier).
    '''

    above_bounds = pd.DataFrame()
    
    for var in quant_vars:
        q1, q3 = df[var].quantile([.25, .75])    # get quartiles
        iqr = q3 - q1    # calculate inter-quartile range
        upper_fence = q3 + multiplier * iqr    # set lower fence
        above_bounds = above_bounds.append(df[df[var] > upper_fence])    # add outliers to dataframe
    
    return above_bounds    # return upper outliers accumulated in a dataframe



# ---


#distribution defines two parameters, a dataframe and feature to accept, and plots a histogram with chart mods for clarity
def distribution(df, feature):

    '''
    This function plots a histogram from specified df for specified feature.
    '''
    
    plt.figure(figsize = (13, 7))    # create figure
    df[feature].hist(color = 'teal', bins = 50)    # plot histogram of feature
    f_feature = feature.replace('_', ' ').capitalize()    # re-format string for title
    plt.title(f'Distribution of {f_feature}', size = 13)    # title
    plt.ylabel('Frequency')
    plt.xlabel(f_feature)