#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep  9 08:54:06 2020

@author: sandesh
"""

#Suppose all elements of the set are represented by ether 0 or `1. 
#O means excluded and 1 means included. Not in this power set problem,
#which is composed of only 0 or 1, the solution to subsets reduces to 2^n 

import math
def Subsets(n):
    
    s = (2**n) % 1000000 
    return s
n = 929
print(Subsets(n))