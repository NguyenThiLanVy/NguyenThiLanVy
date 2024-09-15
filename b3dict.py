# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 00:29:23 2024

@author: USER
"""

n = int(input("Nhập vào một số nguyên n: "))

my_dict = {}
for i in range(1, n+1):
    my_dict[i] = i**2

print(my_dict)