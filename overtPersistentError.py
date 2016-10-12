# -*- coding: utf-8 -*-
"""
Created on Tue Oct 11 21:06:03 2016

@author: frederico
"""

def integerDivision(x, a):
    """
    x: a non-negative integer argument
    a: a positive integer argument

    returns: integer, the integer division of x divided by a.
    """
#   If you remove this line, you might get a OVERT and PERSISTENT error
    
#    File "/home/frederico/Courses/MITx: 6.00.1x/src/overtPersistentError.py", line 19, in integerDivision
#    count += 1
#    UnboundLocalError: local variable 'count' referenced before assignment
    count = 0
    
    while x >= a:
        count += 1
        x = x - a
    return count

print(integerDivision(5,3))