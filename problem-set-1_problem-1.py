# -*- coding: utf-8 -*-
"""
Created on Sun Sep 11 09:32:59 2016

@author: frederico

Problem Set 1 - Problem 1

Assume s is a string of lower case characters.

Write a program that counts up the number of vowels contained in the string s. 
Valid vowels are: 'a', 'e', 'i', 'o', and 'u'. For example, if s = 'azcbobobegghakl', your program should print:

Number of vowels: 5
"""
s = 'throughout the year'
vowels = 0
for letter in s:
    if letter == 'a' or letter == 'e' or letter == 'i' or letter == 'o' or letter == 'u':
        vowels += 1
print('Number of vowels: ', str(vowels))

