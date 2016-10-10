# -*- coding: utf-8 -*-
"""
Created on Tue Oct  4 15:51:36 2016

@author: frederico
"""
def deep_reverse(L):
    """ assumes L is a list of lists whose elements are ints
    Mutates L such that it reverses its elements and also 
    reverses the order of the int elements in every element of L. 
    It does not return anything.
    """    
    # Your code here
    for i in L:
        i.reverse()
    L.reverse()    

L = [[1, 2], [3, 4], [5, 6, 7]]
deep_reverse(L)
print(L)
