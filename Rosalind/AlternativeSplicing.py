#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep  9 11:56:28 2020

@author: sandesh
"""

#We use the formula for Combinations to determine the sum of combination of n integers talking only m at a time. 
#A variable i is iterated from m to n and value is modulated by 1000000 as required. 
import math

f = math.factorial
def AlternativeSplicing(m,n):
    s = 0
    for i in range(m, n+1):
        x = (f(n)// f(i)// f(n-i))
        
        x = x % 1000000
        s = (s+x) % 1000000
    return s

n,m  = 1976, 829
print(AlternativeSplicing(m, n))