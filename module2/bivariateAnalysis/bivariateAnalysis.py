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

bins = [18, 25, 35, 45, 55, 65, 75, 85]
bin_labels = ['18-24', '25-34', '35-44', '45-54', '55-64', '65-74', '75-84']

electronics_df['Age_Group'] = pd.cut(electronics_df['Age'], bins=bins, labels=bin_labels, right=False)

plt.subplot(2, 2, 2)
sns.barplot(x='Age_Group', y='Purchase_Frequency_Per_Month', data=electronics_df, edgecolor='grey', color='skyblue')
plt.title('Purchase Frequency vs. Age in Electronics')
plt.xlabel('Age Group')
plt.ylabel('Purchase Frequency')
plt.xticks(rotation=45) 

# 3: Product_Category vs. Brand_Affinity_Score
plt.subplot(2, 2, 3)
heatmap_data = pd.crosstab(df['Product_Category'], df['Brand_Affinity_Score'])
heatmap_data_norm = heatmap_data.div(heatmap_data.sum(axis=1), axis=0)
sns.heatmap(heatmap_data_norm, cmap='coolwarm', annot=True, fmt=".2f", linewidths=.5, cbar_kws={'label': 'Proportion'})
plt.title('Brand Affinity vs. Product Category')
plt.xlabel('Brand Affinity Score')
plt.ylabel('Product Category')

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
sns.set(rc={'figure.figsize': (10, 6)})
sns.set(style="darkgrid")

# Bar Plot: Gender vs. Income Level
plt.subplot(2, 2, 1)
sns.countplot(x='Income_Level', hue='Gender', data=electronics_df, palette='pastel')
plt.title('Distribution of Gender Across Income Levels')
plt.xlabel('Income Level')
plt.ylabel('Count')
plt.legend(title='Gender', loc='lower right')


# Bar Plot: Product Category Based on Brand
plt.subplot(2, 2, 2)
sns.countplot(x='Product_Category', hue='Brand', data=df, palette='pastel')
plt.title('Distribution of Product Categories Based on Brand')
plt.xlabel('Product Category')
plt.ylabel('Count')
plt.legend(title='Brand', loc='lower right')
plt.show()

