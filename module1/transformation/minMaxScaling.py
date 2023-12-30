from sklearn.preprocessing import MinMaxScaler
import pandas as pd

def normalization(df, columns_to_drop):
    scaler = MinMaxScaler()

    # Dropping non-numeric and non-relevant columns
    df_ = df.drop(columns=columns_to_drop)
    column_names = df_.columns
    scaled_data = scaler.fit_transform(df_)
    normalized_df = pd.DataFrame(scaled_data, columns=column_names, index=df.index)

    normalized_df.to_csv('transformations/normalization.csv')
    print(normalized_df.tail())


