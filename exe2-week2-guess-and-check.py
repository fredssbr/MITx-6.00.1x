# -*- coding: utf-8 -*-
"""
Created on Tue Sep 13 09:22:11 2016

@author: frederico
"""

#Infinite loop
#x = 25
#epsilon = 0.01
#step = 0.1
#guess = 0.0
#
#while guess <= x:
#    if abs(guess**2 -x) >= epsilon:
#        guess += step
#
#if abs(guess**2 - x) >= epsilon:
#    print('failed')
#else:
#    print('succeeded: ' + str(guess))


#This is the number we want to find the root of
x = 29

#Epsilon is a measure of accuracy (how accurate I want the answer to be)
#the higher, the less accurate the answer will be
epsilon = 0.01

#Increasing steps (the less, the more accurate the answer but slower the execution
# due to more iterations)
step = 0.001

#Initial guess
guess = 0.0

#Counter for the iterations
count = 0

while abs(guess**2-x) >= epsilon and guess <= x:
    count += 1
    if guess <= x:
        guess += step
    else:
        break

if abs(guess**2 - x) >= epsilon:
    print('Failed to find the answer.')
else:
    print('Succeded: ', str(guess), '. Iterations: ', str(count))