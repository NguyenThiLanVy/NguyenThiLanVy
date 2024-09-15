# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 01:16:32 2024

@author: USER
"""

n = int(input("Nhập vào một số nguyên dương n: "))
S = 0
for i in range(1, n+1):
    S += 1 / (2*i)
print("Tổng S =", S)