#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug 23 17:43:59 2020

@author: sandesh
"""

#This code gives the minimum number of coins required to give as change for a sum of some money.
#This used Dynamic Programming to reduce the burden of repetative recursions. 
#In this method, a table is formed from 0 to money, and minimum number of coins for the money is filled. 
#Hence, when required, there is no need of recursion, but table can be referred to determine min coins for that money. 
import math

def DPChange(money, coins):
    MinCoins = [0]*(money+1) 
    MinCoins[0] = 0 #for 0 money, no coins should be retuned
    for m in range(1, money+1):
        MinCoins[m] = math.inf 
        for i in coins:           #look at coins once by one, and select the best one.
            if m >= i:
                if MinCoins[m-i]+1 < MinCoins[m]:
                    MinCoins[m] = MinCoins[m-i]+1
    
    return(MinCoins[money])
money = 18758
coins = [1,3,5,6,8,19,23]
print(DPChange(money, coins))