import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = pd.read_csv('transformations/normalization.csv')
columns_to_drop = ['Unnamed: 0', 'Customer_ID', 'Address', 'Transaction_ID', 'Purchase_Date', 'Product_ID', 'Brand', 'Month', 'Year', 'Season']
clustering_data = data 
# Calculate the correlation matrix
correlation_matrix = clustering_data.corr()

# Visualize the correlation matrix using a heatmap
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt='.2f')
plt.title('Correlation Matrix')
plt.show()
