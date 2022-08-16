
"""
Apply function to multiple series
and return a dataframe after processing

pretend do_something returns a dict with a key "result" that we want as new columns
"""
df = old_df[["col1", "col2"]].apply(
    lambda x: pd.Series(
        ( # tuple
            do_something(x[0])["result"],
            do_something(x[1])["result"]
        )
            ), axis=1)
df.columns=["col1-result", "col2-result"]
df.head()

