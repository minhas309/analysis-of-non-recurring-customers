from sklearn.cluster import KMeans
from sklearn.metrics import davies_bouldin_score
import pandas as pd

data = pd.read_csv('transformations/normalization.csv')

kmeans = KMeans(n_clusters=3, random_state=0)
labels = kmeans.fit_predict(data)

davies_bouldin_index = davies_bouldin_score(data, labels)

print(f"Davies-Bouldin Index: {davies_bouldin_index}")
