# -*- coding: utf-8 -*-
"""
Created on Sat Aug 31 15:44:48 2024

@author: USER
"""

a = float(input("Nhập số a: "))
b = float(input("Nhập số b: "))

if a != 0 :
    print("Phương trình có nghiệm x = ", -b/a)
else:
    if b != 0:
        print("Phương trình vô nghiệm")
    else:
        print("Phương trình có vô số nghiệm")