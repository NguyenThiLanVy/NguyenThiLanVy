# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 00:46:36 2024

@author: USER
"""

n = int(input("Nhập vào một số nguyên dương: "))

tong = 0
for chu_so in str(n):
    tong += int(chu_so)

print("Tổng các chữ số của", n, "là:", tong)