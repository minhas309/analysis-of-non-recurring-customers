from sklearn.cluster import DBSCAN
from sklearn.metrics import silhouette_score

def dbScanAlgorithm(data, eps, min_samples):

    # Apply DBSCAN
    dbscan = DBSCAN(eps=eps, min_samples=min_samples)
    labels = dbscan.fit_predict(data)

    # Calculate silhouette score for points assigned to clusters
    silhouette_avg = silhouette_score(data, labels)
    print(f"DBSCAN Silhouette Score: {silhouette_avg}")