# -*- coding: utf-8 -*-
"""
Created on Wed Aug 14 19:09:27 2024

@author: Student
"""
a = float(input("Nhập giá trị của a:"))
b = float(input("Nhập giá trị của b:"))
if a != 0:
    x = -b/a
    print("Nghiệm của phương trình là:", x)
else:
    if b == 0:
        print("Phương trình có vô số nghiệm.")
    else:
        print("Phương trình vô nghiệm.")