
"""
Apply function to multiple series
and return a dataframe after processing
"""
df = news_df[["text", "title"]].apply(
    lambda x: pd.Series(
        ( # tuple
            analyzer.polarity_scores(x[0])["compound"],
            analyzer.polarity_scores(x[1])["compound"]
        )
            ), axis=1)
df.columns=["text-compound", "title-compound"]
df.head()
