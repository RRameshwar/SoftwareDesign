# -*- coding: utf-8 -*-
#graphics output 
"""
Created on Mon Feb 24 13:08:52 2014

@author: ragspiano
"""
import re
from pattern.en import*

def most_common(hist, mcw):
    t = []
    for key, value in hist.items():
        if not(key in mcw):
            t.append((value, key))
    t.sort(reverse=True)
    return t


f = open("SherlockH.txt", "r")
full_text = f.read()
f.close()

f = open("MostCommonWords.txt", "r")
mcw = f.read()
f.close()



end_of_boilerplate = full_text.index("***")
beginning_of_end = full_text.index("End of the Project Gutenberg")
modText = full_text[end_of_boilerplate+4:beginning_of_end]

#print allmcw
modText = modText.lower()
mcw = mcw.lower()
frequencies = {}

allwords = re.findall("[\w\-]+", modText)
allmcw = re.findall("[\w\-]+", mcw)

print allwords
for x in allwords:
    if x in frequencies:
        frequencies[x] += 1
    else:
        frequencies[x] = 1

        
common = most_common(frequencies, allmcw)

for freq, word in common[0:10]:
    print word,'\t', freq



