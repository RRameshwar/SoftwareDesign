# -*- coding: utf-8 -*-
"""
Created on Sun Mar  2 10:26:34 2014

@author: ragspiano
"""

from pattern.en import *
import Image
import re

def openCleanFile(filename):
    """Opens a file by the name of 'filename' and takes out boilerplate text from the beginning 
    and ending of the file. Also makes the entire document lowercase for ease of searching"""
    
    f = open(filename, "r")
    full_text = f.read()
    f.close()    
    
    end_of_boilerplate = full_text.index("***")
    beginning_of_end = full_text.index("End of the Project Gutenberg")
    modText = full_text[end_of_boilerplate+4:beginning_of_end]
    modText = modText.lower()
 
    return modText
    
def sentenceBreakup(text):
    """Takes a block of text and searches for the ends of sentences by looking for periods,
    question marks, and exclamation points. Also accounts for Mr. and Mrs. Returns a 
    list of all the sentences."""
    
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
    """Takes a list of sentences and breaks them up into pages. Returns a nested list of pages
    that have 20 sentences each"""
    
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
    """Takes a page, which is a list of sentences, and calculates the sentiments of all the sentences.
    Returns the average sentiment of the page."""
    
    summ=0
    for sentence in page: #Traverses the list of pages
        sentimentScore = sentiment(sentence)
        summ += sentimentScore[1]
    return summ/len(page)
    
def getWordsInPage(page):
    """Takes a page, which is a list of sentences, and seperates the sentences into words in order
    to search for frequencies. Returns the words in a list."""
    
    allwords = []
    for sentence in page:
        words = re.findall("[\w\-\']+",sentence)
        for x in words:
            allwords.append(x)
    return allwords
    
def removeExtraSentences(page,searchTerm):
    """Takes a page and a word to search for. For each sentence in the page, it deletes the sentence if it does
    not contain the search term. Otherwise it is kept. Returns a list of sentences on that page that contain the given word."""
    
    for sentence in page:
        if not(searchTerm in sentence):
            page.remove(sentence)
    return page
    
def buildSentimentChart(sentimentList):
    """Takes in a list of sentiments and creates a chart. The chart contains bars that are varying shades of
    green to red depending on how positive or negative the corresponding sentiment is. Saves an image."""
    
    im = Image.new("RGB",(len(sentimentList)+1,100),color=(255,255,255))
    pixels = im.load()    
    for i in range(len(sentimentList)):
        red = int((1-sentimentList[i])*255)
        green = int(sentimentList[i]*255)
        for j in range(0, 100):
            pixels[i,j] = (red, green, 0)
    im.save("SentimentAnalysis.jpg","JPEG")

def frequencyAnalyser(page,searchTerm):
    """Takes a page, which is a list of sentences, and a word to search for. Returns the number of times
    the word occurs on that page."""
    
    num = 0
    wordsList = getWordsInPage(page)
    for word in wordsList:
        if word == searchTerm:
            num+=1
    return num
    
def getMaximumFrequency(s):
    """Takes a list of frequencies of word occurence. Returns the maximum value in the list."""
    
    max = 0
    for x in s:
       if x > max:
           max = x
    return max
    
def buildFrequencyChart(frequencyList,maxfreq):
    """Takes a list of frequencies and a maximum value and builds a bar graph showing frequency per page.
    The higher the corresponding frequency, the taller the bar. Saves an image. The width variable defines 
    how many pixels wide each bar is"""
    
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
    """Takes a list of tuples, with each tuple containing a frequency and a sentiment Score, as well as a 
    maximum frequency. Builds a bar graph in which the height of the bar indicates frequency of the word on
    the page, and the color indicates sentiment."""
    
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
    """Takes a list of tuples. Returns the maximum value of the first tuple value, which corresponds
    to frequency."""
    
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








    
