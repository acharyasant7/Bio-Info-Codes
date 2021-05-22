#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep  9 14:10:01 2020

@author: sandesh
"""

#To implement the Wright-Fischer model, first of all calculate the probability of obtaining 1-2N recessive alleles in the first generation using Binomial Distribution
#Secondly, in next generation: first calculate the probability of obtaining 1 recessive from 1-2N recessive parents(sum of all). Similarly, calculate the probabilties for all 1-2N number of recessive chromosomes. 
#Assign, the probability in the second generation as parent and continue for third till g generations and finally calculate required probability. 
import math

def ncr(a,b):
    f = math.factorial
    x = f(a) /(f(b)* f(a-b))
    return x

def WrightFischer(N,m,g,k):
    p = []
    s = 2*N
    pm = m / (2*N)
    prec = 1 -pm
    for i in range(1, s+1):
        x = ncr(s, i) * (prec**i) * (pm)**(s-i)
        p.append(x)
    
    for gen in range(2,g+1):
        new_p = []
        for t in range(1, s+1):
            p_next = []
            z = 0
            for x in range(1, s+1):
                p_next.append(ncr(s, t)*((x/(s))**t)*(1.0-(x/(s)))**(s-t))
            for i in range(len(p_next)):
                z = z+ p[i]*p_next[i]
            new_p.append(z) 
        p = new_p
    prob = sum(p[k-1:])
    print(prob)
    
N, m, g, k = 5,10,5,6

WrightFischer(N,m,g,k)