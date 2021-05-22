#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep  9 08:58:37 2020

@author: sandesh
"""
from collections import defaultdict
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
Patterns = list(lists.values())
sequences = []
k = len(Patterns[0])

count = 0

for i in Patterns:
    
    Prefix_i = i[:3]
    
    
    for  j in Patterns:
        s = len(j)    
        Suffix_j = j[s-3:]
       
        if Prefix_i == Suffix_j:
            if i!=j:
                m = j,i
                sequences.append(m)
f = open("f1.txt", 'w')

for i in sequences:
    f.write("\n")
    for m in range(0, len(i)): 
        for k,v in lists.items():
            if v == i[m]:
                f.write(k)
                if m == 0:
                    f.write(" ")

f.close()
    