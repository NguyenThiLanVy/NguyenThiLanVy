# -*- coding: utf-8 -*-
"""
Created on Wed Aug 28 18:54:35 2024

@author: USER
"""
soxe = int(input("Nhập vào số xe của bạn (4 chữ số):"))

soxe1=soxe//1000
soxe2=soxe%1000//100
soxe3=soxe%100//10
soxe4=soxe%10

tong=soxe1 + soxe2 + soxe3 + soxe4
a=tong//10
b=tong%10

c=a+b

d=c//10
e=c%10
print("Biển số xe của bạn là:", soxe, "và số nút là", e)