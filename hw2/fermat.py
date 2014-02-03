# -*- coding: utf-8 -*-
"""
Created on Sun Feb  2 17:37:56 2014

@author: Raagini Rameshwar
"""

def check_fermat(a, b, c, n):
    if (n>2):
        if (a**n + b**n == c**n):
            print 'Holy Smokes, Fermat Was Right!!'
        else:
            print 'Yeah that wasn\'t exciting'
    else:
        print 'No that doesn\'t work!'


def check_fermat_input():
    input1 = raw_input('Enter a value for a: ')
    a = int(input1)
    
    input2 = raw_input('Enter a value for b: ')
    b = int(input2)
    
    input3 = raw_input('Enter a value for c: ')
    c = int(input3)
    
    input4 = raw_input('Enter a value for n: ')
    n = int(input4)    
    
    if (n>2):
        if (a**n + b**n == c**n):
            print 'Holy Smokes, Fermat Was Right!!'
        else:
            print 'Yeah that wasn\'t exciting'
    else:
        print 'No that doesn\'t work!'


check_fermat_input()


