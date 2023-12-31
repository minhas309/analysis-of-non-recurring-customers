import matplotlib.pyplot as plt
import seaborn as sns

def productCategoryPerCluster(data):

    product_category_cols = data.columns[data.columns.isin(['Product_Category_Books', 'Product_Category_Electronics', 'Product_Category_Clothing'])]
    clustered_preferences = data.groupby('Cluster')[product_category_cols].mean()

    clustered_preferences_transposed = clustered_preferences.transpose()

    # Plotting
    plt.figure(figsize=(12, 8))
    sns.heatmap(clustered_preferences_transposed, annot=True, cmap='viridis')
    plt.title('Product Category Preferences per Cluster')
    plt.ylabel('Product Category')
    plt.xlabel('Cluster')
    plt.show()
