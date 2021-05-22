#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep  9 12:12:43 2020

@author: sandesh
"""

#As one diploid organism, will obtain one set of chromosomes from father and another set from mother.
#Both of them will have same chromosome if they inherit some chromosome from father or mother. The probability that both will obtain chromosome
#from father or mother is 1/2 (sum of 1/4+1/4). Hence, now we can solve this in form of binomial distribution.
#First loop finds probability of k same chromosomes, second loop finds probability of at least k same chromosome and third loop finds out the log value. 
import math

def IndependentSeg(n):
    l = 2*n
    s = [0] * (l+1)
    m= [0] * (l+1)
    t= [0] * (l+1)
    for i in range(1, l+1):
        m[i] = ncr(l, i) * (1/2) ** i * (1/2)**(l-i)
    
   
    for z in range(1, l+1):
        s[z]= sum(m[z:])
    
    for i in range(1, l+1):
        t[i] = math.log(s[i], 10)
    
    print(*t[1:], sep = " ")
    
        

def ncr(a,b):
    f = math.factorial
    x = f(a)/ (f(b)*f(a-b))
    return x

IndependentSeg(43)