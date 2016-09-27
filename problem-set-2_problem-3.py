# -*- coding: utf-8 -*-
"""
Created on Tue Sep 27 13:40:48 2016

@author: frederico.x.silva
"""

balance = 999999
annualInterestRate = 0.18

monthlyInterestRate = annualInterestRate / 12
updatedBalance = balance
monthlyPayment = 0
increment = 0.01
#count = 0
lowerBound = balance / 12
upperBound = (balance * (1 + monthlyInterestRate) ** 12) / 12

while abs(updatedBalance) >= increment:
    monthlyPayment = (upperBound + lowerBound) / 2
    updatedBalance = balance
    for i in range(1,13):    
        monthlyUnpaidBalance = updatedBalance - monthlyPayment    
        updatedBalance = monthlyUnpaidBalance + monthlyInterestRate * monthlyUnpaidBalance
        #print("Payment:", str(minimumFixedMonthlyPayment),"Month:",str(i),"Balance:",str(updatedBalance))
        #count += 1
    if updatedBalance > 0:
        lowerBound = monthlyPayment
    else:
        upperBound = monthlyPayment       

print("Lowest payment:",str(round(monthlyPayment,2)))
#print("Iterations:", str(count))