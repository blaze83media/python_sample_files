import pandas as pd
import datetime
import pandas_datareader.data as web
from pandas import Series, DataFrame

#%matplotlib inline
import matplotlib.pyplot as plt
from matplotlib import style

#Adjust size of matplotlib
import matplotlib as mpl
mpl.rc('figure',figsize=(8, 7))
mpl.__version__


#anaylyzing only Yahoo stocks with start & end dates
start = datetime.datetime(2010, 1, 1)
end = datetime.datetime(2017, 1, 11)
df = web.DataReader("AAPL", 'yahoo', start, end)

#Analyzing stock for 'GE','GOOG','IBM','MSFT'
dfcomp = web.DataReader(['AAPL','GE','GOOG','IBM','MSFT'],'yahoo',start=start,end=end)['Adj Close']
#print(dfcomp.head())
#print(df.head())

# percentage change and correlation function 
retscomp = dfcomp.pct_change()
corr = retscomp.corr()
#print(corr)

# Apple and GE with ScatterPlot to view their return distribution
plt.scatter(retscomp.AAPL, retscomp.GE)
plt.xlabel("Returns AAPL")
plt.ylabel("Returns GE")
plt.legend
plt.show()

#Kernel Density Estimate (KDE). KDE is a fundamental data smoothing problem where inferences about 
#the population are made, based on a finite data sample. 
#It helps generate estimations of the overall distributions.

#estimations of the overall distributions
pd.plotting.scatter_matrix(retscomp, diagonal='kde', figsize=(10,10));

#heat maps to visualize the correlation ranges among the competing stocks. 
#The lighter the color, the more correlated the two stocks are
mk=plt.subplot()
plt.imshow(corr, cmap='hot', interpolation='none')
plt.colorbar()
plt.set_xticks(range(len(corr)), corr.columns)
plt.set_yticks(range(len(corr)), corr.columns)
plt.show()

#this might not show causality, and could just show the trend in the technology 
#industry rather than show how competing stocks

#Stock RETURNS n RISKS
#average of returns (Return Rate) and the standard deviation of returns (Risk).
plt.scatter(retscomp.mean(), retscomp.std())
plt.xlabel("Expected returns")
plt.ylabel("Risk")
plt.legend

for label, x, y in zip(retscomp.columns, retscomp.mean(), retscomp.std()):
    plt.annotate(
            label,
            xy = (x,y), xytext = (20, -20),
            textcoords = 'offset points', ha = 'right', va = 'bottom', 
            bbox = dict(boxstyle = 'round, pad=0.5', fc ='yellow', alpha =0.5),
            arrowprops = dict(arrowstyle = '->', connectionstyle = 'arc3, rad=0')
            )
plt.show()

#stocks from google above are not good to buy but from below google
#a red line failed to show across







###############################################################################################################

## Predicting STOCK PRICE
##We will use these three machine learning models to predict our stocks: Simple Linear Analysis, 
#Quadratic Discriminant Analysis (QDA), and K Nearest Neighbor (KNN). 
#first prepare the High Low Percentage and Percentage Change.
##---------------------------------------------------------------------------
#start,end and df where commented bc they are already written above
#start = datetime.datetime(2010, 1, 1)
#end = datetime.datetime(2017, 1, 11)
#df = web.DataReader("AAPL", 'yahoo', start, end)
##---------------------------------------------------------------------------

dfreg = df.loc[:,['Adj Close','Volume']]
dfreg['HL_PCT'] = (df['High'] - df['Low']) / df['Close'] * 100.0
dfreg['PCT_change'] = (df['Close'] - df['Open']) / df['Open'] *100.0

#print(dfreg.tail())
#print(dfreg['HL_PCT'].tail())
#print(dfreg['PCT_change'].tail())

#clean up and process the data before putting them into the prediction models
#steps for cleanup

#Drop missing value
#Separating the label here, we want to predict the AdjClose
#Scale the X so that everyone can have the same distribution for linear regression
#Finally We want to find Data Series of late X and early X (train) for model generation and evaluation
#Separate label and identify it as y
#Separation of training and testing of model by cross validation train test split


#remove any missing values and replace
dfreg.fillna(value=-99999, inplace=True)

import math
import numpy as np
from sklearn import preprocessing
#keep 1% of data for forecast
forecast_out = int(math.ceil(0.01 * len(dfreg)))

#separate label  (NOTE: CHECK THIS MTHOD HERE AGAIN)
#predict the AdjClose column
forecast_col = 'Adj Close'
dfreg['label'] = dfreg[forecast_col].shift(-forecast_out)
X = np.array(dfreg.drop(['label'], 1))

#scale x to thesame distribution for linear regression
X = preprocessing.scale(X)

#Find data series of late X & early X (train) for model generation & evaluation
X_lately = X[-forecast_out:]
X = X[:-forecast_out]

#Separate label and identify it as y
y = np.array(dfreg.drop(['label'], 1))
y = preprocessing.scale(y)
y_lately = y[-forecast_out:]
y = y[:-forecast_out]



#### Generating MODEL #########################
from sklearn.linear_model import LinearRegression
from sklearn.neighbors import KNeighborsRegressor

from sklearn.linear_model import Ridge
from sklearn.preprocessing import PolynomialFeatures
from sklearn.pipeline import make_pipeline


#simple linear analysis (produces straight line rel btw 2 varibles)
#predicts y when x is used as inputs
#LINEAR REGRESSION

########NOTE: This is not yet done (Find a way to split the data)###############
X_train = X
y_train = y

X_test = X_lately 
y_test = y_lately 

clfreg = LinearRegression(n_jobs = -1)
clfreg.fit(X_train, y_train)


#Quadratic Discriminant analysis (produces straight line & curved relationship btw 2 varibles)
#Quadratic analysis 
clfpoly2 = make_pipeline(PolynomialFeatures(2), Ridge())
clfpoly2.fit(X_train, y_train)

clfpoly3 = make_pipeline(PolynomialFeatures(3), Ridge())
clfpoly3.fit(X_train, y_train)

##KNN (k nearest neighbour) uses similar features to predict values of datapoint
#KNN Regression
clfknn = KNeighborsRegressor(n_neighbors=2)
clfknn.fit(X_train, y_train)



#EVALUATION (this is done using the score method in each trained model)
# The score method finds the mean accuracy of self.predict(x) with y of the test dataset

confidencereg = clfreg.score(X_test, y_test)    #for linear reg
confidencereg2 = clfpoly2.score(X_test, y_test) #for quadratic reg
confidencereg3 = clfpoly3.score(X_test, y_test) #for quadratic reg
confidenceregknn = clfknn.score(X_test, y_test) #for knn reg

print(confidencereg,confidencereg2,confidencereg3,confidenceregknn)

#core (>0.95) for most of the models. However this does not mean we can blindly place our stocks. 
#There are still many issues to consider, especially with different companies that have different price trajectories over time

forecast_set = clf.predict(X_lately)  #this needs check
dfreg['Forecast'] = np.nan

#result should be an array

##Prediction plot
last_date = dfreg.iloc[-1].name
last_unix = last_date
next_unix = last_unix + datetime.timedelta(days=1)

for i in forecast_set:
    next_date = next_unix
    next_unix += datetime.timedelta(days=1)
    dfreg.loc[next_date] = [np.nan for _ in range(len(dfreg.columns)-1)] + [i]
             
    dfreg['Adj Close'].tail(500).plot()
    dfreg['Forecast'].tail(500).plot()
    plt.legend(loc=4)
    plt.xlabel("date")
    plt.ylabel("price")
    plt.show()

































