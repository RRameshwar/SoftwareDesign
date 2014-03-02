# -*- coding: utf-8 -*-
"""
Created on Thu Feb 27 08:14:24 2014

@author: ragspiano
"""

import re
from pattern.en import*
import Image

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


def most_common(hist, mcw):
    t = []
    for key, value in hist.items():
        if not(key in mcw):
            t.append((value, key))
    t.sort(reverse=True)
    return t
    
def SentenceBreakup(text):
    SentenceList = []
    sentenceStart = 0    
    for i in range (len(text)-1):
        if text[i] == "." or text[i] == "!" or text[i] == "?":
            sentenceEnd = i
            sentence = text[sentenceStart:sentenceEnd+1]
            SentenceList.append(sentence)
            sentenceStart = i+1
    return SentenceList

def PageBreakup(SentenceList):
    PageList = []
    wordsPerPage = 250
    words = 0
    start = 0
    count = 0
    for i in range(len(SentenceList)):
        for k in SentenceList[i]:
            if k == " ":
                count += 1
            words += count
            count = 0
        if words >= wordsPerPage: 
            PageList.append(SentenceList[start:i])
            words = 0
            start = i
    return PageList

def Sentiment(PageList):
    SentimentList = []
    metalist = []
    for i in range(len(PageList)): #Traverses the list of pages
        sum = 0
        for j in range(len(PageList[i])): #Traverses the sentences per page
            #print PageList[i][j]
            sent = (sentiment(PageList[i][j]))
            metalist.append(sent[1])
            #print sentiment(PageList[i][j])
            for k in range(len(metalist)):
                sum += metalist[k]
            SentimentList.append(sum/len(metalist))
    return SentimentList

def scaling(SentimentList):
    max = 0
    for i in SentimentList:
        if i > max:
            max = i
    for j in range(len(SentimentList)):
        SentimentList[j] = SentimentList[j]/max  #Gives values between 0 and 1
    return SentimentList
    
def graphics(SentimentList):
    im = Image.new("RGB",(len(SentimentList)+1,300),color=(255,255,255))
    pixels = im.load()
    print len(SentimentList)
    
    for i in range(len(SentimentList)):
        red = int((1-SentimentList[i])*255)
        green = int(SentimentList[i]*255)
        for j in range(0, 300):
            pixels[i,j] = (red, green, 0)
    
    im.save("SentimentAnalysis.jpg","JPEG")

def main():
    f = open("SherlockH.txt", "r")
    full_text = f.read()
    f.close()
    SentenceList = []
    
    beginning_of_text = full_text.index("To Sherlock Holmes")
    beginning_of_end = full_text.index("End of the Project Gutenberg")
    modText = full_text[beginning_of_text:beginning_of_end]
    modText = modText.rstrip()
    
   
    SentenceList = SentenceBreakup(modText)
    
    PageList = PageBreakup(SentenceList)
    
    SentimentList = Sentiment(PageList)
        
    SentimentList = scaling(SentimentList)
    
    graphics(SentimentList)   

if __name__ == '__main__':
    main()


    