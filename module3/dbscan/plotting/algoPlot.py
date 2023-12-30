import matplotlib.pyplot as plt
from sklearn.cluster import DBSCAN
from sklearn.decomposition import PCA
from sklearn.metrics import silhouette_score

def algorithmPlot(data, eps, min_samples):

    # Apply DBSCAN
    dbscan = DBSCAN(eps=eps, min_samples=min_samples)
    labels = dbscan.fit_predict(data)

    # Calculate silhouette score for points assigned to clusters
    silhouette_avg = silhouette_score(data, labels)
    print(f"DBSCAN Silhouette Score: {silhouette_avg}")

    # Apply PCA for dimensionality reduction to 2 columns
    pca = PCA(n_components=2)
    reduced_data = pca.fit_transform(data)

    fig = plt.figure(figsize=(10, 8))
    ax = fig.add_subplot(111)
    # Visualize the results in 2D
    scatter = ax.scatter(reduced_data[:, 0], reduced_data[:, 1], c=labels, cmap='viridis', alpha=0.5)
    plt.title('DBSCAN Clustering (2D)')
    plt.xlabel('Principal Component 1')
    plt.ylabel('Principal Component 2')
    plt.show()