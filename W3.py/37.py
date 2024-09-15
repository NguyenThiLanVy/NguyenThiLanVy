# -*- coding: utf-8 -*-
"""
Created on Mon Sep 16 00:53:07 2024

@author: USER
"""

count = 0
for i in range(1000, 2000):
    print(i, end=" ")
    count += 1
    
    if count == 5:
        print()
        count = 0