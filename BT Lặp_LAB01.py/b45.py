# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 01:21:11 2024

@author: USER
"""

n = int(input("Nhập vào số nguyên dương n: "))
x = int(input("Nhập vào số nguyên dương x: "))

S = x
mau_so = 1
for i in range(2, n+1):
    mau_so += i
    S += (x**i) / mau_so
print("Tổng S =", S)