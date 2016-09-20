# -*- coding: utf-8 -*-
"""
Created on Mon Sep 19 07:07:37 2016

@author: frederico

Steps to convert an integer (x) to binary

    1 - Take the remainder x%2, that will give the last binary bit.
    2 - Divide x//2 - all bits get shifted right
    3 - Repeat that until x = 0
    
"""

num = 19

#Gets the absolute value of the number
if num < 0:
    isNeg = True
    num = abs(num)
else:
    isNeg = False
    
result = ''

#No need to apply those steps if number is 0
if num == 0:
    result = '0'
    
while num > 0:
    #1 - Take the remainder x%2, that will give the last binary bit.
    result = str(num%2) + result
    #2 - Divide x//2 (integerwise) - all bits get shifted right
    num = num//2
    print("remainder = ", str(num%2), "num = ", str(num))
#Just adds a negative sign if the number < 0
if isNeg:
    result = '-' + result

print("Representation of ", str(num), " in binary is ", result)