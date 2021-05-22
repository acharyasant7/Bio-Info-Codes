#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep  9 07:32:07 2020

@author: sandesh
"""


import itertools

def Permutations(n):
    number = []
    for i in range(1, n+1):
        number.append(i)
    
    perm = itertools.permutations(number)
    permutationlist = list(perm)
    print(len(permutationlist))
    
    f = open("s.txt", 'w')
    for i in permutationlist:
        print(*i, sep = " ")
       
    
n = 5
Permutations(n)