from sklearn.cluster import KMeans
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from sklearn.decomposition import PCA

def kMeansAlgorithm(data, clustering_data, clusters):
    # Define the number of clusters
    k_optimal = clusters

    # Choose the number of components (in this case, 2)
    pca = PCA(n_components=2)
    reduced_data = pca.fit_transform(clustering_data)

    # Implement K-Means
    kmeans = KMeans(n_clusters=k_optimal, init='random', random_state=0)
    cluster_labels = kmeans.fit_predict(reduced_data)

    # Adding cluster labels to the dataset for analysis
    data['Cluster'] = cluster_labels

    # Group the data by clusters
    cluster_groups = data.groupby('Cluster')

    plt.scatter(reduced_data[:, 0], reduced_data[:, 1], c=cluster_labels, cmap='viridis')
    plt.title('KMeans Clustering')
    plt.xlabel('Principal Component 1')
    plt.ylabel('Principal Component 2')
    plt.show()
    # Analyze each cluster
    for cluster in range(k_optimal):
        cluster_data = cluster_groups.get_group(cluster)
        print(f"Cluster {cluster} characteristics:")
        
        # Calculate and display key features of each cluster
        average_purchase = cluster_data['Purchase_Amount'].mean()
        average_frequency = cluster_data['Purchase_Frequency_Per_Month'].mean()
        average_brand_affinity = cluster_data['Brand_Affinity_Score'].mean()

        print(f"Average Purchase Amount: {average_purchase}")
        print(f"Average Purchase Frequency Per Month: {average_frequency}")
        print(f"Average Brand Affinity Score: {average_brand_affinity}\n")

    return data
