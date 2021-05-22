#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep  8 17:47:42 2020

@author: sandesh
"""


def DNA(string):
    
    countA, countC, countG, countT = 0,0,0,0
    
    for i in range(0, len(string)):
        if string[i] == 'A':
            countA = countA + 1
        elif string[i] == 'C':
            countC = countC+1
        
        elif string[i] == 'G':
            countG = countG+1
        elif string[i] == 'T':
            countT = countT+1
    
    print(countA, countC, countG, countT)

string = "AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC"
DNA(string)