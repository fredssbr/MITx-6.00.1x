# -*- coding: utf-8 -*-
"""
Created on Tue Oct  4 16:28:27 2016

@author: frederico
"""

def applyF_filterG(L, f, g):
    """
    Assumes L is a list of integers
    Assume functions f and g are defined for you. 
    f takes in an integer, applies a function, returns another integer 
    g takes in an integer, applies a Boolean function, 
        returns either True or False
    Mutates L such that, for each element i originally in L, L contains  
        i if g(f(i)) returns True, and no other elements
    Returns the largest element in the mutated L or -1 if the list is empty
    """
    # Your code here
    L_clone = L[:]
    #Do not want to remove elements of a list you are iterating
    for i in L_clone:
        if not g(f(i)):
            L.remove(i)
    
    if len(L) == 0:
        return -1
    else:
        return max(L)

def f(i):
    return i + 2
def g(i):
    return i > 5

L = [0, -10, 5, 6, -4]
print(applyF_filterG(L, f, g))
print(L)