import pandas as pd
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
import matplotlib.pyplot as plt

def silhouetteAnalysis(clustering_data):
    # Range of k to try
    range_n_clusters = list(range(2, 9))

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
