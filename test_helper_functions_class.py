"""
We're going to test two functions using the pytest feature
"""


import pandas as pd
import numpy as np
from sklearn.utils import shuffle
import pytest
from lambdata.helper_functions_class import CleanData


# DataFrame for testing -- thee toy DataFrame
df = pd.DataFrame([[1, 69, 1, 2, 98], [3, 33, 66, 4, 42], [5, 6, 31, 7, 8]], 
columns = ['A', 'B', 'C', 'D', 'E'])


# Testing CleanData class
def test_type_int():
    '''
    Confirms null_count
    '''
    null_count = CleanData().null_count(df
                                        )
    assert isinstance(null_count, np.int64)

def test_randomize():
    '''
    Confirming length of randomized df
    '''
    df_random = CleanData().randomize(df, 69
                                      )
    assert len(df_random) == len(df
                                )