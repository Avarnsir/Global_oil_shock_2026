import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#import the dataset
df = pd.read_csv('petrol_prices_comparison.csv')
#print(df.head()) #top 5 rows
#print(df.info()) #all the coloumns data type
#print(df.isnull().sum()) #sums up all the blank value
print(df[['Country','Amount_Change']])


##Plot a graph
plt.figure(figsize=(19,6))
plt.plot(df['Country'], df['Amount_Change'], marker='o', linestyle='-')
plt.title("Amount_Change")
plt.ylabel('Amount Change')
plt.xlabel('Country')
plt.savefig('amount_change_country.png')
