import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

def scatter3DPlot(data):
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
    ax.set_xlabel('Brand')
    ax.set_ylabel('Brand Affinity Score')
    ax.set_zlabel('Cluster')
    plt.title('3D Plot of Brand Affinity, Encoded Brands, and Clusters')

    # Adding a color bar
    cbar = plt.colorbar(scatter)
    cbar.set_label('Cluster')

    plt.show()