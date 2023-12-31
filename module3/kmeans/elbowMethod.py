import pandas as pd
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

def elbowMethod(clusteredData):
    inertia = []
    for i in range(1, 11):
        kmeans = KMeans(n_clusters=i, random_state=0)
        kmeans.fit(clusteredData)
        inertia.append(kmeans.inertia_)

    # Plot the Elbow plot
    plt.figure(figsize=(10, 6))
    plt.plot(range(1, 11), inertia, marker='o')
    plt.title('Elbow Method For Optimal k')
    plt.xlabel('Number of clusters')
    plt.ylabel('Inertia')
    plt.show()
