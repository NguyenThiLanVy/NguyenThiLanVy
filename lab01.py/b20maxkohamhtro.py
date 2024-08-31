# -*- coding: utf-8 -*-
"""
Created on Sat Aug 31 00:33:20 2024

@author: USER
"""

a = int(input("Nhập số a: "))
b = int(input("Nhập số b: "))
c = int(input("Nhập số c: "))

if a >= b and a >= c:
    print("Số lớn nhất là a:", a)
if b >= a and b >= c:
    print("Số lớn nhất là b:", b)
else:
    print("Số lớn nhất là c:", c)
    