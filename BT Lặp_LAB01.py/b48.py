# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 01:25:00 2024

@author: USER
"""

min_sum = float('inf')
for x in range(1, 979//2+1):
    for y in range(1, (979-2*x)//7+1):
        z = (979 - 2*x - 7*y) // 9
        if z > 0 and x + y + z < min_sum:
            min_sum = x + y + z
            print(x, y, z)