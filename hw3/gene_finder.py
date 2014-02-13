# -*- coding: utf-8 -*-
"""
Created on Sun Feb  2 11:24:42 2014

@author: YOUR NAME HERE
"""

# you may find it useful to import these variables (although you are not required to use them)
from amino_acids import aa, codons

def collapse(L):
    """ Converts a list of strings to a string by concatenating all elements of the list """
    output = ""
    for s in L:
        output = output + s
    return output


def coding_strand_to_AA(dna):
    """ Computes the Protein encoded by a sequence of DNA.  This function
    does not check for start and stop codons (it assumes that the input
    DNA sequence represents an protein coding region).
    
    dna: a DNA sequence represented as a string
    returns: a string containing the sequence of amino acids encoded by the
    the input DNA fragment"""
    
    aminoStrand = ''
    #Traverses the dna strand and finds the codons. Then traverses the codons
    #list and adds the appropriate amino acid to the string aminoStrand
    
    for i in range(0, len(dna), 3):
        m = i+3
        codon = dna[i:m];
        for j in range(len(codons)):
            for k in xrange(len(codons[j])):
                if (codons[j][k] == codon):
                    aminoStrand = aminoStrand + aa[j]                   
    return aminoStrand

def coding_strand_to_AA_unit_tests():
    """ Unit tests for the coding_strand_to_AA function """  
    print coding_strand_to_AA('ATGCCCGCTTT')
    print coding_strand_to_AA('TCGACTTTCCAGCGTATCGTGAT')

def get_reverse_complement(dna):
    """ Computes the reverse complementary sequence of DNA for the specfied DNA
        sequence
    
        dna: a DNA sequence represented as a string
        returns: the reverse complementary DNA sequence represented as a string
    """
    rev = ''
    #traverses backwards through the dna string and adds the appropriate complementary
    #nucleotide to a string.
    
    for i in range(len(dna)):
        s = dna[len(dna)-i-1]
        if (s == 'A'):
            t = 'T'
        if (s == 'T'):
            t = 'A'
        if (s == 'C'):
            t = 'G'
        if (s == 'G'):
            t = 'C'
        rev = rev + t
    return rev
    
def get_reverse_complement_unit_tests():
    """ Unit tests for the get_complement function """
        
    print get_reverse_complement('TCGACTTTCCAGCGTATCGTGAT')    

def rest_of_ORF(dna):
    """ Takes a DNA sequence that is assumed to begin with a start codon and returns
        the sequence up to but not including the first in frame stop codon.  If there
        is no in frame stop codon, returns the whole string.
        
        dna: a DNA sequence
        returns: the open reading frame represented as a string
    """
    dnaSeq= '' 
    #Traverses through a DNA sequence. When an ending codon is found, the loop breaks.
    #Otherwise, the codon is added to a string.
    for i in range(0, len(dna), 3):
        m = i+3
        s = dna[i:m]
        if (s== 'TAG' or s== 'TAA' or s== 'TGA'):
            break
        else:
            dnaSeq = dnaSeq + s
    return dnaSeq
    
def rest_of_ORF_unit_tests():
    """ Unit tests for the rest_of_ORF function """
        
    print rest_of_ORF('ATGCGCCGCCGCCGCCGCTAGCGCGCGCGCGCGCGCG')
    print rest_of_ORF('ATGCGTACGTAATCGATCCGATCGATCGATACGTAACTG')
        
def find_all_ORFs_oneframe(dna):
    """ Finds all non-nested open reading frames in the given DNA sequence and returns
        them as a list.  This function should only find ORFs that are in the default
        frame of the sequence (i.e. they start on indices that are multiples of 3).
        By non-nested we mean that if an ORF occurs entirely within
        another ORF, it should not be included in the returned list of ORFs.
        
        dna: a DNA sequence
        returns: a list of non-nested ORFs
    """
    
    ORF = []
    done = False
    i = 0    
    #runs through the loop as long as we haven't reached the end of the loop
    while done == False:
        piece = dna[i:(i+3)] #this is the codon we'll be looking at
        if (piece == 'ATG'):
            ORFPiece = rest_of_ORF(dna[i:len(dna)]) #prints out the sequence until it hits a stop codon
            ORF.append(ORFPiece)#adds this sequence piece to a list
            i = i+len(ORFPiece)#i jumps to the end of the sequence.
        else:
            i = i+3
        if (i >= len(dna)):
               done = True
    return ORF
        
    
#print find_all_ORFs_oneframe('ATGCATGAATGTAGATAGATGTGCCC')

def find_all_ORFs(dna):
    """ Finds all non-nested open reading frames in the given DNA sequence in all 3
        possible frames and returns them as a list.  By non-nested we mean that if an
        ORF occurs entirely within another ORF and they are both in the same frame,
        it should not be included in the returned list of ORFs.
        
        dna: a DNA sequence
        returns: a list of non-nested ORFs
    """
    ORFs = []
    for i in range(0,3):
        k = (find_all_ORFs_oneframe(dna[i:len(dna)]))        
        for j in range(len(k)):            
            ORFs.append(k[j])
    return ORFs

    
    

def find_all_ORFs_unit_tests():
    """ Unit tests for the find_all_ORFs function """
        
    print find_all_ORFs('ATGCATGAATGTAG') 
    print find_all_ORFs('ATGCATGAATGTAGATAGATGTGCCC')

def find_all_ORFs_both_strands(dna):
    """ Finds all non-nested open reading frames in the given DNA sequence on both
        strands.
        
        dna: a DNA sequence
        returns: a list of non-nested ORFs
    """
    allORFs = []
    
    k = find_all_ORFs(dna)
    m = find_all_ORFs(get_reverse_complement(dna))
       
    for i in range(len(k)):
        allORFs.append(k[i])
            
    for j in range(len(m)):
        allORFs.append(m[j])
    
    return allORFs
    

def find_all_ORFs_both_strands_unit_tests():
    """ Unit tests for the find_all_ORFs_both_strands function """

    print find_all_ORFs_both_strands('ATGCGAATGTAGCATCAAA')
    print find_all_ORFs_both_strands('ATGCATGAATGTAGATAGATGTGCCC')

def longest_ORF(dna):
    """ Finds the longest ORF on both strands of the specified DNA and returns it
        as a string"""

    ORFs = find_all_ORFs_both_strands(dna)
    
    longest = 'A'
    
    for x in ORFs:
        if len(x) >= len(longest):
            longest = x
    return longest
    
def longest_ORF_noncoding(dna, num_trials):
    from random import shuffle
    """ Computes the maximum length of the longest ORF over num_trials shuffles
        of the specfied DNA sequence
        
        dna: a DNA sequence
        num_trials: the number of random shuffles
        returns: the maximum length longest ORF """
    List = list(dna)       
    longest = ''

    for i in range(num_trials):
        shuffle(List)        
        shuffledDNA = collapse(List)
        s = longest_ORF(shuffledDNA)
        if len(s) >= len(longest):
            longest = s
    return len(longest)

from load import load_seq
dna = load_seq("./data/X73525.fa")

#print longest_ORF_noncoding(dna, 1500)

def gene_finder(dna, threshold):
    """ Returns the amino acid sequences coded by all genes that have an ORF
        larger than the specified threshold.
        
        dna: a DNA sequence
        threshold: the minimum length of the ORF for it to be considered a valid
                   gene.
        returns: a list of all amino acid sequences whose ORFs meet the minimum
                 length specified.
    """
    Aminos = []
    ORFs = find_all_ORFs_both_strands(dna)
    for x in ORFs:
        if len(x) > threshold:
            Aminos.append(coding_strand_to_AA(x))
    return Aminos

#def getThreshold():
#    from load import load_seq
#    dna = load_seq("./data/X73525.fa")
#    num = longest_ORF_noncoding(dna, 1500)
#    return num

def main():
    from load import load_seq
    dna = load_seq("./data/X73525.fa")
    
    Sequence = gene_finder(dna, 669)
    print Sequence

if __name__ == "__main__":
    main()
