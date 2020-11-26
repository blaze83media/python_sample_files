#https://towardsdatascience.com/in-12-minutes-stocks-analysis-with-pandas-and-scikit-learn-a8d8a7b50ee7
import pandas as pd
import datetime
import pandas_datareader.data as web
from pandas import Series, DataFrame
#Pandas web data reader is an extension of pandas library to communicate with most updated financial data. T
#this will include sources as: Yahoo Finance, Google Finance, Enigma, etc.


start = datetime.datetime(2010, 1, 1)
end = datetime.datetime(2017, 1, 11)

df = web.DataReader("AAPL", 'yahoo', start, end)

print(df.head())
print(df.tail())

#The above code pulls 7 years data from January 2010 until January 2017.
#Closing Price which remarks the final price in which the stocks are traded by the end of the day.
#  Rolling Mean and Return Rate of Stocks

close_px = df['Adj Close']
mavg = close_px.rolling(window=100).mean()
# Moving Average for the last 100 windows (100 days) of stocks closing price and take the 
#average for each of the window’s moving average. 

print(mavg)

#%matplotlib inline
import matplotlib.pyplot as plt
from matplotlib import style

#Adjust size of matplotlib
import matplotlib as mpl
mpl.rc('figure',figsize=(8, 7))
mpl.__version__

#Adjust the style of matplotlib
style.use('ggplot')

#this plot is simply moving avg (closing) vs moving avg mean
close_px.plot(label='AAPL')
mavg.plot(label='mavg')
plt.legend()


#Expected Return measures the mean, or expected value, of the probability distribution of investment 
#returns. The expected return of a portfolio is calculated by multiplying the weight of each asset by 
#its expected return and adding the values for each investment — Investopedia.
#returns code

rets = close_px / close_px.shift(1) - 1
rets.plot(label='return')


#conclusion: Logically, our ideal stocks should return as high and stable as possible. If you are risk 
#averse(like me), you might want to avoid this stocks as you saw the 10% drop in 2013. This decision is 
#heavily subjected to your general sentiment of the stocks and competitor analysis.