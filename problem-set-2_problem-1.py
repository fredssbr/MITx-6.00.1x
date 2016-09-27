# -*- coding: utf-8 -*-
"""
Created on Tue Sep 27 07:48:49 2016

@author: frederico
"""

balance = 484
annualInterestRate = 0.2
monthlyPaymentRate = 0.04

monthlyInterestRate = annualInterestRate / 12

for i in range(1,13):
    minimumMonthlyPayment = monthlyPaymentRate * balance 
    monthlyUnpaidBalance = balance - minimumMonthlyPayment    
    balance = monthlyUnpaidBalance + monthlyInterestRate * monthlyUnpaidBalance
    #print("Month", i, "Remaining balance:", round(balance,2))
print("Remaining balance:",str(round(balance,2)))