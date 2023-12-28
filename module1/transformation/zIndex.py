from sklearn.preprocessing import StandardScaler

def standardization(df, columns):
    # Create a StandardScaler object
    scaler = StandardScaler()

    # Add a prefix 'z' to each column name in numeric_columns
    new_columns = ['z' + column for column in columns]

    # Apply Z-score standardization to the specified columns and create new columns
    df[new_columns] = scaler.fit_transform(df[columns])

    # save the DataFrame after standardization
    df.to_csv('transformations/standardization.csv')
