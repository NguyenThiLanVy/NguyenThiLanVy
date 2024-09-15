# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 00:52:13 2024

@author: USER
"""

a = int(input("Nhập độ dài cạnh a: "))
b = int(input("Nhập độ dài cạnh b: "))
c = int(input("Nhập độ dài cạnh c: "))

if a + b > c and a + c > b and b + c > a:

    if a == b == c:
        print("Đây là tam giác đều")
    elif a == b or a == c or b == c:
        print("Đây là tam giác cân")
    elif a**2 + b**2 == c**2 or a**2 + c**2 == b**2 or b**2 + c**2 == a**2:
        print("Đây là tam giác vuông")
    else:  
        print("Đây là tam giác thường")
else:
    print("Ba cạnh không tạo thành tam giác")