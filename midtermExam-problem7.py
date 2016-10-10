# -*- coding: utf-8 -*-
"""
Created on Tue Oct  4 16:11:00 2016

@author: frederico
"""
def f(a,b):
    return a > b

def dict_interdiff(d1, d2):
    '''
    d1, d2: dicts whose keys and values are integers
    Returns a tuple of dictionaries according to the instructions above
    '''
    # Your code here
    dictIntersect = {}
    dictDiff = {}    
    
    for i in d1:
        if i in d2:
            dictIntersect[i] = f(d1[i],d2[i])
        else:
            dictDiff[i] = d1[i]
    
    for i in d2:
        if i not in d1:
            dictDiff[i] = d2[i]
    
    
    return (dictIntersect,dictDiff)


#d1 = {1:30, 2:20, 3:30, 5:80}
#d2 = {1:40, 2:50, 3:60, 4:70, 6:90}
d1 = {1:30, 2:20, 3:30}
d2 = {1:40, 2:50, 3:60}
print(dict_interdiff(d1,d2))