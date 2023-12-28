import pandas as pd
from preprocessing.create import createDataSet
from data_cleaning import cleaning

invalid_values = ['', 'Hidden']

def module1():

    # Reading data from given dataset
    print('Data Acquisition: creating DataFrame')
    df = createDataSet()

    # Data Cleaning
    df = cleaning.dropEmptyRows(df, invalid_values, columns=['Product_ID', 'Product_Category', 'Brand'])
    df = cleaning.rowManipulation(df, invalid_values, columns=['Purchase_Amount', 'Average_Spending_Per_Purchase', 'Purchase_Frequency_Per_Month', 'Brand_Affinity_Score'])
    df = cleaning.forwardFillMethod(df, invalid_values, columns=['Year', 'Month', 'Age', 'Gender'])
    df = cleaning.dateTimeColumn(df)

    # Data Transformation
    df.to_csv('cleaned/data.csv')

    return df

df = module1()
