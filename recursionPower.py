# -*- coding: utf-8 -*-
"""
Created on Mon Sep 26 07:59:43 2016

@author: frederico
"""

def recurPower(base, exp):
    '''
    base: int or float.
    exp: int >= 0
 
    returns: int or float, base^exp
    '''
    # Your code here
    if exp <= 0:
        return 1
    else:
        return base * recurPower(base, exp - 1)

print(recurPower(12,2))