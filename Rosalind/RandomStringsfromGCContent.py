#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep  9 08:33:53 2020

@author: sandesh
"""

import math
def RandomStrings(string, GCContent):
    p= {}
    p['G'] = GCContent/2
    p['C'] = GCContent/2
    p['A'] = (1-GCContent)/2
    p['T'] = (1-GCContent)/2
    
    ptotal = 1
    for i in range(0, len(string)):
        ptotal = ptotal * p[string[i]]
    logp = math.log(ptotal, 10)
    return logp

strings = "AAGAGACAGGATGCAATGAACTCCCGTGTATGTGAGAAAAAGCAGGACGTACCATATGACCCGCCAATATCCGACTCTTCCG"
GCContents = 0.097, 0.120, 0.160, 0.260, 0.274, 0.346, 0.382, 0.443, 0.481, 0.549, 0.618, 0.675, 0.718, 0.758, 0.822, 0.874, 0.914
logP = [] 
for i in GCContents:
    logP.append(RandomStrings(strings, i))
print(*logP, sep = " ")