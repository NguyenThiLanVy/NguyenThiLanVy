# -*- coding: utf-8 -*-
"""
Created on Thu Aug 22 19:33:03 2024

@author: USER
"""

#Viết hoa chữ đầu của chuỗi
a = "i'm a cat"
a = str.capitalize(a)
print(a)

#Viết hoa toàn bộ chuỗi
s = "i'm a cat"
s = str.upper(s)
print(s)

#Viết hoa chứ bất kì trong chuỗi
s = "i'm a cat"
s = s[0:2] + s[2].upper() + s[3:7] + s[7:9].upper() 
print (s)

#Viết hoa đầu chữ cái mỗi từ (C1 đếm)
b ="i am a cat"
b = b[0:1] + b[0].upper() + b[1:4]  + b[4].upper() + b[5:6] + b[6].upper() + b[7:9]

#Viết hoa đầu chữ cái mỗi từ
b = "i'm a cat"
b = s.swapcase()
print(b)

s = "i'm a cat"
print=("a.title")
