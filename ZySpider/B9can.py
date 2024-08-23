# -*- coding: utf-8 -*-
"""
Created on Thu Aug 22 18:23:12 2024

@author: USER
"""

a = float(input("Nhập giá trị a:"))
b = float(input("Nhập giá trị b: "))

x = "math.sprt(a)"
y = "math.sprt(b)"

x1= pow(a**a, 1/4)
y2= pow(b**b, 1/4)
z= pow(a**b, 1/4)

ketqua = ((x1-y2)/(x1-y2)) - ((x1+z))/(x1+y2)

print("Kết quả của biểu thức là: ", ketqua)