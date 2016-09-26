# -*- coding: utf-8 -*-
"""
Created on Mon Sep 26 07:52:39 2016

@author: frederico
"""

def iterPower(base, exp):
    '''
    base: int or float.
    exp: int >= 0
 
    returns: int or float, base^exp
    '''
    # Your code here
    prod = 1
    if exp == 0:
        return 1
    else:
        while exp > 0:
            prod *= base
            exp -= 1
    return prod

print(iterPower(2,4))