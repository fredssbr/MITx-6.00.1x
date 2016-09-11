# -*- coding: utf-8 -*-
"""
Created on Sun Sep 11 09:41:19 2016

@author: frederico

Problem Set 1 - Problem 2

Assume s is a string of lower case characters.

Write a program that prints the number of times the string 'bob' occurs in s. For example, if s = 'azcbobobegghakl', then your program should print

Number of times bob occurs is: 2
"""
s = 'ohbobobmagnabombob'
s = 'bobborbbobbp'

#Non-overlapping occurrencies
#print('Number of times bob occurs is: ', str(s.count('bob')))

#Overlapping occurrencies
initialPos = 0
count = 0
        
while len(s) > 0:
    initialPos = s.find('bob',initialPos, len(s))
    if initialPos >= 0:
        count += 1
        s = s[initialPos+1:]
        initialPos = 0
    else:
        break

print('Number of times bob occurs is: ', str(count))      
