# -*- coding: utf-8 -*-
"""
Created on Mon Sep 16 00:53:46 2024

@author: USER
"""

import random
n = int(input("Nhập số lượng số ngẫu nhiên n: "))

tong = 0
max_1 = 10**9
min_1 = 10**9

for i in range(n):
    songaunhien = random.random()
    tong += songaunhien
    if songaunhien < min_1:
        min_1 = songaunhien
    if songaunhien > max_1 :
        max_1 = songaunhien

tb = tong / n

print("Giá trị trung bình: {:.4f}".format(tb))
print("Giá trị nhỏ nhất: {:.4f}".format(min_1))
print("Giá trị lớn nhất: {:.4f}".format(max_1 ))