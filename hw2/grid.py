# -*- coding: utf-8 -*-
"""
Created on Sun Feb  2 17:14:11 2014

@author: Raagini Rameshwar
"""

def printGrid():

    for i in range (0,2):
        print '+----+----+'
        for k in range(0,3):
            print '|         |'
    print '+----+----+'

def printDoubleGrid():

    for j in range (0, 1):    
        for i in range (0,4):
            print '+----+----+----+----+----+----+----+----+'
            for k in range(0,5):
                print '|         |         |         |         |'
    print '+----+----+----+----+----+----+----+----+'

printGrid()
printDoubleGrid()