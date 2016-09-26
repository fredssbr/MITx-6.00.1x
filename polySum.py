# -*- coding: utf-8 -*-
"""
Created on Mon Sep 26 20:18:03 2016

@author: frederico.x.silva
"""
import math
def polysum(n,s):
    """
    n: number of sides of the polygon
    s: length of each side
    returns: the sum of the area with the square perimeter
    """
    area = (0.25*n*(s**2))/math.tan(math.pi/n)
    perimeter = n*s
    return round(area + perimeter**2,4)

print(polysum(5,5))
    
