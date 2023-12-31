import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('cleaned/data.csv')
electronics_df = df[df['Product_Category'] == 'Electronics']

pastel_palette = sns.color_palette('pastel')
border_color = 'black'
sns.set(rc={'figure.figsize': (16, 10)})
sns.set(style="darkgrid")

# 1: Purchase Amount vs. Income Level
plt.subplot(2, 2, 1)
sns.boxplot(x='Income_Level', y='Purchase_Amount', data=electronics_df, palette=pastel_palette, boxprops=dict(edgecolor=border_color), capprops=dict(color=border_color))
plt.title('Purchase Amount vs. Income Level in Electronics')
plt.xlabel('Income Level')
plt.ylabel('Purchase Amount')

# 2: Purchase Frequency vs. Age
plt.subplot(2, 2, 2)
sns.scatterplot(x='Age', y='Purchase_Frequency_Per_Month', data=electronics_df, edgecolor=border_color, color=pastel_palette[0])
plt.title('Purchase Frequency vs. Age in Electronics')
plt.xlabel('Age')
plt.ylabel('Purchase Frequency')

# 3: Product_Category vs. Brand_Affinity_Score
plt.subplot(2, 2, 3)
heatmap_data = pd.crosstab(df['Product_Category'], df['Brand_Affinity_Score'])
heatmap_data_norm = heatmap_data.div(heatmap_data.sum(axis=1), axis=0)
sns.heatmap(heatmap_data_norm, cmap='coolwarm', annot=True, fmt=".2f", linewidths=.5, cbar_kws={'label': 'Proportion'})
plt.title('Brand Affinity vs. Product Category Preferences')
plt.xlabel('Brand Affinity Score')
plt.ylabel('Product Category Preferences')

# 4: Purchase_Frequency_Per_Month over season (BAR CHART)
plt.subplot(2, 2, 4)
sns.barplot(x='Season', y='Purchase_Frequency_Per_Month', data=electronics_df, palette="pastel")
plt.title('Purchase Frequency Over the Seasons in Electronics')
plt.xlabel('Season')
plt.ylabel('Purchase Frequency')
plt.tight_layout(h_pad=2, w_pad=2)

plt.subplots_adjust(hspace=0.5, wspace=0.3)

plt.show()

pastel_palette = sns.color_palette('pastel')
border_color = 'black'
sns.set(rc={'figure.figsize': (8, 9)})
sns.set(style="darkgrid")

# Bar Plot: Gender vs. Income Level
plt.subplot(2, 2, 1)
sns.countplot(x='Income_Level', hue='Gender', data=electronics_df, palette='pastel')
plt.title('Distribution of Gender Across Income Levels')
plt.xlabel('Income Level')
plt.ylabel('Count')
plt.legend(title='Gender', loc='upper right')
plt.show()

# Bar Plot: Product Category Based on Brand
plt.subplot(2, 2, 2)
sns.countplot(x='Product_Category', hue='Brand', data=df, palette='pastel')
plt.title('Distribution of Product Categories Based on Brand')
plt.xlabel('Product Category')
plt.ylabel('Count')
plt.legend(title='Brand', loc='upper right')
plt.show()

