# -*- coding: utf-8 -*-
"""
Created on Mon Sep 26 18:43:20 2016

@author: frederico.x.silva
"""

def isIn(char, aStr):
    '''
    char: a single character
    aStr: an alphabetized string
    
    returns: True if char is in aStr; False otherwise
    '''
    #print("String: ", aStr)
    lower = ""
    higher = ""
    middle = ""
    midPos = 0
    # Your code here
    if len(aStr) == 0:
        return False
    elif len(aStr) == 1:
        if char == aStr:
            return True
        else:
            return False
    else:
        midPos = len(aStr)%2
        lower = aStr[:midPos]
        middle = aStr[midPos]
        higher = aStr[midPos+1:]
        if char < middle:
            return isIn(char, lower)
        elif char > middle:
            return isIn(char, higher)
        else:
            return True #char is equal middle

print(isIn("x", "abcdefghi"))
            
        
        