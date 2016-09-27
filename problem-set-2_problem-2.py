# -*- coding: utf-8 -*-
"""
Created on Tue Sep 27 08:59:28 2016

@author: frederico
"""

balance = 3926
annualInterestRate = 0.2

monthlyInterestRate = annualInterestRate / 12
updatedBalance = balance
minimumFixedMonthlyPayment = 0
while updatedBalance > 0:
    minimumFixedMonthlyPayment += 10
    updatedBalance = balance
    for i in range(1,13):    
        monthlyUnpaidBalance = updatedBalance - minimumFixedMonthlyPayment    
        updatedBalance = monthlyUnpaidBalance + monthlyInterestRate * monthlyUnpaidBalance
        #print("Payment:", str(minimumFixedMonthlyPayment),"Month:",str(i),"Balance:",str(updatedBalance))
print("Lowest payment:",str(round(minimumFixedMonthlyPayment,2)))