# -*- coding: utf-8 -*-
"""
Created on Mon Sep 16 00:43:09 2024

@author: USER
"""

a = int(input("Nhập số thứ nhất: "))
b = int(input("Nhập số thứ hai: "))
c = int(input("Nhập số thứ ba: "))
d = int(input("Nhập số thứ tư: "))
e = int(input("Nhập số thứ năm: "))

ds = [a, b, c, d, e]
ds.sort()
trung_vi = ds[2]
print("Trung vị là:", trung_vi)