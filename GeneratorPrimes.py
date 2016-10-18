# -*- coding: utf-8 -*-
"""
Created on Mon Oct 17 20:13:54 2016

@author: frederico
"""

def genPrimes():
    primeList = []
    x = 1
    while True:
        flagPrime = True
        x += 1
        for p in primeList:
            if (x % p) == 0:
                flagPrime = False
                break
        if flagPrime:
            primeList.append(x)
            yield x            
