# -*- coding: utf-8 -*-
"""
Created on Sat Aug 31 23:18:47 2024

@author: USER
"""

h1 = int(input("Nhập giờ thứ nhất: "))
m1 = int(input("Nhập giờ phút thứ nhất: "))
s1 = int(input("Nhập giây thứ nhất: "))

h2 = int(input("Nhập giờ thứ hai "))
m2 = int(input("Nhập giờ phút thứ hai: "))
s2 = int(input("Nhập giây thứ hai: "))

if h1 > 24 and h2 > 24 and m1 > 60 and m2 > 60 and s1 > 60 and s2 > 60:
    print("thời gian không hợp lệ")
else:
    print("Thời gian")
tonggiay1 = h1*3600 + m1*60 + s1
tonggiay2 = h2*3600 + m2*60 + s2

tong = tonggiay1 + tonggiay2
sogio = tong//3600
sophut = tong%3600 // 60
sogiay = tong-(sogio*3600 + sophut*60)
print("kết quả tổng: ", sogio, "h", sophut, "m", sogiay, "s")

if tonggiay1 > tonggiay2:
    hieu = tonggiay1 - tonggiay2
    sogio = hieu//3600
    sophut = hieu%3600//60
    sogiay = hieu - (sogio*3600 + sophut*60)
    print("Kết quả: ", sogio, "h", sophut, "m", sogiay, "s")
    
elif tonggiay1 < tonggiay2:
    hieu = tonggiay1 - tonggiay2
    sogio = hieu//3600
    sophut = hieu%3600//60
    sogiay = hieu - (sogio*3600 + sophut*60)
    print("Kết quả: ", sogio, "h", sophut, "m", sogiay, "s")
    