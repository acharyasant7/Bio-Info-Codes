#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep  9 14:03:23 2020

@author: sandesh
"""

import math

def HardyWeinberg(homorece):
    m = []
    for i in homorece:
        q = math.sqrt(i)
        p = 1-q
        pro = 2*p*q + i
        m.append(pro)
    print(*m, sep = " ")

homorece= 0.604463601611, 0.72659083684, 0.141671747134, 0.35472443509, 0.179076981016, 0.0973651047939, 0.418890885977, 0.745314501281, 0.641280446143, 0.107966990329, 0.0530397752819, 0.422151065197, 0.707339878789, 0.843874697127, 0.697424924894, 0.632266212957, 0.483950676148, 0.321687438244

HardyWeinberg(homorece)