from sklearn.preprocessing import StandardScaler
import pandas as pd

def standardization(df, columns_to_drop):
    scaler = StandardScaler()

    df_ = df.drop(columns=columns_to_drop)
    column_names = df_.columns
    scaled_data = scaler.fit_transform(df_)
    dataFrame = pd.DataFrame(scaled_data, columns=column_names, index=df.index)

    dataFrame.to_csv('transformations/standardization.csv')
