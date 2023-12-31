from sklearn.cluster import KMeans
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from sklearn.decomposition import PCA

def kMeansAlgorithmPP(data, clustering_data, clusters):
    k_optimal = clusters

    pca = PCA(n_components=2)
    reduced_data = pca.fit_transform(clustering_data)

    kmeans = KMeans(n_clusters=k_optimal, init='k-means++', random_state=0)
    cluster_labels = kmeans.fit_predict(reduced_data)

    data['Cluster'] = cluster_labels
    clustering_data['Cluster'] = cluster_labels

    cluster_groups = clustering_data.groupby('Cluster')

    plt.scatter(reduced_data[:, 0], reduced_data[:, 1], c=cluster_labels, cmap='viridis')
    plt.title('KMeans++ Clustering')
    plt.xlabel('Principal Component 1')
    plt.ylabel('Principal Component 2')
    plt.show()
    # Analyze each cluster
    cluster_averages = cluster_groups.agg({
    'oPurchase_Amount': 'mean',
    'oPurchase_Frequency_Per_Month': 'mean',
    'oBrand_Affinity_Score': 'mean'
    }).reset_index()

    cluster_averages.rename(columns={
        'Purchase_Amount': 'Average_Purchase',
        'Purchase_Frequency_Per_Month': 'Average_Frequency',
        'Brand_Affinity_Score': 'Average_Brand_Affinity'
    }, inplace=True)

    print(cluster_averages)
    
    return data
