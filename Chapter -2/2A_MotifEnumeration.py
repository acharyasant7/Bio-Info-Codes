#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 10 09:02:17 2020

@author: sandesh
"""

def Neighbors(Pattern, d):
   
    assert(d <= len(Pattern))
        
    if d == 0:
        return [Pattern]
    
    SuffixNeigh = Neighbors(Pattern[1:], d-1)
    Neighborhood = []
    Neighborhood.append(Pattern)
    for text in SuffixNeigh:
        for c in chars:
            if c!= Pattern[0]:
                Neighborhood.append(c + text)
                
    if (d < len(Pattern)):
        SuffixNeigh = Neighbors(Pattern[1:], d)
        for text in SuffixNeigh:
            Neighborhood.append(Pattern[0] + text) 

    return Neighborhood

chars = 'ATGC'

def MotifEnumeration(Dna,k,d):
    Patterns = []
    motif = []
    for string in Dna:        
        for i in range(0, len(string)-k+1):
            Patterns.append(string[i:i+k])
    
    for text in Patterns:
       
        Neighbours = Neighbors(text, d)
        
        for patt in Neighbours:
            count = 0
            patt2 = Neighbors(patt, d)
            for m in Dna:
               for elem in patt2:
                   if (m.find(elem) != -1):
                    count = count +1
                    break
            if count == len(Dna):
                motif.append(patt)
    motif = list(set(motif))
    return motif     
    

Dna =[]
n = int(input("How many DNA Sequences?"))
for i in range(0,n):
    Dna.append(input())
k = 5
d = 1
print(MotifEnumeration(Dna, k, d))
