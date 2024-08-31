# -*- coding: utf-8 -*-
"""
Created on Sat Aug 31 15:51:08 2024

@author: USER
"""

import math

a = float(input("Nhập a:"))
b = float(input("Nhập b:"))
c = float(input("Nhập c:"))

if (a!=0):
    delta = b**2 - 4*a*c
    if(delta<0):
       print ("Phương trình vô nghiệmNhập 1 chữ cái, nếu là chữ thường thì đổi thành chữ hoa, ngược lại đổi thành chữ thường.")
    elif(delta==0):
       x = -b/(2*a)
       print("Phương trình có nghiệm kép x1=x2", x)
    else:
        x1= ((-b+math.sqrt(delta))/(2*a))
        x2= ((-b-math.sqrt(delta))/(2*a))
        print("Phương trình có 2 nghiêm phân biệt x1={0} và x2={1}". format(x1, x2))
else:
    print("Không phải là phương trình bậc 2")