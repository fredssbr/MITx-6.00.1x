# -*- coding: utf-8 -*-
"""
Created on Tue Oct  4 15:43:04 2016

@author: frederico
"""

def dotProduct(listA, listB):
    '''
    listA: a list of numbers
    listB: a list of numbers of the same length as listA
    '''
    # Your code here
    sumOfParwiseProducts = 0
    for i in range(len(listA)):
        sumOfParwiseProducts += listA[i]*listB[i]
    return sumOfParwiseProducts
    
listA = [1, 2, 3]
listB = [4, 5, 6]

print(dotProduct(listA, listB))