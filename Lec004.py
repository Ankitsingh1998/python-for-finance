#Lecture 4 - Analyzing data

#Stock returns

#pct_change - to calculate the daily returns, i.e., which calculates the percentage change between the current element and prior one.
#pct_change is a pandas function and can be applied to the dataframes

import yfinance as yf

import matplotlib.pyplot as plt

data = yf.Ticker('TSLA')
price = data.history(period='1y')

x = price['Close'].pct_change() #applied on Close column of prices

print(x)

x.plot()
plt.savefig('Tesla_stock_change_past_one_year.png')

x.plot(kind='hist')
#hist - for a histogram.
#A histogram is an approximate representation of the distribution of numerical data.


#After understanding the return distribution, we can calculte return from an investment.
#For this we need to calculate the cumulative returns usig the cumprod() function.

returns = (x + 1).cumprod()

returns.plot()
plt.savefig('Growth_of_a_$1_investment.png')
#This figure will show how a $1 investment would grow.
#cumprod() - used to get a cumulative product over an array of elements and return an array of the results.

"""
#Example to understand cumprod() function:

x = np.array([2, 4, 2])
r = x.cumprod()
print(r)
"""

#Multiple stocks:
import yfinance as yf
import matplotlib.pyplot as plt
 
data = yf.download('AAPL MSFT TSLA', start='2021-06-01') 
data.columns #tell about columns present in the table

x = data['Close']
print(x)

y = data['Close'].pct_change()
print(y)

x.describe() #will give the statistical values
y.describe()

x.plot()
plt.savefig('Multiple_stocks_close.png')
y.plot()
plt.savefig('Multiple_stocks_close_daily_returns.png')

z = (x + 1).cumprod()
z.plot()
plt.savefig('Multiple_stocks_cumulative_product')
#Visualization helps to understand how the stock performs in a given time.


#Correlations - corr() function
#In finance, correlation is a statistic that measures the degree to which two securities move in relation to each other.
data1 = yf.download('MSFT AAPL TSLA GOOG FB NFLX AMZN', start='2020-06-01')
x = data1['Close'].pct_change()

correlation = x.corr()
print(correlation)

#statmodels package - graphical representation
import statsmodels.api as sm
sm.graphics.plot_corr(correlation, xnames=list(x.columns)) #second argument is for column names deruved from original data - Here, company name

"""
#Correlation - How to read correlation from the graph?
#The corr() function results in a matrix that includes values for each stock pair.
#In the range of (-1,1)
#A positive correlation means that the stocks have returns that are positively correlated and move in the same direction.
#+1 means that the returns are perfectly correlated.
#A correlation of 0 shows no relationship between the pair.
#A negative correlation shows that the returns move in different directions.
#Finding stocks that have low correlation helps to diversify an investment portfolio and minimize risk.
"""

#Analyzing a portfolio
import yfinance as yf
import numpy as np
#A hypothetical portfolio of stocks and analyze it by calculating some important metrics.
#Now, defining the stock tickers and the portfolios weights using arrays

stocks = ['MSFT', 'AAPL', 'TSLA', 'GOOG', 'FB', 'NFLX', 'AMZN']
weights = [0.15, 0.1, 0.2, 0.3, 0.1, 0.05, 0.1]

data2 = yf.download(stocks, start='2020-07-01')

x = data2['Close'].pct_change() #daily returns

ret = (x * weights).sum(axis = 1) #portfolio returns
#To get the daily portfolio returns, we multiplied the daily returns by the weights and calculated the sum of the results.

#total cumulative returns for our portfolio
cumulative = (ret + 1).cumprod() 

print(cumulative)

#Now, plotting the cumulative returns will give a better understanding of the data
#And the chart will show how the portfolio works in the period.
cumulative.plot()
plt.savefig('Analyzing_a_portfolio.png')

#Volatility - oftenly, used to measure risk.
#If a stock is very volatile, you can expect large changes in its price and therefore a higher risk.
#Volatility is calculated using the standard deviation of the portfolio return.

volatility = np.std(ret) #daily volatility, multiplying this with square root of total trading days will give the annual volatility
print(volatility)

#Calculation of the annual volatility by taking the square of the number of trading days in a year(252 days) and then multiplying it by the daily volatility.
#There are 252 trading days in a year.

annual_volatility = np.std(ret) * np.sqrt(252) #np.sqrt() - gives square root of any number
#This will return the risk percentage of our portfolio.


#Sharpe ratio - important metric, which is the measure of the risk-adjusted return of a portfolio.
#A portfolio with a higher sharpe ratio is considered better (a better investment).
#Sharpe ratio - (average return) / (volatility)

avg_ret = np.mean(ret) #avergae of the total returns

sharpe_ratio = (avg_ret/volatility)*np.sqrt(252) #To obtain the sharpe ratio we need to multiply the ratio with the square root of number of trading days in a year
print(sharpe_ratio)
#mean/std - sharpe ratio
#sharpe ratios greater than 1 are considered optimal.

"""
#loops - looping
#The process when the code in a loop executes is called iteration.
for k in range(0,5):
    print(k*2)
"""

#portfolio optimization
"""
#Portfoilo optimization: The technique of allocating assets so that it has the maximum return and minimum risk.
#This can be achieved by finding the allocation that results in the maximum sharpe ratio.
#The simplest way to do this is to check many random allocations(weights) and to find the one that has the best sharpe ratio.
#This process of randomly guessing is known as Monte Carlo Simulation.
"""

import yfinance as yf
import numpy as np
import pandas as pd

stocks = ['MSFT', 'AAPL', 'TSLA', 'GOOG', 'FB', 'NFLX', 'AMZN']

data3 = yf.download(stocks, start='2016-07-01')

daily_ret = data3['Close'].pct_change()

p_weights = [] #To store weights, returns, risk, sharpe ratios for each portfolios that we are going to check and then we will choose best among them.
p_returns = []
p_risk = []
p_sharpe = []

#To generate random weights we can use numpy random function

for k in range(0, 1000):
   wts = np.random.uniform(size = len(x.columns)) #numpy random function
   wts = wts/np.sum(wts) #normalization - sum comes to 1.
   
   p_weights.append(wts) 

   #returns
   mean_ret = (daily_ret.mean() * wts).sum()*252
   p_returns.append(mean_ret)

   #volatility
   ret = (daily_ret * wts).sum(axis = 1)
   annual_vol = np.std(ret) * np.sqrt(252)
   p_risk.append(annual_vol)
    
   #Sharpe ratio
   sharpe = (np.mean(ret) / np.std(ret))*np.sqrt(252)
   p_sharpe.append(sharpe)


#Now, we will find the index with maximum sharpe ratio
max_ind = np.argmax(p_sharpe) #argmax() - index that has maximum value

#Max sharpe ratio
max_sr = p_sharpe[max_ind]
print(max_sr)

#weights
max_weight = p_weights[max_ind]
print(max_weight)

#Visualization
series = pd.Series(max_weight, index=x.columns)
series.plot(kind='bar')
plt.savefig('portfolio_optimization.png')

#Plotting the entire 1000 portfolios
#The chart is called Efficient Frontier and shows the returns on the Y-axis and volatility on the X-axis.
plt.scatter(p_risk, p_returns, c=p_sharpe, cmap='plasma')
plt.colorbar(label='Sharpe Ratio')
plt.scatter(p_risk[max_ind], p_returns[max_ind], color='b', marker='*', s=200)
plt.show()
plt.savefig('portfolio_optimizatio_best_allocation.png')

#star marker - showing the most efficient portfolio with the best sharp ratio.
#The Efficient Frontier chart shows the return we can get for the given volatility, or, the volatility that we get for a certain return.

