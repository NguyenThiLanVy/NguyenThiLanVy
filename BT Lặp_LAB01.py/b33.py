# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 00:57:45 2024

@author: USER
"""

import math

n = int(input("Nhập vào một số nguyên dương: "))

can_bac_hai = math.sqrt(n)
if can_bac_hai == int(can_bac_hai):
    print("là số chính phương")
else:
    print(n, "không phải là số chính phương")