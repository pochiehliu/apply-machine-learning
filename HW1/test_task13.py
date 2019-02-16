import pandas as pd

"""
    Write a test that reads input.txt as provided in your repository using 
    pandas. It’s countries population from 1980 to 2010. Test that the number 
    of rows in the data is 225 and the number of columns is 31 (using the 
    country as an index). Given the correct options this file will parse 
    without changes. Write a separate test that tests that the world 
    population according to this table in 2010 is ca. 7065 million.
    """
"""
reference
https://stackoverflow.com/questions/13824840/escaped-quotes-in-pandas-read-csv
"""


def test_row_col_num():
  
    # read file and extract row and col number
    df = pd.read_csv('input.txt',
                    sep=',',
                    na_values=["--", "NA"],
                    encoding='utf-16',
                    index_col=0,
                    header=0,
                    escapechar='\\')

    row, col = df.shape

    # check
    assert row == 225, 'Number of row should be 225'
    assert col == 31, 'Number of column should be 31'
    
    return df
    

def test_world_pop():
    
    # read file
    df = test_row_col_num()
    
    # extract 2010 populaition
    pop = df.sum().loc['2010'].round()
    
    # check 
    assert int(pop) == 7065, 'World population in 2010 should be 7065 million'