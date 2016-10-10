# -*- coding: utf-8 -*-
"""
Created on Tue Oct  4 17:05:19 2016

@author: frederico
"""

#def flatten(aList):
#    ''' 
#    aList: a list 
#    Returns a copy of aList, which is a flattened version of aList
#    '''
#    #use recursion
#    flatList = []
#    for i in aList:
#        if type(i) is list:
#            return flatList.append(flatten(i))
#        else:            
#            return flatList.append(i)
#    return flatList

def flatten(aList):
    ''' 
    aList: a list 
    Returns a copy of aList, which is a flattened version of aList
    '''
    if aList == []:
        return aList
    if type(aList[0]) is list:
        return flatten(aList[0]) + flatten(aList[1:])
    return aList[:1] + flatten(aList[1:])

aList = [[1,'a',['cat'],2],[[[3]],'dog'],4,5]
print(flatten(aList))
#Expected [1,'a','cat',2,3,'dog',4,5]

#Recursion is extremely useful for this question. 
#You will have to try to flatten every element of the original list. 
#To check whether an element can be flattened, the element must be another 
#object of type list.



#    listFlattened = []
#    if type(aList[0]) == 'list':
#        return listFlattened.append(flatten(aList[0]))
#    else:
#        return listFlattened.append(aList[0])