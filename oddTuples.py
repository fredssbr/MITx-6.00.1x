# -*- coding: utf-8 -*-
"""
Created on Thu Sep 29 09:01:29 2016

@author: frederico
"""

def oddTuples(aTup):
    '''
    aTup: a tuple
    
    returns: tuple, every other element of aTup. 
    '''
    # Your Code Here
    retTuple = ()    
    for i in range(0,len(aTup),2):
        retTuple = retTuple + (aTup[i],)
    return retTuple

print(oddTuples(("I")))