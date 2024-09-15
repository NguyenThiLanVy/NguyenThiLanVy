# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 00:48:41 2024

@author: USER
"""

quang_duong = float(input("Nhập quãng đường (km): "))

cuoc_van_chuyen = 0
if quang_duong <= 1:
    cuoc_van_chuyen = 15000
elif quang_duong <= 5:
    cuoc_van_chuyen = 15000 + (quang_duong - 1) * 13500
elif quang_duong <= 120:
    cuoc_van_chuyen = 15000 + 4 * 13500 + (quang_duong - 5) * 11000
else:
    cuoc_van_chuyen = 15000 + 4 * 13500 + 115 * 11000 + (quang_duong - 120) * 11000 * 0.9

print("Tổng cước vận chuyển:", cuoc_van_chuyen)