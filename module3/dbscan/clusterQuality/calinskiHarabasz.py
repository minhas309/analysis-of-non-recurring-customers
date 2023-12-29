from sklearn.cluster import DBSCAN
from sklearn.metrics import calinski_harabasz_score
import pandas as pd

data = pd.read_csv('transformations/normalization.csv')

# Specify the columns to cluster
columns_to_cluster = ['mPurchase_Frequency_Per_Month', 'mBrand_Affinity_Score', 'mAverage_Spending_Per_Purchase', 'mPurchase_Amount']
clustering_data = data[columns_to_cluster]

# Perform DBScan clustering
dbscan = DBSCAN(eps=0.1, min_samples=1)
labels = dbscan.fit_predict(clustering_data)

# Identify noise points as a separate cluster
labels[labels == -1] = max(labels) + 1

# Calculate the Calinski-Harabasz Index
calinski_harabasz_index = calinski_harabasz_score(clustering_data, labels)

print(f"Calinski-Harabasz Index: {calinski_harabasz_index}")
