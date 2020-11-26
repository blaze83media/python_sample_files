import numpy as np
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import seaborn as sns

df=pd.read_csv('Pandas1Cleaned.csv') 

#Data Exploration
print(df.columns) 
print(df.head())

a1=df['PID']
a2=df['ST_NUM']
a3=df['ST_NAME']
a4=df['OWN_OCCUPIED']
a5=df['NUM_BEDROOMS']
a6=df['NUM_BATH']
a7=df['SQ_FT']

q2=[a5,a6]

sns.set(style="whitegrid")
tips = q2#sns.load_dataset("tips")
sns.barplot(data=tips)
plt.show()