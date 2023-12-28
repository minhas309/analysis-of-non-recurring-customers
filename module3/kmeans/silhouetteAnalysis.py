import pandas as pd
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
import matplotlib.pyplot as plt

# Load the data
data = pd.read_csv('transformations/normalization.csv')

# Assuming you're using specific columns for clustering
columns_to_cluster = ['mPurchase_Amount', 'Product_Category_Books',	'Product_Category_Clothing','Product_Category_Electronics',	'Income_Level_High',	'Income_Level_Low',	'Income_Level_Medium','Product_Category_Preferences_High',	'Product_Category_Preferences_Low',	'Product_Category_Preferences_Medium', 
                      'mPurchase_Frequency_Per_Month', 'mBrand_Affinity_Score']
clustering_data = data[columns_to_cluster]

# Range of k to try
range_n_clusters = list(range(2, 7))

silhouette_avg_scores = []

for n_clusters in range_n_clusters:
    # Initialize the clusterer with n_clusters
    kmeans = KMeans(n_clusters=n_clusters, random_state=10)
    cluster_labels = kmeans.fit_predict(clustering_data)

    # Calculate the average silhouette score
    silhouette_avg = silhouette_score(clustering_data, cluster_labels)
    silhouette_avg_scores.append(silhouette_avg)

    print("For n_clusters =", n_clusters, "The average silhouette_score is :", silhouette_avg)

# Plotting the silhouette scores
plt.figure(figsize=(10, 6))
plt.plot(range_n_clusters, silhouette_avg_scores, marker='o')
plt.title('Silhouette Scores for Various Numbers of Clusters')
plt.xlabel('Number of Clusters (k)')
plt.ylabel('Silhouette Score')
plt.show()
