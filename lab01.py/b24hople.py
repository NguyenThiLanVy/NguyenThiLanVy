# -*- coding: utf-8 -*-
"""
Created on Fri Aug 30 00:08:19 2024

@author: USER
"""

a = int(input("Nhập số giờ:"))
b = int(input("Nhập số phút:"))
c = int(input("Nhập số giây:"))

if 0<=a<24 and b<=60 and c<=60:
    print("Thời gian hợp lệ")
else:
    print("Thời gian không hợp lệ")