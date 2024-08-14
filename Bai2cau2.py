# -*- coding: utf-8 -*-
"""
Created on Wed Aug 14 19:45:03 2024

@author: Student
"""

# import thư viện
import math

#Nhập dữ liệu
print("Giải phương tình bậc 2: ax^2 + bx + c = 0")
a = float(input("Nhập giá trị của a:"))
b = float(input("Nhập giá trị của b:"))
c = float(input("Nhập giá trị của c:"))

if(a!=0):
    delta = b**2 - 4*a*c
    if (delta<0):
        print("Phương trình vô nghiệm")
    elif (delta==0):
        print("Có nghiệm kép x1=x2=" , 'x')
    else:
        x1 = (-b-math.sqrt(delta))/(2*a)
        x1 = (-b+math.sqrt(delta))/(2*a)
        print(f"Có nghiệm kép x1={0} và x2={1}")
else:
        print("Không phải phương trình bậc 2")