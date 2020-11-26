#https://towardsdatascience.com/data-cleaning-with-python-and-pandas-detecting-missing-values-3e9c6ebcf78b
#REAL DATA CLEANING STEPS
import numpy as np
import pandas as pd
#import matplotlib.pyplot as plt

missing_values=['n/a','na','--','HURLEY'] # place all non-standard missing values values in a list
df=pd.read_csv('property data.csv', na_values=missing_values) #attach d list to pd.read_csv(). Pandas would treat them all as NA (missing)
print(df)
print(df.head())  #type of data: st_num(float) st_name(string) own_occupied (categorical string) num_bd (float, int num)

#Standard missing values (empty fields)
print(df['ST_NUM'])   #Standard missing values. SHOWS THE WHOLE COLUMN, pandas replaces empty fileds with NA
#print(df['ST_NUM'].isnull())   #shows all empty fields inST_NUM col as TRUE
## Pandas sees an empty space as NA and a field with NA as empty also

##NON-STANDARD MISSING VALUES 
print(df['NUM_BEDROOMS'])     #Shows all 3 non-standard missing values (n/a, NAN & na)
print(df['NUM_BEDROOMS'].isnull())    #if missing_values above is absent this would show n/a & NAN as true  but na as false
#You need to work thru the data to see all the missing values and add them to the list
#Dont count missing values before converting them to non-std

#unexpected missing value. A case where u find a number in place of a string
#OWN_OCCUPIED column is a categorical col which has a number,12, instead of Y or N
#To handle this simply loop through
##Detect missing values in OWN_OCCUPIED
cnt=0
for row in df['OWN_OCCUPIED']:
    try:
        int(row)                #convert values a number
        df.loc[cnt, 'OWN_OCCUPIED']=np.nan      #np.nan is numpy missing value. Also, loc[] is pandas preferred for modyfying entries
    except ValueError:                  #exception handling for errors
        pass
    cnt+=1

print(df['OWN_OCCUPIED'])
print(df['OWN_OCCUPIED'].isnull())
  
#Summarize the missing values 
print(df.isnull().sum())   #calulate all NA in each column of the table
print(df.isnull().sum().sum())  #sum all NA found in all columns (Total NA)
print(df.isnull().values.any()) #quick check to see if there are any missing values left


###############################################################################
#replace NA with the median value of the column
#column PID
pidMedian=df['PID'].median()             #find the median of a col 
pid=float('%0.2f'% (pidMedian))         #convert the median to 2 decimal places
pid1=df['PID'].fillna(pid, inplace=True)
print(pid1)       #replace NA (missing values) with value of choice or mean

#column ST_NUM
st_numMedian=df['ST_NUM'].median()    
stm=float('%0.2f'% (st_numMedian))    
stm1=df['ST_NUM'].fillna(stm, inplace=True)
print(stm1)  


#column OWN_OCCUPIED  (categorical data)
ownMode=df['OWN_OCCUPIED'].mode()[0]        
ownMode1=df['OWN_OCCUPIED'].fillna(ownMode, inplace=True)
print(ownMode1)


#column NUM_BEDROOMS
num_bedMedian=df['NUM_BEDROOMS'].mode()[0]      
num_bedMedian1=df['NUM_BEDROOMS'].fillna(num_bedMedian, inplace=True)
print(num_bedMedian)

#column NUM_BATH
num_bathMedian=df['NUM_BATH'].median()     
num_b=float('%0.2f'% (num_bathMedian))    
num_b1=df['NUM_BATH'].fillna(num_b, inplace=True)
print(num_b1)

#column SQ_FT
sqfMedian=df['SQ_FT'].median()     
sqf=float('%0.2f'% (sqfMedian))    
sqf1=df['SQ_FT'].fillna(sqf, inplace=True)
print(sqf1) 


###############################################################################

# descriptive stats
print(df['ST_NUM'].mean())  #print mean
print(df['ST_NUM'].median())    #print median
print(df['ST_NUM'].mode())      #print mode
print(df['ST_NUM'].describe())      #print summary stats (mean,SD,range,25-75%)
print(df['ST_NUM'].describe()[7])  #print item 7 on summary stats list
print(df['ST_NUM'].describe()[2])  #std Dev

print(df)
#df.to_csv('Pandas1Cleaned.csv')  #write cleaned data to csv

