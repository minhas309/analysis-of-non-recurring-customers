from sklearn.cluster import DBSCAN
from sklearn.metrics import calinski_harabasz_score
import pandas as pd

data = pd.read_csv('transformations/normalization.csv')
data.drop(['Unnamed: 0'], axis=1, inplace=True)
columns_to_drop = [col for col in data.columns if col.startswith('o')]
data.drop(columns=columns_to_drop, inplace=True)

dbscan = DBSCAN(eps=0.5, min_samples=1)
labels = dbscan.fit_predict(data)

# Identify noise points as a separate cluster
labels[labels == -1] = max(labels) + 1

# Calculate the Calinski-Harabasz Index
calinski_harabasz_index = calinski_harabasz_score(data, labels)

print(f"Calinski-Harabasz Index: {calinski_harabasz_index}")
