# -*- coding: utf-8 -*-
"""
Created on Sun Feb  2 21:05:58 2014

@author: Raagini Rameshwar
"""

def compare(x, y):
    if x>y:
        return 1
    elif x == y:
        return 0
    else:
        return -1
        
        

print compare(5, 5)
print compare(6, 5)
print compare(4, 5)