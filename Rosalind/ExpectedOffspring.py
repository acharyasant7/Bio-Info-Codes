#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep  8 18:18:17 2020

@author: sandesh
"""


#The six input integer determine the number of couples with the following genotype in order
# AA-AA       AA-Aa       AA-aa      Aa-Aa     Aa-aa     aa-aa

#Offsprings showing dominant from each group = no of couples * probability of dominant *2

def ExpectedOffspring(a,b,c,d,e,f):
    
    total = a+b+c+d+e+f
    
    off1 = 1 * 2  *a
    off2 = 1*2*b
    off3 = 1*2*c
    off4 = 3/4*2*d
    off5 = 1/2*2*e
    off6 = 0
    
    ExpectedOffspring = off1+ off2 + off3 +off4 + off5 + off6
    print(ExpectedOffspring)

a,b,c,d,e,f = 18659, 16143, 18429, 19383, 16580, 16492
ExpectedOffspring(a, b, c, d, e, f)
    