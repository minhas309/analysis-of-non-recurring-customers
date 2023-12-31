from sklearn.cluster import KMeans
from sklearn.metrics import calinski_harabasz_score
import pandas as pd

data = pd.read_csv('transformations/normalization.csv')
data = data.drop(['Unnamed: 0'], axis=1)
columns_to_drop = [col for col in data.columns if col.startswith('o')]
data = data.drop(columns=columns_to_drop)

kmeans = KMeans(n_clusters=5, random_state=0)
labels = kmeans.fit_predict(data)

# Calculate the Calinski-Harabasz score
calinski_harabasz_index = calinski_harabasz_score(data, labels)

print(f"Calinski-Harabasz Index: {calinski_harabasz_index}")
