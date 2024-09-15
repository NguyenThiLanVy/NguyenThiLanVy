# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 01:14:32 2024

@author: USER
"""

n = int(input("Nhập vào một số nguyên dương n: "))
giai_thua = 1
for i in range(1, n+1):
    giai_thua *= i
print("Giai thừa của", n, "là:", giai_thua)