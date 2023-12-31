import matplotlib.pyplot as plt
import seaborn as sns

def brandAffinityPerCluster(data):
    brand_affinity_cols = [col for col in data.columns if 'Brand_Affinity_' in col]
    clustered_brand_affinity = data.groupby('Cluster')[brand_affinity_cols].mean()
    clustered_brand_affinity_transposed = clustered_brand_affinity.transpose()

    # Plotting a heatmap
    plt.figure(figsize=(12, 8))
    sns.heatmap(clustered_brand_affinity_transposed, annot=True, cmap='viridis')
    plt.title('Brand Affinity per Cluster')
    plt.ylabel('Brand')
    plt.xlabel('Cluster')
    plt.show()
    