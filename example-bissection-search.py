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

#x = 25
#epsilon = 0.01
#numbGuesses = 0
#low = 1
#high = x
#ans = (low + high)/2
#
#while abs(ans**2 - x) >= epsilon:
#    print('low = ' + str(low) + ' high = ' + str(high) + ' ans = ' + str(ans))
#    numbGuesses +=1
#    if ans**2 < x:
#        low = ans
#    else:
#        high = ans
#    ans = (high + low)/2
#print('Number of guesses: ' + str(numbGuesses))
#print(str(ans) + ' is close to square root of ' + str(x))
        

def closest_power(base, num):
    '''
    base: base of the exponential, integer > 1
    num: number you want to be closest to, integer > 0
    Find the integer exponent such that base**exponent is closest to num.
    Note that the base**exponent may be either greater or smaller than num.
    In case of a tie, return the smaller value.
    Returns the exponent.
    '''
    # Your code here
    lowExp = 0
    highExp = 0
    
    while base**highExp < num:
        lowExp = highExp
        highExp += 1
    
    if abs(num - base**lowExp) <= abs(num - base**highExp):
        return lowExp
    else:
        return highExp
        
print(closest_power(5, 375.0))

        

