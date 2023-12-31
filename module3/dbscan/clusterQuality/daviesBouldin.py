from sklearn.cluster import DBSCAN
from sklearn.metrics import pairwise_distances
import numpy as np
import pandas as pd

# Read your dataset into a DataFrame
data = pd.read_csv('transformations/normalization.csv')
data.drop(['Unnamed: 0'], axis=1, inplace=True)

# Perform DBScan clustering
dbscan = DBSCAN(eps=0.5, min_samples=1)
labels = dbscan.fit_predict(data)

# Compute cluster centers and dispersion
cluster_centers = []
cluster_dispersions = []
for label in np.unique(labels):
    cluster_points = data[labels == label]
    center = np.mean(cluster_points, axis=0)
    dispersion = np.mean(pairwise_distances(cluster_points, [center]))
    cluster_centers.append(center)
    cluster_dispersions.append(dispersion)

# Compute Davies-Bouldin Index
dbi = 0
for i in range(len(cluster_centers)):
    max_similarity = 0
    for j in range(len(cluster_centers)):
        if i != j:
            distance_ij = np.linalg.norm(cluster_centers[i] - cluster_centers[j])
            similarity_ij = (cluster_dispersions[i] + cluster_dispersions[j]) / distance_ij
            max_similarity = max(max_similarity, similarity_ij)
    dbi += max_similarity

dbi /= len(cluster_centers)

print("Davies-Bouldin Index:", dbi)