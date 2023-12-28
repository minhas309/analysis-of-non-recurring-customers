from sklearn.preprocessing import MinMaxScaler
import pandas as pd

def normalization(df, columns):
    # Create a MinMaxScaler object
    scaler = MinMaxScaler()

    # Add a prefix 'm' to each column name in numeric_columns
    new_columns = ['m' + column for column in columns]

    # Apply Min-Max scaling to the specified columns
    df[new_columns] = scaler.fit_transform(df[columns])

    # save the DataFrame after normalization
    df.to_csv('transformations/normalization.csv')
