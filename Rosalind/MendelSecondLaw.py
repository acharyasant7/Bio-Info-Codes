#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep  8 18:25:34 2020

@author: sandesh
"""

#After k generations, find the probability that at least N individuals will have genotype: AaBb
#Suppose independent assortment, Hence just considering for Aa
#The two possible cross are Aa* Aa or aa *Aa because everytime the children are crossed with Aa
#In both cases the probability of Aa 1/2 
#Thus, probability for AaBb is 1/4. Now, we can solve this problem using binomial distribution

import math
def MendelSecondLaw(k,N):
    total_children = 2**k #(K generations, 2 children in each)
    prob = []
    p = 1/4.0 #As explained in statement
    
    for i in range(N, total_children+1):
        prob.append(ncR(total_children, i) * (p **i) * ((1-p)**(total_children-i)))
       
    
    probability = sum(prob)
    print(probability)
       

def ncR(m,n):
    f = math.factorial
    C = f(m) / f(n) / f(m-n)
    
    
    return C

k,N = 5,8
MendelSecondLaw(k, N)