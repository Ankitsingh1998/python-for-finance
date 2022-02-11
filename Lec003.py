#Lecture 3 - Accessing data

#Accessing financial data from the web - web scraping and python package

#Web scraping - It is the process of using a program to extract content and data from a website.
#Web scraping extracts the underlying HTML code of a website.
#can scrape any public web page.

#yfinance - a python package to access data from the Yahoo finance.
#Yahoo Finance is a reliable and popular source for financial data.
#Yahoo Finance - provides data on companies, their financial performance and profile.

#pandas - used to scrape and store data in tabular format.
#Series and DataFrame - two primary components of pandas
#Series - a column (like an array)
#DataFrame - multi-dimensional table (similar to a spreadsheet, storing data in rows and columns) made up of a collection of series(a collection of arrays).

import pandas as pd
prices = [42.8, 102.03, 240.38, 80.9]
series1 = pd.Series(prices)
series1.describe() #describe - function to see the key statistics


data = {'dates':['2021-06-10', '2021-06-11', '2021-06-12', '2021-06-13'], 
          'prices':[42.8, 102.03, 240.38, 80.9]}
df = pd.DataFrame(data)
print(df)
df.describe()

#read_html() - function to convert tables on web pages to DataFrames
data = pd.read_html('https://en.wikipedia.org/wiki/List_of_S%26P_500_companies')
print(data)
data1 = data[0]
data2 = data1[['Symbol', 'Security']] #to take only few columns
df1 = pd.DataFrame(data2) #converting to a DataFrame
df2 = df1[df1['Security'] == 'Apple'] #filtering the table by company name i.e., Security provided by which company
data1.info() #info() - to see all available columns, data type, and memory usage

#Tesla's profile page: https://finance.yahoo.com/quote/TSLA/profile
tesla = pd.read_html('https://finance.yahoo.com/quote/TSLA/profile') #This code will cause an error because Yahoo checks the requester and requires a valid header.

#In order to fix the error, we need to specify the request header. For that, we will use the requests package and provide it with a valid header.

import pandas as pd
import requests

url = 'https://finance.yahoo.com/quote/TSLA/profile'
request = requests.get(url,headers =
                       {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'})

tesla_data = pd.read_html(request.text) #list with multiple DataFrames
print(tesla_data[0]) #A request header is used in an HTTP request to provide information about the request context, so that the server can tailor the response. We provided data for a standard web browser.

#Scraping the Earnings Estimates from the Analysis page:
import pandas as pd
import requests

url1 = 'https://finance.yahoo.com/quote/TSLA/analysis?p=TSLA'
request1 = requests.get(url1, headers =
                 {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'})

data1 = pd.read_html(request1.text)
print(data1[0]) #lists with multiple DataFrames

t_data = data1[0]
t_data = t_data[t_data['Earnings Estimate'] == 'Avg. Estimate']

import matplotlib.pyplot as plt

t_data.plot(kind='bar') #average estimated values from the table
plt.savefig('tesla_data_plot.png')

import yfinance as yf
#yfinance - to get financial data from Yahoo Finance
#Ticker - a module that allows to access company data based on their market ticker symbol

data = yf.Ticker("TSLA")
data.info #company information

data.info['profitMargins'] #column information - profitMargins
data.info['returnOnEquity'] #column information - return on equity (ROE)
data.info.keys() #for all of the available field names

data.dividends #shows dividends
data.splits #shows splits
data.balance_sheet #shows balance sheet
data.cashflow #shows cashflow
data.earnings #shows earnings

#plot bar chart for revenue - Amazon
import yfinance as yf
import matplotlib.pyplot as plt
data = yf.Ticker('AMZN')
x = data.earnings
x.plot(kind='bar')
plt.savefig('Amazon_revenue.png')

data1 = yf.Ticker('TSLA')
x = data1.earnings
x.plot(kind='bar')
plt.savefig('Tesla_revenue.png')

#access company data
#access data of company investors
import yfinance as yf
data = yf.Ticker('TSLA')
data.major_holders #Tesla's major holders
data.institutional_holders #Tesla's institutional holers
data.info

x = data.recommendations #recommendations - this field provides data on historic recommendations by investment banks
x = x[x.index > '2021-06-02'] #The index of the DatafRame is the date column
print(x)

#create a function that will take a ticker as its parameter, and output the ROE value for that ticker.
def ROE(ticker):
    data = yf.Ticker(ticker)
    roe = data.info['returnOnEquity']
    name = data.info['shortName']
    print(name, ':', roe)
    #to compare ROE of different companies

ROE('TSLA')
ROE('AMZN')
ROE('AAPL')
ROE('MSFT')


#access stock prices
import yfinance as yf
data = yf.Ticker('AAPL')

data.history() #stock prices for last month
data.history(period = '1mo') #valid periods: 1d, 5d, 1mo, 3mo, 6mo, 1y, 2y, 5y, 10y, ytd, max
data.history(start='2021-05-01', end='2021-07-28') #custom dates - start and end

#plotting the daily close price of Tesla stock for the last month
import yfinance as yf
import matplotlib.pyplot as plt
data = yf.Ticker("TSLA")
x = data.history()['Close']
x.plot()
plt.savefig('Tesla_stock_daily_close_price_for_the_last_month.png')

#for multiple stock
import yfinance as yf
import matplotlib.pyplot as plt

data = yf.download("AAPL MSFT TSLA", start='2021-07-01') #Ticker symbols seperated by spaces - download used instead of Ticker
#print(data['Close])
data['Close'].plot()

plt.savefig('Apple_Microsoft_Tesla_stock_prices.png')

data['Close']['AAPL'] #close price of only one selected ticker
data['Close']['AAPL'].plot()

data['Close'][['AAPL', 'TSLA']]
data['Close'][['AAPL', 'TSLA']].plot() #close price of selected tickers

data['Close'][['AAPL', 'TSLA']].max() #all time highest stock price of Apple and Tesla


