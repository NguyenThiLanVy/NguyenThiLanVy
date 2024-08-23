# -*- coding: utf-8 -*-
"""
Created on Wed Aug 21 19:50:11 2024

@author: USER
"""
giay =int(input("Nhập số giây:"))
phut =int(input("Nhập số phút:"))
gio = int(input("Nhập số giờ:"))

tonggiay = gio*3600 + phut*60 + giay
print("Số giây là: ", tonggiay)
