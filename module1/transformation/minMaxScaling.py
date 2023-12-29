from sklearn.preprocessing import MinMaxScaler
import pandas as pd

def normalization(df, columns):
    scaler = MinMaxScaler()
    new_columns = ['m' + column for column in columns]
    df[new_columns] = scaler.fit_transform(df[columns])

    df.to_csv('transformations/normalization.csv')
