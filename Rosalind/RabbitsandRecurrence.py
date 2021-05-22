#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep  8 19:11:35 2020

@author: sandesh
"""


#Rabits and Recurrence Problem 
#The problem is solved using Dynamic Programming Approach
#Note for the first two months, number of rabbit pairs = 1,1 after that 
#the number of rabbit pairs is equal to no of rabbits in previous month plus the number of offsprings produced by rabbits 2 months prior. 

import numpy as np
def Rabits(n, k):
    
    F = np.zeros(n +1)
    F[1] = 1
    F[2] = 1
    for i in range(3, n+1):
        F[i] = F[i-1] + F[i-2] * k
    
    print(F[n])

Rabits(35,5)