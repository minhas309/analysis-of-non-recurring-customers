from sklearn.preprocessing import MinMaxScaler
import pandas as pd

def normalization(df, columns_to_drop):
    scaler = MinMaxScaler()

    # Dropping non-numeric and non-relevant columns
    df_ = df.drop(columns=columns_to_drop)
    column_names = df_.columns
    scaled_data = scaler.fit_transform(df_)

    normalized_df = pd.DataFrame(scaled_data, columns=column_names, index=df.index)

    columns_to_preserve = ['Purchase_Amount','Average_Spending_Per_Purchase','Purchase_Frequency_Per_Month','Brand_Affinity_Score']
    df_ = df_[columns_to_preserve]
    df_ = df_.rename(columns=lambda col: 'o' + col)
    final_df = pd.concat([df_, normalized_df], axis=1)

    final_df.to_csv('transformations/normalization.csv')
