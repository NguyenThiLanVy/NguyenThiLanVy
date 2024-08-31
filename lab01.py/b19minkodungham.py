# -*- coding: utf-8 -*-
"""
Created on Sat Aug 31 00:22:30 2024

@author: USER
"""

a = int(input("Nhập số a: "))
b = int(input("Nhập số b: "))
c = int(input("Nhập số c: "))
d = int(input("Nhập số d: "))

min_number = a

if b<min_number:
    min_number = b
if c<min_number:
    min_number = c
if d<min_number:
    min_number = d
    
print("Số nhỏ nhất là: ", min_number)