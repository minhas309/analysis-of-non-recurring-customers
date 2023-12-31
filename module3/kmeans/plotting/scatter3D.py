import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

def scatter3DPlot(data):
    brand_encoded_cols = [col for col in data.columns if 'Product_Category_' in col]
    brand_affinity_scores = data['Brand_Affinity_Score'] 
    clusters = data['Cluster']

    brand_indices = np.argmax(data[brand_encoded_cols].values, axis=1)

    fig = plt.figure(figsize=(10, 8))
    ax = fig.add_subplot(111, projection='3d')

    # Plotting data
    scatter = ax.scatter(brand_indices, brand_affinity_scores, clusters, c=brand_affinity_scores, cmap='viridis', marker='o')
    ax.set_xticks([0, 1, 2])
    ax.set_xticklabels(['Books', 'Clothing', 'Electronics'])
    ax.set_xlabel('Product')
    ax.set_ylabel('Brand Affinity Score')
    ax.set_zlabel('Cluster')
    plt.title('3D Plot of Brand Affinity, Encoded Brands, and Clusters')

    cbar = plt.colorbar(scatter)
    cbar.set_label('Cluster')
    
    plt.show()