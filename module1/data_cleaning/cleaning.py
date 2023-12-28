import pandas as pd

# Drop Rows based on the NaN values
def dropEmptyRows(df, invalid_values, columns):
    # Create a boolean mask for rows containing invalid values in any of the specified column
    mask = df[columns].isin(invalid_values).any(axis=1)
    # Drop rows based on the boolean mask
    df = df[~mask]

    return df


# Fill Empty Cells with Column Medians
def rowManipulation(df, invalid_values, columns):
    # Convert invalid values to NaN
    df[columns] = df[columns].replace(invalid_values, pd.NA)
    # Convert specified columns to numeric
    df[columns] = df[columns].apply(pd.to_numeric, errors='coerce')
    # calculate medians
    medians = df[columns].mean()
    # fill data with medians
    df[columns] = df[columns].fillna(medians)

    return df

def forwardFillMethod(df, invalid_values, columns):
    # Fill empty cell by forward fill method to avoid mean centric data and have some randomness in data
    df[columns] = df[columns].replace(invalid_values, pd.NA).fillna(method='ffill')

    return df

def dateTimeColumn(df):
    df['Purchase_Date'] = pd.to_datetime(df['Purchase_Date'], errors='coerce')
    df.dropna(subset=['Purchase_Date'], inplace=True)

    return df