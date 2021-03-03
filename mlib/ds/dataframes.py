from typing import Union, List

import pandas as pd


def df_preview(df: pd.DataFrame) -> pd.DataFrame:
    """To be used in the last line of a Jupyter cell, 
    this function will print the shape of a given dataframe, 
    and return the top 5 rows to be displayed. 

    Args:
        df (pd.DataFrame): The dataframe to preview

    Returns:
        pd.DataFrame: The top 5 rows of the provided dataframe
    """

    print(df.shape)
    return df.head()


def df_count(df: pd.DataFrame, columns: Union[List[str], str], sort: bool = False) -> pd.DataFrame:
    """Similar to the count function in the dplyr package in R, this lets you quickly count 
    the unique values of one or more variables.

    Args:
        df (pd.DataFrame): The dataframe to use
        columns (Union[List[str], str]): The column(s) to group by.
        sort (bool): If True, will show the largest groups at the top.

    Returns:
        pd.DataFrame: [description]
    """

    counts = df.groupby(columns).size().rename("n").reset_index()
    if sort:
        return counts.sort_values("n", ascending=False)
    else:
        return counts.sort_values(columns)
