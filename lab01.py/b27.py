# -*- coding: utf-8 -*-
"""
Created on Sat Aug 31 16:10:47 2024

@author: USER
"""

import math

hinh = input("Nhập hình (v, n, t): ")

if hinh == 'v':
    canh = float(input("Nhập độ dài cạnh hình vuông: "))
    chu_vi = 4 * canh
    dien_tich = canh * canh
elif hinh == 'n':
    chieu_dai = float(input("Nhập chiều dài hình chữ nhật: "))
    chieu_rong = float(input("Nhập chiều rộng hình chữ nhật: "))
    chu_vi = 2 * (chieu_dai + chieu_rong)
    dien_tich = chieu_dai * chieu_rong
elif hinh == 't':
    ban_kinh = float(input("Nhập bán kính hình tròn: "))
    chu_vi = 2 * math.pi * ban_kinh
    dien_tich = math.pi * ban_kinh * ban_kinh
else:
    print("Hình không hợp lệ!")

if hinh in ['v', 'n', 't']:
    print("Chu vi =", chu_vi)
    print("Diện tích =", dien_tich)