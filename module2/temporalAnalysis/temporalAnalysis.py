import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('cleaned/data.csv')
electronics_df = df[df['Product_Category'] == 'Electronics']

sns.set(rc={'figure.figsize':(10,6)})

# Subplot 1: Average Spending Over Time by Gender
plt.subplot(2, 2, 1)
sns.lineplot(data=electronics_df, x='Year', y='Average_Spending_Per_Purchase', hue='Gender')
plt.title('Average Spending Over Time by Gender')
plt.xlabel('Year')
plt.ylabel('Average Spending Per Purchase')
plt.legend(loc = 'center left')
plt.show()

# Subplot 2: Purchase Frequency by Month Over with Respect to Age
plt.subplot(3, 2, 1)
sns.lineplot(x='Age', y='Purchase_Frequency_Per_Month', data=electronics_df)
plt.title('Purchase Frequency by Month with Respect to Age')
plt.xlabel('Year')
plt.ylabel('Purchase Frequency Per Month')

# Subplot 2: Purchase Frequency by Month Over with Respect to Age
plt.subplot(3, 2, 2)
sns.lineplot(x='Age', y='Purchase_Frequency_Per_Month', data=df)
plt.title('Purchase Frequency by Month with Respect to Age')
plt.xlabel('Year')
plt.ylabel('Purchase Frequency Per Month Overall')

# Subplot 3: Purchase Amount of Electronics Over the Year
plt.subplot(2, 2, 3)
sns.lineplot(x='Year', y='Purchase_Frequency_Per_Month', hue='Product_Category', data=electronics_df, marker='o')
plt.title('Purchase_Frequency_Per_Month for Electronics Over the Year')
plt.xlabel('Year')
plt.ylabel('Purchase_Frequency_Per_Month')
plt.show()
plt.subplot(2, 2, 1)
sns.lineplot(x='Year', y='Purchase_Frequency_Per_Month', hue='Product_Category', data=df, marker='o')
plt.title('Purchase_Frequency_Per_Month Over the Year (Overall)')
plt.xlabel('Year')
plt.ylabel('Purchase_Frequency_Per_Month')

plt.show()

# Subplot 4: Yearly Performance Comparison (BAR CHART)
plt.subplot(2, 2, 1)
sns.lineplot(x='Month', y='Purchase_Frequency_Per_Month', hue='Season', data=electronics_df,  palette="pastel")
plt.title('Purchase Frequency per Month Over the Seasons in Electronics')
plt.xlabel('Month')
plt.ylabel('Purchase Frequency Per Month')
plt.legend(title='Season', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.tight_layout(h_pad=2, w_pad=2)
plt.show()

# Subplot 5: Purchase Frequency of Each Brand Over Time
plt.subplot(3, 2, 1)
sns.countplot(x='Season', hue='Product_Category_Preferences', data=electronics_df, palette="pastel")
plt.title('Product Category Preferences for Electronics Over the Seasons')
plt.xlabel('Season')
plt.ylabel('Count')
plt.legend(title='Category Preferences', bbox_to_anchor=(1, .4), loc='upper left')

# Subplot 6: Seasonal Purchase Trend by Product Category
plt.subplot(3, 2, 2)
sns.lineplot(x='Season', y='Purchase_Amount', hue='Product_Category', data=electronics_df, marker='o')
plt.title('Seasonal Purchase Trend of Electronics')
plt.xlabel('Season')
plt.ylabel('Purchase Amount')

plt.subplot(3, 2, 3)
sns.lineplot(x='Season', y='Purchase_Amount', hue='Product_Category', data=df, marker='o')
plt.title('Seasonal Purchase Trend')
plt.xlabel('Season')
plt.ylabel('Purchase Amount')

plt.tight_layout(h_pad=2, w_pad=2)
plt.show()