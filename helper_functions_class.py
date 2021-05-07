"""
Here are two different functions used for common data cleaning tasks. 
You can use these functions to load data into a pandas Dataframe.
"""

import numpy as np
import pandas as pd
from sklearn.utils import shuffle



 class CleanData:         
    def __init__(self):
        """
        This init function instantiates objects
        """
        return


 # This function randomizes variables
    def randomize(self, df, seed):
        random_this = shuffle(df,random_state=seed)
        return random_this


# This function determines if there are missing values in the specified DataFrame   
    def null_count(self, df):
        num_nulls = df.isnull().sum().sum()
        return num_nulls

