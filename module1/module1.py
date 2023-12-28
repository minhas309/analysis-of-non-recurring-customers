import pandas as pd
from preprocessing.create import get_DataSet
from data_cleaning import cleaning
from transformation.minMaxScaling import normalization
from transformation.zIndex import standardization
from transformation.encoding import encoding
from data_cleaning import outliers
invalid_values = ['', 'Hidden']

def module1():

    # Reading data from given dataset
    print('Data Acquisition: creating DataFrame')
    df = get_DataSet()

    # Data Cleaning
    df = cleaning.dropEmptyRows(df, invalid_values, columns=['Product_ID', 'Product_Category'])
    df = cleaning.rowManipulation(df, invalid_values, columns=['Purchase_Amount', 'Average_Spending_Per_Purchase', 'Purchase_Frequency_Per_Month', 'Brand_Affinity_Score'])
    df = cleaning.forwardFillMethod(df, invalid_values, columns=[ 'Purchase_Date', 'Customer_ID','Address', 'Transaction_ID','Year', 'Month', 'Age', 'Gender', 'Income_Level', 'Product_Category_Preferences', 'Brand', 'Season'])
    df = cleaning.dateTimeColumn(df)
    df = outliers.handlingOutliers(df, columns=['Purchase_Amount', 'Average_Spending_Per_Purchase', 'Purchase_Frequency_Per_Month', 'Brand_Affinity_Score'])

    df.to_csv('cleaned/data.csv')

    # Data Transformation
    # Encoding
    df = encoding()
    columns = ['Purchase_Amount', 'Average_Spending_Per_Purchase', 'Purchase_Frequency_Per_Month', 'Brand_Affinity_Score']
    normalization(df, columns)
    standardization(df, columns)

module1()