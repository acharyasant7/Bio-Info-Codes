#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep  9 07:26:01 2020

@author: sandesh
"""

import math

def PartialPermutation(m,n):
    f = math.factorial
    x = f(m)/ f(m-n)
    y = x%1000000
    print(y)

m,n = 84, 8
PartialPermutation(m,n)