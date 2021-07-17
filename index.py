import datetime as dt
import pandas as pd

df = pd.DataFrame({'year': [2021, 2021],
                   'month': [6, 7],
                   'day': [1, 1]},)

# returns datetime objects
df['Timestamp'] = df.apply(lambda row: dt.datetime(row.year, row.month, row.day),
                           axis=1)

# converts to pandas timestamps if desired
df['Timestamp'] = pd.to_datetime(df.Timestamp)


# Create a DatetimeIndex and assign it to the dataframe.
df.index = pd.DatetimeIndex(df.Timestamp)

print(df)