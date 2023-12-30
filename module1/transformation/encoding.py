import pandas as pd
import os
from sklearn.preprocessing import OneHotEncoder

def encoding():
    script_dir = os.path.dirname(__file__)
    file_path = os.path.join(script_dir, '../../cleaned/data.csv')
    df = pd.read_csv(file_path)

    # Create a OneHotEncoder object, and ignore unknown categorical values
    encoder = OneHotEncoder(sparse=False, handle_unknown='ignore')

    # Encode the categorical values as numeric using one-hot encoding
    df_encoded = pd.DataFrame(encoder.fit_transform(df[['Product_Category', 'Gender', 'Income_Level', 'Product_Category_Preferences']]))
    df_encoded.columns = encoder.get_feature_names_out(['Product_Category', 'Gender', 'Income_Level', 'Product_Category_Preferences'])

    # Concatenate df and df_encoded and drop the original categorical columns
    df = pd.concat([df, df_encoded], axis=1).drop(['Product_Category', 'Gender', 'Income_Level', 'Product_Category_Preferences'], axis=1)
    return df
