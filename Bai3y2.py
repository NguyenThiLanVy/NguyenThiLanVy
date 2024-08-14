# -*- coding: utf-8 -*-
"""
Created on Wed Aug 14 20:10:31 2024

@author: Student
"""
a = float(input("Nhập cạnh a: "))
b = float(input("Nhập cạnh b: "))
c = float(input("Nhập cạnh c: "))

if a + b > c and a + c > b and b + c > a:
    print("Đây là một tam giác")
    
    if a == b and b == c:
        print("Đây là tam giác đều")
    elif a == b or b == c or a == c:
        print("Đây là tam giác cân")
        
        if a**2 + b**2 == c**2 or a**2 + c**2 == b**2 or b**2 + c**2 == a**2:
            print("Đây là tam giác vuông cân")
        else:
            print("Đây là tam giác cân nhưng không phải tam giác vuông cân")
    elif a**2 + b**2 == c**2 or a**2 + c**2 == b**2 or b**2 + c**2 == a**2:
        print("Đây là tam giác vuông")
    else:
        print("Đây là tam giác thường")
else:
    print("Đây không phải là một tam giác")
