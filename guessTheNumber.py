# -*- coding: utf-8 -*-
"""
Created on Mon Sep 19 07:27:24 2016

@author: frederico
"""

low = 0
high = 100
ans = int((low + high)/2)
charInput = 'h'
high
print('Please think of a number between 0 and 100!')

while charInput != 'c':
    
    charInput = input("Is your secret number " + str(ans) + "?\n"
                        "Enter 'h' to indicate the guess is too high. "
                        "Enter 'l' to indicate the guess is too low. "
                        "Enter 'c' to indicate I guessed correctly. ")
    if charInput == 'h':
        high = ans
    elif charInput == 'l':
        low = ans
    elif charInput == 'c':
        print('Game over. Your secret number was: ' + str(ans))
        break
    else:
        print('Sorry, I did not understand your input.')
    ans = int((low + high)/2)