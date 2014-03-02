# -*- coding: utf-8 -*-
"""
Created on Sun Mar  2 10:26:34 2014

@author: ragspiano
"""

from pattern.en import *
import Image
import re

def openCleanFile(filename): 
    f = open(filename, "r")
    full_text = f.read()
    f.close()    
    
    end_of_boilerplate = full_text.index("***")
    beginning_of_end = full_text.index("End of the Project Gutenberg")
    modText = full_text[end_of_boilerplate+4:beginning_of_end]
    modText = modText.lower()
 
    return modText

"%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%"

    
def sentenceBreakup(text):
    
    sentenceList = []
    sentenceStart = 0    
    for i in range (len(text)-1):
        if text[i] == "." or text[i] == "!" or text[i] == "?":
            if (text[i-2:i] == "mr") or (text[i-3:i] == "mrs"):
                continue
            sentenceEnd = i
            sentence = text[sentenceStart:sentenceEnd+1].replace('\r\n',' ')
            sentenceList.append(sentence)
            sentenceStart = i+1
        
    return sentenceList
    
def pageBreakup(sentenceList):
    pageList = []
    sentencesPerPage = 20
    start = 0
    count = 0
    for i in range(len(sentenceList)):
        count +=1
        if count >= sentencesPerPage: 
            pageList.append(sentenceList[start:i])
            count = 0
            start = i
    return pageList
    
def sentimentAnalyser(page):
    summ=0
    for sentence in page: #Traverses the list of pages
        sentimentScore = sentiment(sentence)
        summ += sentimentScore[1]
    return summ/len(page)
    
def getWordsInPage(page):
    allwords = []
    for sentence in page:
        words = re.findall("[\w\-\']+",sentence)
        for x in words:
            allwords.append(x)
    return allwords
    
def removeExtraSentences(page,searchTerm):
    for sentence in page:
        if not(searchTerm in sentence):
            page.remove(sentence)
    return page
    
def buildSentimentChart(sentimentList):
    im = Image.new("RGB",(len(sentimentList)+1,100),color=(255,255,255))
    pixels = im.load()    
    for i in range(len(sentimentList)):
        red = int((1-sentimentList[i])*255)
        green = int(sentimentList[i]*255)
        for j in range(0, 100):
            pixels[i,j] = (red, green, 0)
    im.save("SentimentAnalysis.jpg","JPEG")

def frequencyAnalyser(page,searchTerm):
    num = 0
    wordsList = getWordsInPage(page)
    for word in wordsList:
        if word == searchTerm:
            num+=1
    return num
    
def getMaximumFrequency(s):
    max = 0
    for x in s:
       if x > max:
           max = x
    return max
    
def buildFrequencyChart(frequencyList,maxfreq):
    width=3
    n = len(frequencyList)*width
    q = maxfreq*width
    im = Image.new("RGB",(n,q))
    pixels = im.load() 
    currentPage = 0
    for x in range(0,n-1,width):
        if currentPage>=len(frequencyList):
            break
        freq = frequencyList[currentPage]
        currentPage +=1
        for y in range(freq):
            for a in range(x,x+width):
                for b in range(y,y+(2*width)):
                    pixels[a,q-b-1] = (255,255,255)
    im.save('frequency.jpg', 'JPEG')
    
def buildCombinationChart(frequencySentimentList,maxfreq):
    width=3
    n = len(frequencySentimentList)*width
    q = maxfreq*width
    im = Image.new("RGB",(n,q))
    pixels = im.load() 
    currentPage = 0
    for x in range(0,n-1,width):
        if currentPage>=len(frequencySentimentList)-1:
            break
        freq = frequencySentimentList[currentPage][0]
        currentPage +=1
        for y in range(freq):
            for a in range(x,x+width):
                for b in range(y,y+(2*width)):
                    red = int((1-frequencySentimentList[currentPage][1])*255)
                    green = int(frequencySentimentList[currentPage][1]*255)
                    pixels[a,q-b-1] = (red,green,0)
    im.save('combination.jpg', 'JPEG')

def getMaxOfTuple(tupleList):
    max = 0
    for x in tupleList:
       if x[0] > max:
           max = x[0]
    return max

def main():
    fullText = openCleanFile("SherlockH.txt")
    sentenceList = sentenceBreakup(fullText)
    pages = pageBreakup(sentenceList)
    searchTerm = "holmes"
    
    ##sentiment
    sentimentList = []
    for page in pages:
        sentimentList.append(sentimentAnalyser(page))
    buildSentimentChart(sentimentList)
    ##frequency
    frequencyList = []
    for page in pages:
        frequencyList.append(frequencyAnalyser(page,searchTerm))
    buildFrequencyChart(frequencyList,getMaximumFrequency(frequencyList))
    ##combination
    frequencySentimentList = []
    for page in pages:
        page = removeExtraSentences(page,searchTerm)
        frequencySentimentList.append((frequencyAnalyser(page,searchTerm),sentimentAnalyser(page)))
    buildCombinationChart(frequencySentimentList, getMaxOfTuple(frequencySentimentList))
            

if __name__ == "__main__":
    main()








    
