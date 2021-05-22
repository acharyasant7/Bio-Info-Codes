#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep  8 18:07:26 2020

@author: sandesh
"""


def MendelfirstLaw(k,m,n):
    tot = k+m+n
    
    p1 = k/tot * (k-1)/ (tot-1) #probability that two homozygous dominant will mate
    p2 = k/tot * m/(tot-1) #Probability that homozy dom mate with heterozygous, hence producing all phenotype dominant
    p3 = k/tot * n/(tot-1) #homozy dom mate with homozy recess
    
    p4 = m/tot * k/(tot-1) #heterozygous with homozygous dominant
    p5 = 3/4* m/tot * (m-1) /(tot-1) #heterozygous with heterozygous: 3:1 phenotypic ratio
    p6 = 1/2 * m/tot * n/(tot-1) #heterozygous with homozygous dominant
    
    p7 = n/tot * k/(tot-1)
    p8 = n/tot * m/(tot-1) * 0.5
    p9 = 0
    
    p = p1+p2+p3+p4+p5+p6+p7+p8+p9
    print(p)
    
k,m,n = 21, 24, 17
MendelfirstLaw(k, m, n)