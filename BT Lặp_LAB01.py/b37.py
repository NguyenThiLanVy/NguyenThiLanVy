# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 01:13:24 2024

@author: USER
"""

n = int(input("Nhập vào một số nguyên dương chẵn n: "))
S = 0
for i in range(2, n+1, 2):
    S += i
print("Tổng S =", S)