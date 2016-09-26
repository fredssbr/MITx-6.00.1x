# -*- coding: utf-8 -*-
"""
Created on Mon Sep 26 07:13:10 2016

@author: frederico
"""

def mult(a,b):
    """
    Multiplies a*b using recursion
    a: int or float number
    b: int or float number
    """
    if b==1:
        return a
    else:
        return a + mult(a, b -1)

print("Result of the multiplication: ", str(mult(12,12)))

def fact(n):
    if n == 1:
        return 1
    else:
        return n*fact(n-1)

def fact_it(n):
    prod = 1
    for i in range(1,n+1):
        prod *= i
    return prod

print("Factorial of 5 (recursively): ", str(fact(5)))
print("Factorial of 5 (iteratively): ", str(fact_it(5)))