#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep  9 08:12:46 2020

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

seqlist = list(lists.values())
countGC = ["0"]* len(seqlist)
for i in range(0, len(seqlist)): 
    countGC[i] = seqlist[i].count("G") + seqlist[i].count("C")
    countGC[i] = countGC[i] / len(seqlist[i])

maxGC = max(countGC)
seqwithmaxGC = seqlist[countGC.index(maxGC)]
for k,v in lists.items():
    if v == seqwithmafor k,v in lists.items():
    if v == seqwithmaxGC:
        print(k)xGC:
        print(k)
print(maxGC*100)

