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

    # Handling Missing Values
    df = cleaning.dropEmptyRows(df, invalid_values, columns=['Product_Category'])
    df = cleaning.rowManipulation(df, invalid_values, columns=['Purchase_Amount', 'Average_Spending_Per_Purchase', 'Purchase_Frequency_Per_Month', 'Brand_Affinity_Score'])
    df = cleaning.forwardFillMethod(df, invalid_values, columns=[ 'Product_ID', 'Purchase_Date', 'Customer_ID','Address', 'Transaction_ID','Year', 'Month', 'Age', 'Gender', 'Income_Level', 'Product_Category_Preferences', 'Brand', 'Season'])
    df = cleaning.dateTimeColumn(df)
    df.to_csv('cleaned/data.csv')

    # Data Transformation
    columns_to_drop = ['Unnamed: 0', 'Customer_ID', 'Address', 'Transaction_ID', 'Purchase_Date', 'Product_ID', 'Brand', 'Month', 'Year', 'Season']
    df1 = encoding()
    normalization(df1, columns_to_drop=columns_to_drop)
    standardization(df1, columns_to_drop=columns_to_drop)

module1()