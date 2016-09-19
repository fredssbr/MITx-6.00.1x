# -*- coding: utf-8 -*-
"""
Created on Mon Sep 19 07:07:37 2016

@author: frederico

BISSECTION SEARCH

    Square root of x lies between 1 and X
    Pick a number g in  the middle of this
    If g**2 > x, then work with the first half (pick a number in the middle), discard the second
    If g**2 < x, then work with the second half (pick a number in the middle), discard the first
    
Each stage(iteration), reduce the range of values to search by half
"""

x = 25
epsilon = 0.01
numbGuesses = 0
low = 1
high = x
ans = (low + high)/2

while abs(ans**2 - x) >= epsilon:
    print('low = ' + str(low) + ' high = ' + str(high) + ' ans = ' + str(ans))
    numbGuesses +=1
    if ans**2 < x:
        low = ans
    else:
        high = ans
    ans = (high + low)/2
print('Number of guesses: ' + str(numbGuesses))
print(str(ans) + ' is close to square root of ' + str(x))
        


