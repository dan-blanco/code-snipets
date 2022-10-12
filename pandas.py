
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


## Normalize JSON Data
import pandas as pd

# credit to Oyenike for explode and json_normalize

# read data from URL
data = pd.read_json("https://the-software-guild.s3.amazonaws.com/techstart-1909/data-files/laureate.json")

# normalize the data
laur = pd.json_normalize(data["laureates"])

# normalize the prices data
# explode transforms list like oject to dict 
prizes = pd.json_normalize(laur["prizes"].explode())

# normalize affiliations. 
# we end up with some empty list, it causes an error with json_normalize
# to fix it we apply a function to replace any list with an empty {}
affilliations = pd.json_normalize(prizes["affiliations"].explode().apply(lambda x: {} if isinstance(x, list) else x))

# example of using pandas to count number of laureates in each country and sort it
# to help explain the group by and aggregator function, the sql code would return the same thing
""" SELECT COUNT(*) FROM lauretes GROUP BY bornCountryCode ORDER BY COUNT(*) """
laur.groupby(['bornCountryCode'])['bornCountryCode'].count().sort_values()
