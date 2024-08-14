# -*- coding: utf-8 -*-
"""
Created on Wed Aug 14 20:24:24 2024

@author: Student
"""
print("Kiểm tra 3 cạnh của tam giác")
a = int(input("Nhập cạnh a: "))
b = int(input("Nhập cạnh b: "))
c = int(input("Nhập cạnh c: "))

if (a+b>c) and (a+c>b) and (b+c>a):
    
    print("{}, {}, {} là 3 cạnh của tam giác". format(a, b, c))
