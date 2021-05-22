#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep  9 17:04:18 2020

@author: sandesh
"""

#This code helps demonstrate the founder effect through WrightFischer Model
#For different values of number of recessive genes at start, the parameters are passed into the WrightFischer model
#and the probability that the gene is lost in m generations is obtained generation by generation. 

import math

def ncr(a,b):
    f = math.factorial
    x = f(a) /(f(b)* f(a-b))
    return x

def FounderEffect(N,m,A):
    
    s = 2*N
    
    for i in A:
        prec = i/s
        print('\nThe logarithm of probability the recessive gene is lost in different generations when number of allles is', i, "is")
        WrightFischer(s, prec, m )
    
def WrightFischer(s, prec, g):
    p = []
    pm = 1-prec
    for i in range(1, s+1):
        x = ncr(s, i) * (prec**i) * (pm)**(s-i)
        p.append(x)
    gen1 = sum(p[0:])
    norec1 = 1-gen1
    print(math.log(norec1, 10))
    for gen in range(2,g+1):
        new_p = []
        for t in range(1, s+1):
            p_next = []
            z = 0
            for x in range(1, s+1):
                p_next.append(ncr(s, t)*((x/(s))**t)*(1.0-(x/(s)))**(s-t))
            for i in range(len(p_next)):
                z = z + p[i]* p_next[i]
            new_p.append(z) 
        p = new_p
        pss= 1- sum(p[0:])
        print(math.log(pss, 10))
    
N,m = 16,3
A = [1, 6, 7]
FounderEffect(N,m,A)