#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep  8 20:53:40 2020

@author: sandesh
"""

#From a list of DNA Fasta sequences, this code returns the Consensus sequence and dictionary of profile matrix for A,C,G and T


from collections import defaultdict

def ProfileMatrix(motifs):
    A = []
    G= [] 
    C = [] 
    T = []
    Profile = {}
    consensus = ""
    for i in range(0, len(motifs[0])):
         
        countA, countC, countG, countT = 0,0,0,0
         
        for motif in motifs:
            
            if motif[i] == 'A':
                countA = countA+1
            if motif[i] == 'C':
                countC = countC+1
            if motif[i] == 'G':
                countG = countG+1
            if motif[i] == 'T':
                countT = countT+1
        

        if countA >= max(countC, countG, countT):
            consensus += "A"
        elif countC >= max(countA, countG, countT):
            consensus += "C"
        elif countG >= max(countC, countA, countT):
            consensus += "G"
        elif countT >= max(countC, countG, countA):
            consensus += "T"
     
        
        A.append(countA)
        G.append(countG)
        C.append(countC)
        T.append(countT)
    

    Profile['A'] = A
    Profile['C'] = C
    Profile ['G'] = G
    Profile['T'] = T
    #Now, you can print as the output is required
   
f = open('profile.fasta','r')
lists=defaultdict(str)
name = ''
for line in f:
    #if your line starts with a > then it is the name of the following sequence
    if line.startswith('>'):
        name = line[1:-1]
        continue #this means skips to the next line
    #This code is only executed if it is a sequence of bases and not a name.
    lists[name]+=line.strip()

sequences = list(lists.values())

ProfileMatrix(sequences)