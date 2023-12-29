from sklearn.cluster import KMeans
from sklearn.metrics import calinski_harabasz_score
import pandas as pd

data = pd.read_csv('transformations/normalization.csv')

columns_to_cluster = ['mPurchase_Frequency_Per_Month', 'mBrand_Affinity_Score', 'mAverage_Spending_Per_Purchase', 'mPurchase_Amount']
clustering_data = data[columns_to_cluster]

kmeans = KMeans(n_clusters=6, random_state=0)
labels = kmeans.fit_predict(clustering_data)

# Calculate the Calinski-Harabasz score
calinski_harabasz_index = calinski_harabasz_score(clustering_data, labels)

print(f"Calinski-Harabasz Index: {calinski_harabasz_index}")
