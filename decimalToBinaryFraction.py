# -*- coding: utf-8 -*-
"""
Created on Tue Sep 20 08:59:44 2016

@author: frederico

Steps to convert a decimal(x) to binary:

    1 - So if we multiply X by a power of 2 big enough to convert it into a 
    whole number, then we can apply the same technique as in decimal to binary
    
        1 - Take the remainder x%2, that will give the last binary bit.
        2 - Divide x//2 - all bits get shifted right
        3 - Repeat that until x = 0
    
"""

x = float(input('Enter a decimal number between 0 and 1: '))

p = 0

#Iterate to find the power that gives a whole number to te multiplication
while ((2**p)*x)%1 != 0: 
    print('Remainder = ' + str((2**p)*x - int((2**p)*x)))
    print('Another way to get the remainder = ', str(((2**p)*x)%1))
    p += 1

print('Power achieved to get a whole number: ', str(p))

num = int(x*(2**p))

print('Check the number is whole: ', str(num))

result = ''

if num == 0:
    result = '0'
while num > 0:
    result = str(num%2) + result
    num = num//2

print('Result line 1: ', result)
#Fill in with 0s to the left up to p
for i in range(p - len(result)):
    result = '0' + result
print('Result line 2: ', result)
#this line prints the first part (integer) + . + fraction part(decimal)
#only useful when you type in something larger than 1
result = result[0:-p] + '.' + result[-p:]
print('The binary representation of the decimal ' + str(x) + ' is ' + str(result))
