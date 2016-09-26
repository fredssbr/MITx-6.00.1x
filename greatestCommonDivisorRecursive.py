# -*- coding: utf-8 -*-
"""
Created on Mon Sep 26 08:38:36 2016

@author: frederico
"""

def gcdRecur(a, b):
    '''
    Euclid version
    
    a, b: positive integers
    
    returns: a positive integer, the greatest common divisor of a & b.
    '''
    # Your code here
    if b == 0:
        return a
    else:
        return gcdRecur(b, a%b)    

print(gcdRecur(12,17))
        