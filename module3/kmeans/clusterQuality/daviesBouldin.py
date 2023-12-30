from sklearn.cluster import KMeans
from sklearn.metrics import davies_bouldin_score
import pandas as pd

data = pd.read_csv('transformations/normalization.csv')

# Specify the columns to cluster
columns_to_cluster = ['mPurchase_Frequency_Per_Month', 'mBrand_Affinity_Score', 'mAverage_Spending_Per_Purchase', 'mPurchase_Amount']
clustering_data = data[columns_to_cluster]

kmeans = KMeans(n_clusters=6, random_state=0)
labels = kmeans.fit_predict(clustering_data)

davies_bouldin_index = davies_bouldin_score(clustering_data, labels)

print(f"Davies-Bouldin Index: {davies_bouldin_index}")
