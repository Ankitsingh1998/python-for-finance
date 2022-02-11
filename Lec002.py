#Lecture 2 - Basic calculations
import numpy_financial as npf
print(npf.fv(rate=0.05, nper=3, pmt=0, pv=-100)) #fv - final value
print(npf.pv(rate=0.03, nper=4, pmt=0, fv=-100)) #pv - previous value

#pmt - monthly loan payments (to calculate mortgage payments)
#monthly
print(npf.pmt(rate=0.05/12, nper=4*12, pv=100, fv=0)) #loan payment
print(npf.pmt(rate=0.07/12, nper=2*12, pv=0, fv=5000)) #deposit to get an interest

#anually/yearly
print(npf.pmt(rate=0.05, nper=4, pv=100, fv=0))
print(npf.pmt(rate=0.07, nper=2, pv=0, fv=5000))


#IRR(Internal Rate of Return)
cashflow = [-5000, 500, 700, 1000, 3000] #first value with initial investment, after that put paymenst that we are getting back
print(npf.irr(cashflow))

cashflow1 = [-10000, 2000, 3000, 5000, 2500]
cashflow2 = [-10000, 2500, 3000, 4500, 3500]
print('cashflow1:',npf.irr(cashflow1))
print('cashflow2:',npf.irr(cashflow2))
rate_year = ['investment', 'year1', 'year2', 'year3', 'year4']

import matplotlib.pyplot as plt
plt.plot(rate_year, cashflow1)
plt.plot(rate_year, cashflow2)
plt.savefig('irr_example')
