import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Read your dataset into a DataFrame
data = pd.read_csv('cleaned/data.csv')
columns_to_cluster = ['Purchase_Amount', 'Purchase_Frequency_Per_Month', 'Brand_Affinity_Score', 'Average_Spending_Per_Purchase', 'Age', 'Year', 'Month']
clustering_data = data[columns_to_cluster]
# Calculate the correlation matrix
correlation_matrix = clustering_data.corr()

# Visualize the correlation matrix using a heatmap
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt='.2f')
plt.title('Correlation Matrix')
plt.show()
