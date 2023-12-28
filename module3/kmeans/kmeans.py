from sklearn.cluster import KMeans
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

# Load the data
data = pd.read_csv('transformations/normalization.csv')

# Assuming you're using specific columns for clustering
columns_to_cluster = ['mPurchase_Amount', 'Product_Category_Books',	'Product_Category_Clothing','Product_Category_Electronics',	'Income_Level_High',	'Income_Level_Low',	'Income_Level_Medium','Product_Category_Preferences_High',	'Product_Category_Preferences_Low',	'Product_Category_Preferences_Medium', 
                      'mPurchase_Frequency_Per_Month', 'mBrand_Affinity_Score']
clustering_data = data[columns_to_cluster]

# Define the number of clusters
k_optimal = 6 

# Implement K-Means
kmeans = KMeans(n_clusters=k_optimal, random_state=0)
cluster_labels = kmeans.fit_predict(clustering_data)

# Adding cluster labels to the dataset for analysis
data['Cluster'] = cluster_labels

# Group the data by clusters
cluster_groups = data.groupby('Cluster')

# Analyze each cluster
for cluster in range(k_optimal):
    cluster_data = cluster_groups.get_group(cluster)
    print(f"Cluster {cluster} characteristics:")
    
    # Calculate and display key features of each cluster
    average_purchase = cluster_data['mPurchase_Amount'].mean()
    average_frequency = cluster_data['mPurchase_Frequency_Per_Month'].mean()
    average_brand_affinity = cluster_data['mBrand_Affinity_Score'].mean()

    print(f"Average Purchase Amount: {average_purchase}")
    print(f"Average Purchase Frequency Per Month: {average_frequency}")
    print(f"Average Brand Affinity Score: {average_brand_affinity}\n")


product_category_cols = data.columns[data.columns.isin(['Product_Category_Books', 'Product_Category_Electronics', 'Product_Category_Clothing'])]
clustered_preferences = data.groupby('Cluster')[product_category_cols].mean()

# Transposing for easier plotting
clustered_preferences_transposed = clustered_preferences.transpose()

# Plotting
plt.figure(figsize=(12, 8))
sns.heatmap(clustered_preferences_transposed, annot=True, cmap='viridis')
plt.title('Product Category Preferences per Cluster')
plt.ylabel('Product Category')
plt.xlabel('Cluster')
plt.show()

# Assuming 'data' is your DataFrame containing both cluster labels and brand affinity data
# Replace 'Brand_Affinity_' with the prefix used for your brand affinity columns

# Aggregating brand affinity data per cluster
brand_affinity_cols = [col for col in data.columns if 'mBrand_Affinity_' in col]
clustered_brand_affinity = data.groupby('Cluster')[brand_affinity_cols].mean()

# Transposing for easier plotting in case of a heatmap
clustered_brand_affinity_transposed = clustered_brand_affinity.transpose()

# Plotting a heatmap
plt.figure(figsize=(12, 8))
sns.heatmap(clustered_brand_affinity_transposed, annot=True, cmap='viridis')
plt.title('Brand Affinity per Cluster')
plt.ylabel('Brand')
plt.xlabel('Cluster')
plt.show()


brand_encoded_cols = [col for col in data.columns if 'Brand_Brand_' in col]
brand_affinity_scores = data['mBrand_Affinity_Score']  # Replace with your actual column name
clusters = data['Cluster']

# Create a numerical representation for brand names (e.g., 0, 1, 2, ...)
brand_indices = np.argmax(data[brand_encoded_cols].values, axis=1)

# Create a 3D plot
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

# Plotting data
scatter = ax.scatter(brand_indices, brand_affinity_scores, clusters, c=brand_affinity_scores, cmap='viridis', marker='o')
ax.set_xticks([0, 1, 2])
ax.set_xticklabels(['A', 'B', 'C'])
# Adding labels and title
ax.set_xlabel('Brand Index')
ax.set_ylabel('Brand Affinity Score')
ax.set_zlabel('Cluster')
plt.title('3D Plot of Brand Affinity, Encoded Brands, and Clusters')

# Adding a color bar
cbar = plt.colorbar(scatter)
cbar.set_label('Cluster')

plt.show()