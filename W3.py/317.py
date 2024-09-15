# -*- coding: utf-8 -*-
"""
Created on Mon Sep 16 00:21:45 2024

@author: USER
"""


n = int(input("Nhập số nguyên n: "))
for i in range(n):
    for j in range(n):
        if (i + j) % 2 == 0:
            print('*', end=' ')
        else:
            print(' ', end=' ')
    print()
    

