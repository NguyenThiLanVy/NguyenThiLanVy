# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 00:48:40 2024

@author: USER
"""

thang = int(input("Nhập tháng: "))
nam = int(input("Nhập năm: "))

# Kiểm tra năm nhuận
nam_nhuan = False
if nam % 4 == 0 and (nam % 100 != 0 or nam % 400 == 0):
    nam_nhuan = True

# Tính số ngày
so_ngay = 0
if thang in [1, 3, 5, 7, 8, 10, 12]:
    so_ngay = 31
elif thang == 2:
    if nam_nhuan:
        so_ngay = 29
    else:
        so_ngay = 28
else:
    so_ngay = 30

print("Tháng", thang, "năm", nam, "có", so_ngay, "ngày")