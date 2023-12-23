import pandas as pd

def handlingMissingValues(df):
    #df.fillna(fill_value, inplace=True)
    print(df['Month'].value_counts())
