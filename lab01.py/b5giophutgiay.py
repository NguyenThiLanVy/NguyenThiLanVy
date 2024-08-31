# -*- coding: utf-8 -*-
"""
Created on Thu Aug 29 19:29:42 2024

@author: USER
"""
#Viết chương trình cho phép nhập vào giờ, phút và giây theo định dạng hh:mm:ss. Hãy đổi ra giây và in kết quả ra màn hình.
a = int(input("Nhập số giờ: "))
b = int(input("Nhập số phút: "))
c = int(input("Nhập số giây: "))
print ("Nhập vào thời gian:{}:{}:{} ". format(a, b, c))

tong = a*3600 + b*60 + c
print ("Ket qua là: ", tong)

