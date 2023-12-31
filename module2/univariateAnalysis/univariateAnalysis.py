import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('cleaned/data.csv')

sns.set(rc={'figure.figsize':(11,10)}) 
sns.set(style="darkgrid")
electronics_df = df[df['Product_Category'] == 'Electronics']

# 1: Age Histogram
plt.subplot(2, 2, 1)
sns.histplot(electronics_df['Age'].astype(int), bins=10, kde=True)
plt.title('Distribution of Ages')
plt.xlabel('Age')
plt.ylabel('Frequency')

# 2: Gender Bar Plot
plt.subplot(2, 2, 2)
sns.countplot(x='Gender', data=electronics_df, palette='pastel')
plt.title('Gender Distribution')
plt.xlabel('Gender')
plt.ylabel('Count')

# 3: Box Plot for Purchase Amount
plt.subplot(2, 2, 3)
sns.boxplot(y='Purchase_Amount', data=electronics_df, width=.2)
plt.title('Distribution of Purchase Amounts')
plt.ylabel('Purchase Amount')

# 4: Pie Chart for Income Level
plt.subplot(2, 2, 4)
electronics_df['Income_Level'].value_counts().plot.pie(autopct='%1.1f%%', colors=sns.color_palette('pastel'), startangle=90, wedgeprops=dict(edgecolor='black'))
plt.title('Distribution of Income Levels')
plt.ylabel('')

plt.tight_layout(h_pad=3, w_pad=3)
plt.show()

# Setting up the figure
plt.figure(figsize=(15, 5))

# Plotting Customer Age
plt.subplot(1, 3, 1)
sns.histplot(df['Age'], kde=True)
plt.title('Distribution of Customer Age')

# Plotting Purchase Frequency
plt.subplot(1, 3, 2)
sns.histplot(electronics_df['Purchase_Frequency_Per_Month'], kde=True)
plt.title('Distribution of Purchase Frequency in Electronics')

# Plotting Purchase Frequency
plt.subplot(1, 3, 3)
sns.histplot(df['Purchase_Frequency_Per_Month'], kde=True)
plt.title('Distribution of Purchase Frequency')

plt.tight_layout()
plt.show()
# Pie Chart: Seasonal Distribution of Purchase Amounts
seasonal_purchase_amounts = electronics_df.groupby('Season')['Purchase_Amount'].sum()
plt.figure(figsize=(6, 5))
plt.pie(seasonal_purchase_amounts, labels=seasonal_purchase_amounts.index, autopct='%1.1f%%', colors=sns.color_palette('pastel'), startangle=90, wedgeprops=dict(edgecolor='black'))
plt.title('Seasonal Distribution of Purchase Amounts in Electronics')
plt.show()

#pie chart: income level distribution
plt.figure(figsize=(6, 5))
plt.pie(df['Income_Level'].value_counts(), labels=df['Income_Level'].value_counts().index, autopct='%1.1f%%', colors=sns.color_palette('pastel'), startangle=90, wedgeprops=dict(edgecolor='black'))
plt.title('Income Level Distribution')
plt.show()

# Descriptive Statistics
age_desc = df['Age'].describe()
purchase_amount_desc = df['Purchase_Amount'].describe()
purchase_frequency_desc = df['Purchase_Frequency_Per_Month'].describe()

print(age_desc, purchase_amount_desc, purchase_frequency_desc)