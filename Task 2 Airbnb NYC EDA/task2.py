'''SWYNEX Technologies - Data Analytics Internship
Task 2 : Exploratory Data Analysis (EDA)
Dataset : cleaned_airbnb_nyc.csv
Author : Waseeque Ahmad (Intern ID : SWX-2026-001813)
'''

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os 

#Style
sns.set_style('whitegrid')
plt.rcParams['figure.figsize'] = (12, 6)
plt.rcParams['font.size'] = 10

#Output folder
os.makedirs('Charts', exist_ok=True)

#Load Dataset
print('Loading Cleaned Dataset')
df = pd.read_csv('cleaned_airbnb_nyc.csv')
print(f'Shape : {df.shape}')
print(f'Coloumns : {df.columns.tolist()}')
print(f'First 5 rows : {df.head()}')

#Basic Statistics
print('\nBasic Statistics:')
print(f'Dataset Info: {df.info()}')
print(f'\nNumerical Summary: {df.describe()}')
print(f'\nMissing Values : {df.isnull().sum()}')

#Univariate Analysis
print('\nUNIVARIATE ANALYSIS')
print('\nRoom Type Distribution')
room_counts = df['room_type'].value_counts()
print(room_counts)
print(f'\nPercentage : \n{(room_counts / len(df) * 100).round(2)}')

plt.figure(figsize=(10, 6))
sns.countplot(data = df, x='room_type', palette='Set2')
plt.title('Distribution of Room Types in NYC Airbnb', fontsize=14, fontweight='bold')
plt.xlabel('Room Types')
plt.ylabel('Number of Listings')
for i, v in enumerate(room_counts.values):
    plt.text(i, v + 5, str(v), ha= 'center', fontweight='bold')
plt.tight_layout()
plt.savefig('Distribution by Room_Types.png', dpi=100, bbox_inches='tight')
plt.show()

print('Neighbourhood Group Distribution:')
nb_count = df['neighbourhood_group'].value_counts()
print(nb_count)
print(f'\nPercentages : \n{(nb_count / len(df)*100).round(2)}')

plt.figure(figsize=(8, 5))
sns.countplot(data=df, x='neighbourhood_group', palette='magma', order=nb_count.index)
plt.title('Listings by Neighbourhood Group', fontsize=14, fontweight='bold')
plt.xlabel('Number of Listings')
plt.ylabel('Borough')
plt.tight_layout()
plt.savefig('Distribution by Neighbourhood Group.png', dpi=100, bbox_inches='tight')
plt.show()

print('\nPrice Statistics:')
print(f'Mean : {df['price'].mean():.2f}')
print(f'Median : {df['price'].median():.2f}')
print(f'Std Dev : {df['price'].std():.2f}')
print(f'Min : {df['price'].min()}')
print(f'Max : {df['price'].max()}')

fig, axes = plt.subplots(1, 2, figsize=(14, 5))
sns.histplot(data = df, x='price', bins=50, kde=True, ax=axes[0], color='steelblue')
axes[0].set_title('Price Distribution', fontweight='bold')
axes[0].set_xlabel('Price($)')

sns.boxplot(data=df, x='price', ax=axes[1], color='coral')
axes[1].set_title('Price Box Plot', fontweight='bold')
axes[1].set_xlabel('Price ($)')
plt.tight_layout()
plt.savefig('Distribution of Price.png', dpi=100, bbox_inches='tight')
plt.show()

print('\nBIVARIATE ANALYSIS')

print('Averge Price by Room Types')
price_by_room = df.groupby('room_type')['price'].mean().sort_values(ascending=False)
print(price_by_room)

plt.figure(figsize=(8, 5))
sns.barplot(data=df, x='room_type', y='price', estimator=np.mean, 
            palette='coolwarm', errorbar=None)
plt.title('Average Price by Room Type', fontsize=14, fontweight='bold')
plt.xlabel('Room Type')
plt.ylabel('Average Price')
for i, v in enumerate(price_by_room):
    plt.text(i, v + 2, f'${v:.0f}', ha='center', fontweight='bold')
plt.tight_layout()
plt.savefig('Price by Room Type.png', dpi=100, bbox_inches='tight')
plt.show()

print('\nAverage Price by Neighbourhood Group:')
price_by_nb = df.groupby('neighbourhood_group')['price'].mean().sort_values(ascending=False)
print(price_by_nb)

plt.figure(figsize=(8, 5))
sns.barplot(data=df, x='neighbourhood_group', y='price', estimator=np.mean,
            palette='Set2', errorbar=None)
plt.title('Average Price by Neighbourhood Group', fontsize=14, fontweight='bold')
plt.xlabel('Borough')
plt.ylabel('Average Price')
for i, v in enumerate(price_by_nb.values):
    plt.text(i, v + 2, f'${v:.0f}', ha='center', fontweight='bold')
plt.tight_layout()
plt.savefig('Price by Borough.png', dpi=100, bbox_inches='tight')
plt.show()

print('\nRoom type vs Neighbourhood (Stacked Bar)')
plt.figure(figsize=(12, 6))
room_nb = pd.crosstab(df['neighbourhood_group'], df['room_type'])
room_nb.plot(kind='bar', stacked=True, figsize=(10, 6), colormap='Set3')
plt.title('Room Type Distribution by Borough', fontsize=14, fontweight='bold')
plt.xlabel('Borough')
plt.ylabel('Number of Listings')
plt.xticks(rotation=45)
plt.legend(title='Room Type')
plt.tight_layout()
plt.savefig('Room Type by Borough.png', dpi=100, bbox_inches='tight')
plt.show()

print('\nGeospatial Analysis')
plt.figure(figsize=(12, 10))
sns.scatterplot(data = df, x='longitude', y='latitude', hue='neighbourhood_group', palette='Set1', size='price', sizes=(10, 300), alpha=0.6)
plt.title('Airbnb Listings Across NYC (Size = Price)', fontsize=14, fontweight='bold')
plt.xlabel('Longitude')
plt.ylabel('Latitude')
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
plt.tight_layout()
plt.savefig('Geospatial Distribution.png', dpi=100, bbox_inches='tight')
plt.show()

print('\nCorrelation Analysis')
numerical_cols = ['price', 'minimum_nights', 'number_of_reviews', 'reviews_per_month',
                  'calculated_host_listings_count', 'availability_365']
correlation = df[numerical_cols].corr()
print(f'\nCorrelation Matrix : {correlation.round(2)}')

plt.figure(figsize=(10, 8))
sns.heatmap(correlation, annot=True, cmap='rocket', fmt='.2f',
            linewidths=0.5, square=True)
plt.title('Correlation Matrix of Numerical Features', fontsize=14, fontweight='bold')
plt.tight_layout()
plt.savefig('Correlation_Matrix.png', dpi=100, bbox_inches='tight')
plt.show()

print('\nTop Neighbourhood Analysis')
top_nb = df['neighbourhood_group'].value_counts().head(10)
print(f'\nTop 10 Neighbourhoods by Listings : \n{top_nb}')

plt.figure(figsize=(10, 6))
sns.barplot(x=top_nb.values, y=top_nb.index, palette='inferno')
plt.title('Top 10 Neighbourhoods by Number of Listings', fontsize=14, fontweight='bold')
plt.xlabel('Number of Listings')
plt.ylabel('Neighbourhood')
plt.tight_layout()
plt.savefig('Top 10 Neighbourhood.png', dpi=100, bbox_inches='tight')
plt.show()

print('\nTop 10 Hosts by Listings')
top_host = df['host_name'].value_counts().head(10)
print(f'\nTop 10 Hosts by Listings : \n{top_host}')

plt.figure(figsize=(10, 6))
sns.barplot(x=top_host.values, y=top_host.index, palette='crest')
plt.title('Top 10 Hosts by Number of Listings', fontsize=14, fontweight='bold')
plt.xlabel('Number of Listings')
plt.ylabel('Host Names')
plt.tight_layout()
plt.savefig('Top Host.png', dpi=100, bbox_inches='tight')
plt.show()

print("EDA It's Done Bro!!")