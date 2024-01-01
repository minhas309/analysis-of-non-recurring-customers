import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('cleaned/data.csv')
electronics_df = df[df['Product_Category'] == 'Electronics']
sns.set(rc={'figure.figsize':(11,10)})

# 1: Age Histogram
#plot the box plot on the age distribution of the customers per cluster
plt.subplot(2, 2, 1)
sns.boxplot(x='cluster', y='Age', data=df, palette='pastel')
plt.title('Age Distribution')
plt.xlabel('Cluster')
plt.ylabel('Age')

#income level
plt.subplot(2, 2, 2)
sns.countplot(data=df, x='Income_Level', hue='cluster', palette='pastel')
plt.title('Income Level Distribution')
plt.xlabel('Income Level')
plt.ylabel('Count')

# seasonal purchase frequency per clusters
plt.subplot(2, 2, 3)
sns.barplot(data=df, x='Season', y='Purchase_Frequency_Per_Month', hue='cluster', palette='pastel')
plt.title('Seasonal Purchase Distribution')
plt.xlabel('Seasonal Purchase')
plt.ylabel('Count')

#puchase frequency vs brand affinity per clusters 
plt.subplot(2, 2, 4)
sns.barplot(data=df, x='Brand_Affinity_Score', y='Purchase_Frequency_Per_Month', hue='cluster', palette='pastel')
plt.title('Brand Affinity vs Purchase Frequency')
plt.xlabel('Brand Affinity')
plt.ylabel('Purchase Frequency')
plt.legend(loc='lower right')

plt.tight_layout(h_pad=3, w_pad=3)
plt.show()

#Product Catergory distribution per clusters
sns.countplot(data=df, x='Product_Category', hue='cluster', palette='pastel')
plt.title('Product Category Distribution')
plt.xlabel('Product Category')
plt.ylabel('Count')
plt.legend(loc='lower right')

plt.show()