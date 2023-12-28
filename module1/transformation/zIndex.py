from sklearn.preprocessing import StandardScaler

def standardization(df, columns):
    # Create a StandardScaler object
    scaler = StandardScaler()

    # Add a prefix 'z' to each column name in numeric_columns
    new_columns = ['z' + column for column in numeric_columns]

    # Apply Z-score standardization to the specified columns and create new columns
    df[new_columns] = scaler.fit_transform(df[numeric_columns])

    # save the DataFrame after standardization
    df.to_csv('transformations/standardization.csv')
