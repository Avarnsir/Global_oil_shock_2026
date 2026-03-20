import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#import the dataset
df = pd.read_csv('pros_cons_analysis.csv')
print(df.head()) #top 5 rows
print(df.info()) #all the coloumns data type
print(df.isnull().sum()) #sums up all the blank value


#check all the coloumns
print(df.to_string())
