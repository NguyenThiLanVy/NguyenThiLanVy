# -*- coding: utf-8 -*-
"""
Created on Mon Sep 16 00:30:03 2024

@author: USER
"""

import math
n = int(input("Nhập n: "))
for i in range(1, n+1):
    for j in range(1, n+1):
        if math.gcd(i, j) == 1:
            print('*', end=' ')
        else:
            print(' ', end=' ')
    print()