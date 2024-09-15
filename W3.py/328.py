# -*- coding: utf-8 -*-
"""
Created on Mon Sep 16 00:24:30 2024

@author: USER
"""

x = int(input("Nhập số nguyên x: "))
y = int(input("Nhập số nguyên y: "))

while y != 0:
  a=x%y
  x=y
  y=a
print("Ước chung lớn nhất của hai số là: {}".format(x))