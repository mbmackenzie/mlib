import pandas as pd

from mlib.ds.dataframes import df_count


def test_df_count():
    test_df = pd.DataFrame({
        "col1": ["A", "B", "A", "A", "A", "B", "A", "B", "A", "A"],
        "col2": ["C", "D", "C", "E", "D", "E", "D", "E", "D", "D"]
    })

    # A is first alphabetically and there are 7 A's in col1
    t1 = df_count(test_df, "col1")
    assert t1.iloc[0].col1 == "A"
    assert t1.iloc[0].n == 7

    # C is first alphabetically and there are 2 C's in col1
    t2 = df_count(test_df, "col2")
    assert t2.iloc[0].col2 == "C"
    assert t2.iloc[0].n == 2

    # There are 5 D's in col2 and it is the most frequent
    t2 = df_count(test_df, "col2", sort=True)
    assert t2.iloc[0].col2 == "D"
    assert t2.iloc[0].n == 5
