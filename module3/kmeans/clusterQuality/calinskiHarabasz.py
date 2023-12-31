from sklearn.cluster import KMeans
from sklearn.metrics import calinski_harabasz_score
import pandas as pd

data = pd.read_csv('transformations/normalization.csv')

kmeans = KMeans(n_clusters=3, random_state=0)
labels = kmeans.fit_predict(data)

# Calculate the Calinski-Harabasz score
calinski_harabasz_index = calinski_harabasz_score(data, labels)

print(f"Calinski-Harabasz Index: {calinski_harabasz_index}")
