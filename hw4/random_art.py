# -*- coding: utf-8 -*-
"""
Created on Tue Feb 11 11:34:57 2014

@author: pruvolo
"""

# you do not have to use these particular modules, but they may help
#if max depth equals 1, then return x or y
#if min depth equals 1 check your max depth
#if it's not, return things that aren't x or y 
from random import randint
import math
import pprint
import Image

def build_random_function(min_depth, max_depth):
    """creates a deeply nested function using some basic building block functions. THe number of
    nests is between min_depth and man_depth"""

    basicFunctions = ['prod', 'cos_pi', 'sin_pi', 'x', 'y']
    
    
    if max_depth == 1:
        n = randint(0,2)
        if n == 0:
            return 'x'
        else:
            return 'y'
            
    if min_depth <= 1:#allowed to return x or y but are not forced to
        n = randint(0,4)
        if n == 3:
            return 'x'
        if n == 4:
            return 'y'
        if n == 0:
            return [basicFunctions[n], build_random_function(min_depth, max_depth-1), build_random_function(min_depth, max_depth-1)]
        else:
            return [basicFunctions[n], build_random_function(min_depth, max_depth-1)]
    else:
        n = randint(0,3)
        if n == 0:
            return [basicFunctions[n], build_random_function(min_depth-1, max_depth-1), build_random_function(min_depth-1, max_depth-1)]
            #print "n = 0, 3, 4", myList
        else:
            return [basicFunctions[n], build_random_function(min_depth-1, max_depth-1)]
            #print "n = 1, 2", myList
            
#print "build_random_function ", build_random_function(2, 5)        
       
        
def evaluate_random_function(f, x, y):
    '''evaluates the value of a randomly built function given the function f and an x and y value for which to evaluate f'''
    function = f[0];
    if function == 'x':
        return x
    if function == 'y':
        return y
    if function == 'prod':
        #pprint.pprint(f[1])
        #pprint.pprint(f[2])
        return evaluate_random_function(f[1], x, y) * evaluate_random_function(f[2], x, y)        
    if function == 'cos_pi':
        return math.cos(math.pi*evaluate_random_function(f[1], x, y))
    if function == 'sin_pi':
        return math.sin(math.pi*evaluate_random_function(f[1], x, y))

func = build_random_function(2, 5)
print evaluate_random_function(func, -0.2, 0.5)

def remap_interval(val, input_interval_start, input_interval_end, output_interval_start, output_interval_end):
    """ Maps the input value that is in the interval [input_interval_start, input_interval_end]
        to the output interval [output_interval_start, output_interval_end].  The mapping
        is an affine one (i.e. output = input*c + b).
    
        TODO: please fill out the rest of this docstring
    """
        
    val2 = val-input_interval_start
    val3 = val2*(output_interval_end-output_interval_start)/float(input_interval_end-input_interval_start)
    val4 = val3 + output_interval_start
    return val4

print remap_interval(200, 0, 349, -1, 1)                                           

def main():

    red = build_random_function(4, 7)
    #print red
    blue = build_random_function(3, 10)
    #print blue
    green = build_random_function(3, 15)
    #print green
   
    im = Image.new("RGB",(350,350))

    pixels = im.load()
   
   
    for i in range(0,349):
        for j in range(0, 349):
            scaledvali = remap_interval(i, 0, 349, -1, 1)
            print scaledvali
            scaledvalj = remap_interval(j, 0, 349, -1, 1)
            print scaledvalj
            
            valred = evaluate_random_function(red, scaledvali, scaledvalj)
            print valred
            valblue = evaluate_random_function(blue, scaledvali, scaledvalj)
            print valblue
            valgreen = evaluate_random_function(green, scaledvali, scaledvalj)
            print valgreen
           
            plotred = int(remap_interval(valred, -1, 1, 0, 255)) #convert to int
            plotgreen = int(remap_interval(valgreen, -1, 1, 0, 255))
            plotblue = int(remap_interval(valblue, -1, 1, 0, 255))
           
            pixels[i,j] = (plotred, plotgreen, plotblue)
   
      
    im.save("Picture1.jpg","JPEG")
    
    
if __name__ == '__main__':
    main()
    
    
    
    
    
    
    
    