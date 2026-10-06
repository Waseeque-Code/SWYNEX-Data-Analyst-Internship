import pandas as pd
import numpy as np
import os

#Load dataset 
df = pd.read_csv('Airbnb_in_NYC.csv')
print('First 5 rows')
print(df.head(5))

#Data Exploration
print(f'\nInfo: {df.info()}')
print(f'\nShape: {df.shape}')
print(f'\nColumn Names: {df.columns.tolist()}')
print(f'Statical Summary: {df.describe()}')
print(f'Statistical Summary (Object): {df.describe(include=[object])}')

#Check Missing Values
print(f'\nTotal Missing Values : {df.isnull().sum()}')

#Drop missing names and host_names 
df = df.dropna(subset=['name', 'host_name'])
print(f'\nAfter droping missing rows from names and host_name: {df.isnull().sum()}')

#Handle last_review and reviews_per_month
print(f'Print Sample of Last reviews : {df['last_review'].sample(10)}')
df['last_review'] = pd.to_datetime(df['last_review'], errors='coerce')
print(f'Last review : {df["last_review"].dtype}')

print(f'\nReview_per_month Sample : {df['reviews_per_month'].sample(10)}')
#Fill with 0 means no review
df['reviews_per_month'] = df['reviews_per_month'].fillna(0)
print(f'\nAfter filling Reviews Per Month : {df.isnull().sum()}')

#Handle duplicates 
print(f'Total Duplicates : {df.duplicated().sum()}')

#Data Types
print('\nDataTypes')
print(df.dtypes)

#Handle invalid values
print('\nInvalid Values')

zero_price = (df['price'] == 0).sum()
print(zero_price)

if zero_price > 0:
    print(f'Rows with price =0:\n{df[df['price'] == 0][['id', 'name', 'price']]}')
    df = df[df['price'] > 0]
    print(f'Removed {zero_price} rows with price = 0. New Shape: {df.shape}')

print(f'\nMinimum_nights statistics:')
print(f'Min : {df['minimum_nights'].min()}')
print(f'Max : {df['minimum_nights'].max()}')
print(f'99th Percentile : {df['minimum_nights'].quantile(0.99)}')

extreme_nights = (df['minimum_nights'] > 365).sum()
print(f'\nListings with minimum_nights > 365: {extreme_nights}')

if extreme_nights > 0:
    print(f'Sample extreme values :\n{df[df['minimum_nights'] > 365][['id', 'name', 'minimum_nights']].head()}')
    df = df[df['minimum_nights'] <= 365]
    print(f'Removed {extreme_nights} rows with minimum_nights > 365. New Shape: {df.shape}')

# Outliers
print('Price Outliers:')

Q1 = df['price'].quantile(0.25)
Q3 = df['price'].quantile(0.75)

IQR = Q3 - Q1
lower = Q1 - 1.5 * IQR
upper = Q3 + 1.5 * IQR

print(f'Q1: {Q1}, Q3: {Q3}, IQR: {IQR}')
print(f'Lower bound: {lower:.2f}, upper bound: {upper:.2f}')

outliers = df[(df['price'] < lower) | (df['price'] > upper)]
print(f'\nPrice outliers found: {len(outliers)} ({len(outliers)/len(df)*100:.1f}%)')

if len(outliers) > 0:
    df['price'] = np.where(df['price'] > upper, upper, df['price'])
    print(f'Capped {len(outliers)} outliers to upper bound ({upper:.2f}).')

print(f'\nPrice stats after capping:')
print(f' MIn: {df['price'].min()}')
print(f' Max: {df['price'].max()}')
print(f' Mean: {df['price'].mean():.2f}')
print(f' Median: {df['price'].median():.2f}')

print('Final Vaidation')
print(f'\nFinal Shape : {df.shape}')
print(f'Missing Values : {df.isnull().sum().sum()}')
print(f'Duplicates remaining : {df.duplicated().sum()}')
print(f'Final Dtypes : {df.dtypes}')
print(f'Final 5 rows : {df.head()}')

print('\nSaving Cleaned Dataset')

os.makedirs('data', exist_ok=True)
output_path = 'data/cleaned_airbnb_nyc.csv'
df.to_csv(output_path, index=False)

print(f'Cleaned dataset saved: {output_path}')
print(f' Rows: {len(df)}')
print(f' Columns: {len(df.columns)}')
