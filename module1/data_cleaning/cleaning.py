import pandas as pd

def dropEmptyRows(df, invalid_values, columns):
    mask = df[columns].isin(invalid_values).any(axis=1)
    df = df[~mask]

    return df

def rowManipulation(df, invalid_values, columns):
    df[columns] = df[columns].replace(invalid_values, pd.NA)
    df[columns] = df[columns].apply(pd.to_numeric, errors='coerce')
    medians = df[columns].median()
    df[columns] = df[columns].fillna(medians)

    return df

def forwardFillMethod(df, invalid_values, columns):
    df[columns] = df[columns].replace(invalid_values, pd.NA).fillna(method='ffill')

    return df

def dateTimeColumn(df):
    df['Purchase_Date'] = pd.to_datetime(df['Purchase_Date'], errors='coerce')
    df.dropna(subset=['Purchase_Date'], inplace=True)

    return df