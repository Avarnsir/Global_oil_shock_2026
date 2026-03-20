import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#import the dataset
df = pd.read_csv('country_impact.csv')
#print(df.head()) #top 5 rows
#print(df.info()) #all the coloumns data type
#print(df.isnull().sum()) #sums up all the blank value

print(df[['Country','GDP_Impact_Pct','Inflation_Risk','Stock_Market_Change','Currency_Pressure']])
