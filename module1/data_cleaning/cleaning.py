import pandas as pd
from module1.preprocessing.create import get_DataSet

df = get_DataSet()

def handlingMissingValues(df):
    #df.fillna(fill_value, inplace=True)
    print(df['Month'].value_counts())

handlingMissingValues(df)