from sklearn.cluster import KMeans
from sklearn.metrics import davies_bouldin_score
import pandas as pd

data = pd.read_csv('transformations/normalization.csv')
data = data.drop(['Unnamed: 0'], axis=1)
columns_to_drop = [col for col in data.columns if col.startswith('o')]
data = data.drop(columns=columns_to_drop)

kmeans = KMeans(n_clusters=5, random_state=0)
labels = kmeans.fit_predict(data)

davies_bouldin_index = davies_bouldin_score(data, labels)

print(f"Davies-Bouldin Index: {davies_bouldin_index}")
