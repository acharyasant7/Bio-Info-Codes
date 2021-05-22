#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep  9 10:51:51 2020

@author: sandesh
"""


count = 0 
data = []
with open(r"tree.txt") as file:
    for line in file:
        data.append(line.strip())
        count = count+1

nodes = int(data[0]) #FirstLineofFile
total_edges_present = count-1 #First line gives total nodes

total_edges_required = nodes - 1 
total_edges_to_add = total_edges_required- total_edges_present
print(total_edges_to_add) 