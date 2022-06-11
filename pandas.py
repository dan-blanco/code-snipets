
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




"""
Perform a backtest on time series data!
"""

def model(x):
    # pretend model.... should be trained, fit return single prediction
    return x.mean()*1.5

data["back_test_pred"] = \
    data["data"].shift(1).rolling(window=40, min_periods=40).apply(model)

data[["data","back_test_pred"]].plot()


"""
Create tensor of window data 
"""
import numpy as np
np.array([
    window_data.ravel()
    for window_data in list(data["data"].rolling(40))
    if len(window_data) == 40
])
