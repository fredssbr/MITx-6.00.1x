# -*- coding: utf-8 -*-
"""
Created on Sun Sep 11 12:56:18 2016

@author: frederico

Problem Set 1 - Problem 3

Assume s is a string of lower case characters.

Write a program that prints the longest substring of s in which the letters occur in alphabetical order. 
For example, if s = 'azcbobobegghakl', then your program should print

Longest substring in alphabetical order is: beggh

In the case of ties, print the first substring. For example, if s = 'abcbcd', then your program should print

Longest substring in alphabetical order is: abc
"""

s = 'azcbobobegghakl'
s = 'wrhgtfwpw' #should output gt
s = 'yooqomjvefxmqoutkjqelsb' #should output ooq
s = 'abcbcd' #should output abc
s = 'dpnpxoxxrikgiho' #should output npx
s = 'ewdppgsnzikyjurge' #should output dpp
s = 'olcrowrm' #should output cr
s = 'mcivjrqd' #should output civ
s = 'gvvhxvbgq' #should output gvv
s = 'abcdefghijklmnopqrstuvwxyz' #should output abcdefghijklmnopqrstuvwxyz
s = 'fnfnkcjfvkvihthvbctepe' #should output bct
s = 'xkbynnyjw' #should output nny
s = 'upmcjxwekpyxuxuydfav' #should output ekpy
s = 'zyxwvutsrqponmlkjihgfedcba' #should output z
s = 'zhhrjhxnyfgncr' #should output hhr 
s = 'ctkhrpqvzyow' #should output pqvz
s = 'krknzphmey' #should output knz
s = 'lexonyqcaztumk' #should output ex
s = 'jwavuipcimdlns' #should output dlns
s = 'irlwmdtzwbjrm' #should output dtz
s = 'qcfwmgeytrnekr' #should output cfw
s = 'pxygdwhk' #should output pxy


longest_sub = ''
possible_longest_sub = ''

for i in range(len(s) - 1):
    if len(possible_longest_sub) == 0:
        possible_longest_sub = s[i]
        
    if possible_longest_sub[len(possible_longest_sub)-1] <= s[i + 1]:
        possible_longest_sub += s[i + 1]
    else:        
        possible_longest_sub = ''
        
    if len(possible_longest_sub) > len(longest_sub):
            longest_sub = possible_longest_sub

#if both are empty, it means the subsequent letter came before, remaining true throughout the whole string
#so  that the first letter (occurrency) should be printed
if len(longest_sub) == 0:
    longest_sub = s[0]
print('Longest substring in alphabetical order is: ', longest_sub)
    