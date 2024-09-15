# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 01:22:31 2024

@author: USER
"""
max_sum = 0
for x in range(979//2, 0, -1):
    for y in range((979-2*x)//7, 0, -1):
        z = (979 - 2*x - 7*y) // 9
        if z > 0 and x + y + z > max_sum:
            max_sum = x + y + z
            print(x, y, z)

