from sklearn.preprocessing import MinMaxScaler

def normalization(df, columns):
    # Create a MinMaxScaler object
    scaler = MinMaxScaler()

    # Add a prefix 'z' to each column name in numeric_columns
    new_columns = ['m' + column for column in numeric_columns]

    # Apply Min-Max scaling to the specified columns
    df[new_columns] = scaler.fit_transform(df[numeric_columns])

    # save the DataFrame after normalization
    df.to_csv('transformations/normalization.csv')
