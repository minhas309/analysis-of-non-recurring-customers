from module1.preprocessing.create import createDataSet
from module1.data_cleaning.cleaning import handlingMissingValues

def module1():

    #Reading data from given dataset
    print('Data Acquisition: creating DataFrame')
    df = createDataSet()

    #Data Cleaning 
    handlingMissingValues(df)

    #Data Transformation

    return df