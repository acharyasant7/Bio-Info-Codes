#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 20 17:01:05 2020

@author: sandesh
"""
#This code determines the protein from the reading frame of RNA provided as input (in pattern).
#However, if the reading frame is not provided, you need to first determine the reading frame. 
#Reading frame is the RNA string starting with AUG, then checking for 3 nucleotides (at a time).
#While encountering UAA, UGA, or UAG as the 3 nucleotides, the reading frame is returned. 

def ProteinTranslation(Pattern, GeneticCode):
    protein = []
    for i in range(0, len(Pattern), 3):
        codon = Pattern[i:i+3]
        aminoacid = GeneticCode[codon] 
        protein.append(aminoacid)
    protein = ''.join(protein)
    return protein

Pattern = 'AUGGCGCCCUAUAACCGUACUUGGAUCAAUAUACUUAGGUAG'
GeneticCode = { 
        'AUA':'I', 'AUC':'I', 'AUU':'I', 'AUG':'M', 
        'ACA':'T', 'ACC':'T', 'ACG':'T', 'ACU':'T', 
        'AAC':'N', 'AAU':'N', 'AAA':'K', 'AAG':'K', 
        'AGC':'S', 'AGU':'S', 'AGA':'R', 'AGG':'R',                  
        'CUA':'L', 'CUC':'L', 'CUG':'L', 'CUU':'L', 
        'CCA':'P', 'CCC':'P', 'CCG':'P', 'CCU':'P', 
        'CAC':'H', 'CAU':'H', 'CAA':'Q', 'CAG':'Q', 
        'CGA':'R', 'CGC':'R', 'CGG':'R', 'CGU':'R', 
        'GUA':'V', 'GUC':'V', 'GUG':'V', 'GUU':'V', 
        'GCA':'A', 'GCC':'A', 'GCG':'A', 'GCU':'A', 
        'GAC':'D', 'GAU':'D', 'GAA':'E', 'GAG':'E', 
        'GGA':'G', 'GGC':'G', 'GGG':'G', 'GGU':'G', 
        'UCA':'S', 'UCC':'S', 'UCG':'S', 'UCU':'S', 
        'UUC':'F', 'UUU':'F', 'UUA':'L', 'UUG':'L', 
        'UAC':'Y', 'UAU':'Y', 'UAA':'_', 'UAG':'_', 
        'UGC':'C', 'UGU':'C', 'UGA':'_', 'UGG':'W', 
    } #table providing information about what codon codes for what amino acid. _ means stop codons. 
print(ProteinTranslation(Pattern, GeneticCode))
key_list = list(GeneticCode.keys()) 
val_list = list(GeneticCode.values()) 
  o
print(key_list[val_list.index('I')]) 
print(key_list[val_list.index("T")]) 