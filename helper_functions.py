"""
Here are two different functions used for common data cleaning tasks. 
You can use these functions to load data into a pandas Dataframe.
"""

import numpy as np
import pandas as pd
from sklearn.utils import shuffle


 # This function randomizes variables
def randomize(df, seed):
    random_this = random.shuffle(df,random_state=seed)
    return random_this


# This function determines if there are missing values in the specified DataFrame
def null_count(df):
    num_nulls = df.isnull().sum().sum()
    return num_nulls


