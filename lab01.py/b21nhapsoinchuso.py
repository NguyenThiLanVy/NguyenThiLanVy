# -*- coding: utf-8 -*-
"""
Created on Sat Aug 31 00:37:07 2024

@author: USER
"""
so_chu = ["Không" , "Một" , "Hai" , "Ba" , "Bốn" , "Năm" , "Sáu" , "Bảy" , "Tám" , "Chín"]
so = int(input("Nhập một số: "))
if 0 <= so <= 9:
    print(so_chu[so])
else:
    print("Không đọc được")