from module1.preprocessing.create import get_DataSet
from module1.data_cleaning.cleaning import handlingMissingValues

def module1():

    #Reading data from given dataset
    print('Data Acquisition: creating DataFrame')
    df = get_DataSet()

    #Data Cleaning 
    handlingMissingValues(df)

    #Data Transformation

    return df