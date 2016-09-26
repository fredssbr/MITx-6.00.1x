# -*- coding: utf-8 -*-
"""
Created on Mon Sep 26 08:30:16 2016

@author: frederico
"""

def gcdIter(a, b):
    '''
    a, b: positive integers
    
    returns: a positive integer, the greatest common divisor of a & b.
    '''
    # Your code here
    smaller = 0
    if a >= b:
        smaller = b
    else:
        smaller = a
    gcd = 1
    while smaller >= 1:
        if (a%smaller == 0) and (b%smaller == 0):
            gcd = smaller
            break
        else:
            smaller -= 1
    return gcd
print(gcdIter(12,9))