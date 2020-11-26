#https://towardsdatascience.com/inferential-statistics-series-t-test-using-numpy-2718f8f9bf2f
## Import the packages
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import scipy
from scipy import stats

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
xc=[2,3,4,5,6,7,10,9,7,8]
xc1=[2,4,6,8,10,12,14,16,18,20]
xc2=[1,2,3,4,5,6,7,8,9,4]


#####################################################################################
print(df.describe())    #show summary stat of table

print(a6)
print(stats.normaltest(a6))     #normality test
print(stats.describe(a6))      #desciptive stats
print(stats.mode(a6))   #mode
print(stats.variation(a6))   #coefficient of variance
#standard deviation is sq rt of variance 
print(a6.describe()[2])  #StdDev

oneT_test=stats.ttest_1samp(a5,5.0)     #one sample T-test
print(oneT_test)

indT_test=stats.ttest_ind(a5,a6, equal_var = False)  #Two-sample independent T-test
print(indT_test)


depT_test=stats.ttest_rel(a5,a6)    #Two-sample dependent T-test
print(depT_test)


one_wayAnova=stats.f_oneway(xc,xc1,xc2)    #one way anova
print(one_wayAnova)






