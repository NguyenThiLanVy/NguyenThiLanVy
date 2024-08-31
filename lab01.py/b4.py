# -*- coding: utf-8 -*-
"""
Created on Sat Aug 31 16:20:03 2024

@author: USER
"""

N = int(input("Nhập số nguyên dương N có 2 chữ số: "))


chu_so_hang_chuc = N // 10
chu_so_hang_don_vi = N % 10


tong = chu_so_hang_chuc + chu_so_hang_don_vi
print(chu_so_hang_chuc, "+", chu_so_hang_don_vi, "=", tong)