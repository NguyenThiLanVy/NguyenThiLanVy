# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 01:21:35 2024

@author: USER
"""

for x in range(1, 979//2+1):  
    for y in range(1, (979-2*x)//7+1):
        z = (979 - 2*x - 7*y) // 9
        if z > 0:
            print(x, y, z)