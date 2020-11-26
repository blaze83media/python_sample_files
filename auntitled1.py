
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



#### MODEL GENERATION #########################
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





