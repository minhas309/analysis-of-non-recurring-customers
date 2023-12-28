import pandas as pd
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

normalized_data = pd.read_csv('transformations/normalization.csv')

# Selecting the relevant columns for clustering
# We have prefixed normalized columns with 'm' or choose relevant columns manually
clustering_columns = [col for col in normalized_data.columns if col.startswith('m')]
clustering_data = normalized_data[clustering_columns]

optimal_clusters = 3
kmeans = KMeans(n_clusters=optimal_clusters, random_state=0)
kmeans.fit(clustering_data)
cluster_labels = kmeans.labels_
normalized_data['Cluster'] = cluster_labels

# Plotting the clusters
plt.figure(figsize=(10, 6))
plt.scatter(normalized_data['mPurchase_Frequency_Per_Month'], normalized_data['mPurchase_Amount'], c=cluster_labels, cmap='viridis', marker='o')
plt.xlabel('Purchase Amount')
plt.ylabel('Purchase Frequency Per Month')
plt.title('Clusters from KMeans')   
plt.show()