# -*- coding: utf-8 -*-
#graphics output 
"""
Created on Mon Feb 24 13:08:52 2014

@author: ragspiano
"""
import re
<<<<<<< HEAD
from pattern.en import*
=======


>>>>>>> 86c29be59674b0aa2672cf45e522038fb7f459fa

def most_common(hist, mcw):
    t = []
    for key, value in hist.items():
        if not(key in mcw):
            t.append((value, key))
    t.sort(reverse=True)
    return t
<<<<<<< HEAD


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

=======
    
if __name__ == "__main__":


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
    
    for x in allwords:
        if x in frequencies:
            frequencies[x] += 1
        else:
            frequencies[x] = 1
    #print frequencies
            
    common = most_common(frequencies, allmcw)
    #print common
    """
    for freq, word in common[0:10]:
        print word,'\t', freq
        """

def getAllWordsArray(filename):
    f = open(filename, "r")
    full_text = f.read()
    f.close()
    end_of_boilerplate = full_text.index("***")
    beginning_of_end = full_text.index("End of the Project Gutenberg")
    modText = full_text[end_of_boilerplate+4:beginning_of_end]
    modText = modText.lower()    
    allwords = re.findall("[\w\-\']+", modText)
    return allwords
>>>>>>> 86c29be59674b0aa2672cf45e522038fb7f459fa


