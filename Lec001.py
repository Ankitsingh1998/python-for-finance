#Lecture 1 - python for finance
#python's use in finance to solve different problems and to perform financial analysis.

#ROE - Return on Equity

#Why python?? - It's easy to learn and syntax is simple. Also, python has many packages that is useful when working with financial data.

print(126*458)

'''
Projects to be covered:
    -calculate basic financial metrics
    -plot charts based on financial data
    -retrieve and analyze stock prices
    -perform financial analysis of stocks and portfolios, included stock returns, correlations, risk analysis
    -optimise a portfolio using the Monte Carlo Simulation
    
    e.g. to analyse the price of bitcoin(a decentralized digital currency)
'''

#python operations:
print('This is a course in python for finance!')
print(1 + 3)
print(5 - 8)
print(5 * 2)
print(10 / 2) #will gives result as a float
print(10 // 3)
print(10 % 3)

currency = 'Bitcoin'
price = 412.80
print(currency+': Rs'+str(price))

print(346*(89**78))
print(346*(89^78))

x = 12
y = 9
print(x*y)
print(x+y)
print(x-y)
print(x/y)
print(x//y)
print(x%y)

#python packages
a = max(2,1,0,9)
b = min(1,0,2,5)
print(a,'\n',b) #\n - newline, \t - tab

import math as m #as is a keyword to shorten or change our package/module's name
print(m.factorial(6))
print(int(m.sqrt(625)))

#annual rteurn rate
import numpy_financial as npf
year5 = npf.fv(rate=0.08, nper=5, pmt=0, pv=-1000)
print(year5)
"""
fv - future value
rate - interest rate in decimals
nper - number of periods
pmt - periodic payments/investments
pv = present value
"""

#Numpy
#numpy_financial is based on numpy
#Array - It allows to store multiple values in a single variable.
#numpy arrays - allows one to easily and efficiently perform calculations.
import numpy as np
prices = [42.8, 102.03, 240.38, 80.9]
print(np.mean(prices)) #mean - average of all elements/numbers
print(np.std(prices)) #std - standard deviation of all elements/numbers
print(np.sum(prices)) #sum - sum of all elements/numbers
print(np.max(prices)) #max - maximum of all elements/numbers

