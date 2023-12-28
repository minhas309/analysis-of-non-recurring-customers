import pandas as pd
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

# Load the data
encoded_data = pd.read_csv('transformations/normalization.csv')

# Filter for numeric columns
columns_to_cluster = ['mPurchase_Amount', 'Product_Category_Books',	'Product_Category_Clothing','Product_Category_Electronics',	'Income_Level_High',	'Income_Level_Low',	'Income_Level_Medium','Product_Category_Preferences_High',	'Product_Category_Preferences_Low',	'Product_Category_Preferences_Medium', 
                      'mPurchase_Frequency_Per_Month', 'mBrand_Affinity_Score']
clustering_data = encoded_data[columns_to_cluster]

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
