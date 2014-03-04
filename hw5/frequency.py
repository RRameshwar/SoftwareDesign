# -*- coding: utf-8 -*-
"""
Created on Thu Feb 27 11:13:48 2014

@author: anneubuntu
"""

# -*- coding: utf-8 -*-
#graphics output 
"""
Created on Mon Feb 24 13:08:52 2014

@author: ragspiano
"""
import re
from SherlockAnalysis import getAllWordsArray
import Image
import math
import SentimentAnalysis

def findNumber(a,searchTerm):
    num = 0
    for x in a:
        if x==searchTerm:
            num+=1
    return num
    
def getMaximumFrequency(d):
    max = 0
    for x in d:
       if d[x] > max:
            max = d[x]
    return max
    
def drawImage(pages,maxfreq):
    width=3
    n = len(pages)*width
    q = maxfreq*width
    im = Image.new("RGB",(n,q))
    pixels = im.load() 
    currentPage = 0
    for x in range(0,n-1,width):
        if currentPage>=len(pages):
            break
        freq = pages[currentPage]
        currentPage +=1
        for y in range(freq):
            for a in range(x,x+width):
                for b in range(y,y+(2*width)):
                    pixels[a,q-b-1] = (125,125,0)
    im.save('holmesFrequency.jpg', 'JPEG')


def makePageFrequencyDict(allwords,searchTerm):
    numpages = int(math.ceil(len(allwords)/250.0))
    pages = {}
    for i in range(numpages):
        if i+250<len(allwords):
            page = tuple(allwords[(i*250):(i*250)+250])
            pages[i] = findNumber(page, searchTerm)
        else:
            page = tuple(allwords[(i*250):len(allwords)])
            pages[i] = findNumber(page, searchTerm)
    return pages
    
def getSentenceOfWord(page,searchTerm,count):
    sentenceListPage = SentimentAnalysis.SentenceBreakup(page)
    c=0
    for x in sentenceListPage:
        if searchTerm in x:
            c+=1
            if c==count:
                return x
    return None #this should never run
                
    
    
def pageSentiment(page,searchTerm):
    pageAllWords = getAllWordsArray(page)
    sentimentsForPage = []
    countForPage = 0
    for x in pageAllWords:
        if x==searchTerm:
            countForPage+=1
            sentence = getSentenceOfWord(page,searchTerm,countForPage)
            sentimentsForPage.append(sentiment(sentence)[1])
    averagePageSentiment = sum(sentimentsForPage)/float(len(sentimentsForPage))
    return averagePageSentiment
    
def makePageArray(fulltext):
    pages = []
    wordCount=1
    for k in fulltext:
        if k==" ":
            wordCount+=1
    numpages = int(math.ceil(wordCount/250.0)
    for 

#makePageArray("hi my name is anne and I like warm hugs")
    


def makePageSentimentDict(fulltext,searchTerm):
 #####  pages = makePageArray(fulltext)
    pageSentimentDict = {}
    for i in range(pages):
        pageSentimentDict[i] = pageSentiment(pages[i],searchTerm)
    return pageSentimentDict

def drawSentimentImage(pageSentimentDict,pagesDict,maxfreq):

    pageSentimentDict = SentimentAnalysis.scaling(pageSentimentDict)    
    
    width=3
    n = len(pagesDict)*width
    q = maxfreq*width
    im = Image.new("RGB",(n,q))
    pixels = im.load() 
    currentPage = 0
    for x in range(0,n-1,width):
        if currentPage>=len(pagesDict):
            break
        freq = pagesDict[currentPage]
        currentPage +=1
        for y in range(freq):
            for a in range(x,x+width):
                for b in range(y,y+(2*width)):
                    red = int((1-pageSentimentDict[x])*255)
                    green = int(pageSentimentDict[x]*255)
                    pixels[a,q-b-1] = (red,green,0)
    im.save('sentimentFrequency.jpg', 'JPEG')
         
"""
if __name__ == "__main__":
    searchTerm = "the"
    f = "SherlockH.txt"
    
    allwords = getAllWordsArray(f)
    pagesDict = makePageFrequencyDict(allwords,searchTerm)

    drawImage(pagesDict,getMaximumFrequency(pagesDict))
    

    
"""
    
def pageWords(page):
    """
    Takes a list that represents a page, with nested lists, one for each
    sentence.  Returns a list of strings, an array of words
    """
    allwords = []
    for sentence in page:
        words = re.findall("[\w\-\']+", sentence)
        for x in words:
            allwords.append(x)
    return allwords
    
def searchSentences(page,searchTerm):
    for sentence in page:
        if not(searchTerm in sentence):
            page.remove(sentence)
    return page