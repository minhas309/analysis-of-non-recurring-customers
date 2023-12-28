import pandas as pd
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

# Load the data
encoded_data = pd.read_csv('transformations/normalization.csv')

# Filter for numeric columns
numeric_columns = encoded_data.select_dtypes(include=['float64', 'int64']).columns
clustering_data = encoded_data[numeric_columns]

# Apply K-Means and find inertia
inertia = []
for i in range(1, 11):
    kmeans = KMeans(n_clusters=i, random_state=0)
    kmeans.fit(clustering_data)
    inertia.append(kmeans.inertia_)

# Plot the Elbow plot
plt.figure(figsize=(10, 6))
plt.plot(range(1, 11), inertia, marker='o')
plt.title('Elbow Method For Optimal k')
plt.xlabel('Number of clusters')
plt.ylabel('Inertia')
plt.show()
