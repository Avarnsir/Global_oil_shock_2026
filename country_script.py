import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#import the dataset
df = pd.read_csv('country_impact.csv')
#print(df.head()) #top 5 rows
#print(df.info()) #all the coloumns data type
#print(df.isnull().sum()) #sums up all the blank value
#print(df[['Region','Vulnerability']])

severity_map = {
    'Low': 1,
    'Moderate': 2,
    'High': 3,
    'Critical': 4
}

df['Severity_Score'] = df['Vulnerability'].map(severity_map)

region_score = df.groupby('Region')['Severity_Score'].mean().sort_values(ascending=False)

print(region_score)


plt.figure(figsize=(10,5))

region_score.plot(kind='bar')

plt.title('Average Vulnerability by Region')
plt.ylabel('Severity Score')
plt.xlabel('Region')
plt.xticks(rotation=45)
plt.tight_layout()

plt.savefig('region_vulnerability.png')
