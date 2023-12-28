from sklearn.cluster import KMeans
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

def kMeansAlgorithm(data, clustering_data, clusters):
    # Define the number of clusters
    k_optimal = clusters

    # Implement K-Means
    kmeans = KMeans(n_clusters=k_optimal, random_state=0)
    cluster_labels = kmeans.fit_predict(clustering_data)

    # Adding cluster labels to the dataset for analysis
    data['Cluster'] = cluster_labels

    # Group the data by clusters
    cluster_groups = data.groupby('Cluster')

    # Analyze each cluster
    for cluster in range(k_optimal):
        cluster_data = cluster_groups.get_group(cluster)
        print(f"Cluster {cluster} characteristics:")
        
        # Calculate and display key features of each cluster
        average_purchase = cluster_data['mPurchase_Amount'].mean()
        average_frequency = cluster_data['mPurchase_Frequency_Per_Month'].mean()
        average_brand_affinity = cluster_data['mBrand_Affinity_Score'].mean()

        print(f"Average Purchase Amount: {average_purchase}")
        print(f"Average Purchase Frequency Per Month: {average_frequency}")
        print(f"Average Brand Affinity Score: {average_brand_affinity}\n")

    return data
