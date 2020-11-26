#PANDAS tutorial      
# df = pd.read_csv(''path/to/brics.csv", index_col=0, sep=',', header=none)   #to load a csv file or use cars=pd.read_csv('cars.csv')
import pandas as pd

ndf = pd.read_csv("1pokemon_data1.csv")  #read files in working dir (install xlrd to access all excel files)
de = pd.read_csv("skaters.csv") 
#dx = pd.read_csv("1pokemon_data1.xlsx") 
km=ndf.describe()    #summary stat for loaded data

df=pd.DataFrame(ndf)     #always dataframe your read files, list of dict after reading
print(df)
print(df[['Name','HP','Attack']][2:5])   #show listed columns rows 2 - 4

print(df)       #show all content in file
print(de)

print(df.head(6))     #show first 6 rows
print(df.columns)     #shows all column titles in the table
print(df.tail(5))     #print last 5 rows

print(df[['Name']])       #show the listed column
print(df[['Name']][2:5])       #show the listed column rows 2 - 4


print(df[['Name','HP','Attack']])   #show the listed column
print(df[['Name','HP','Attack']][2:5])   #show listed columns rows 2 - 4

#another method
print(df.iloc[2:5])    #rows 2 - 4 & all columns
print(df.iloc[2:5,[2,8]])   #rows 2-4 & col 2 & 8 only
print(df.iloc[2:5,[2,3,4,5]])   #rows 2-4 & col 2,3,4 & 5 only
print(df.iloc[[2,3,4,5],[2,3,4,5]])   #rows 2,3,4,5 & cols 2,3,4,5

print(df.iloc[[2,3,4,5]])  #rows 2,3,4,5 & all columns
print(df.iloc[:,[2,3,4,5]])  # all rows & cols 2,3,4,5
print(df.iloc[:,2])   #all rows & col 2
print(df.iloc[:,:])     #all rows & all columns

############loc[]requires u to spell out the data as it is on the table##################################################################
print(df.loc[[2,4]])           #prints the only index rows 2 & 4 with all col
print(df.loc[2,'Speed'])    #prints intercept of row 2 & col: Speed

#################### FLOAT & ROUNDING DECIMAL ################################################
kkm=45.5647899
bza=float('%0.2f'% (kkm))  #2 dec places
bz=float('%0.4f'% (kkm))  #4 dec places
print(bza)
print(bz)
#######################################################################################
'''
v1=df.iloc[:,2]
df.index=v1               #replace index with the values in v1. Index is the numbering col 
print(df)
''' 

'''
bz=input('Name:')
bz=float('%0.20f'% (bz))
print(bz)
'''

###########################################################################################
names = ['United States', 'Australia', 'Japan', 'India', 'Russia', 'Morocco', 'Egypt']   #python variable list
dr =  [True, False, False, False, True, True, True]               #variable
cpc = [809, 731, 588, 18, 200, 70, 45]                      #variable
my_dict= {'country':names,'drives_right':dr,'cars_per_cap':cpc}   #parsed data like object
cars = pd.DataFrame(my_dict)                    # framed data in tabular form
print(cars)                     #prints framed data
print(my_dict)
print(cars['country'])      #prints column
print(cars[['country']])     #prints as col: country only
print(cars[['country','drives_right']])  #prints col: country and drive_right

print(cars[0:3])           #prints across rows 0 to 2
print(cars[3:6])          #prints across rows 3 to 5
print(cars[1:4])         #prints across rows 1 to 3

print(cars.iloc[2])      #prints all row 2
print(cars.iloc[[4,5],[1,2]])  #prints row 4-5, col 1-2

cars.index = ['US', 'AUS', 'JAP', 'IN', 'RU', 'MOR', 'EG']    #REPLACES a col with the data it carries. index is the numbering col
print(cars) 
print(cars.loc[['AUS','EG']])           #prints the rows AUS and EG
print(cars.loc['MOR','drives_right'])    #prints intercept of row: MOR & col: drives_right

print(cars.iloc[[1,2,3]])       #rows 1,2,3
print(cars.iloc[:,2])           #all rows & 3rd col
print(cars.iloc[:,[0,1,2]])     #all rows & col 1,2,3
print(cars.iloc[1:3,[0,2]])     #rows 1 to 2 & col 0 & 2
print(cars.iloc[[1,2,3], [0,1]])     #rows 1,2,3  & col 0,1
print(cars.dtypes)

print(df.head(6))
print(df.columns)

nm=df.iloc[0:8,[1,2,3,4,5]]
#print(df.sort_values(['Name','HP','Attack'], ascending=True))   #sort in ascending
#print(df.sort_values(nm, ascending=True))   #sort in ascending
nm1=df.iloc[:,:6].values  #all rows, cols 0 to 6
print(nm1)



###############################################################################
   
# list of name, degree, score 
nme = ["aparna", "pankaj", "sudhir", "Geeku"] 
deg = ["MBA", "BCA", "M.Tech", "MBA"] 
scr = [90, 40, 80, 98] 
   
# dictionary of lists  
dict = {'name': nme, 'degree': deg, 'score': scr}  
     
dfx = pd.DataFrame(dict) 
  
# saving the dataframe 
dfx.to_csv('file1.csv') 

print(dfx)