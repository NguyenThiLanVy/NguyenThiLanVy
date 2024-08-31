# -*- coding: utf-8 -*-
"""
Created on Thu Aug 29 19:05:00 2024

@author: USER
"""

import math


a = float(input("Nhập số a: "))
b = float(input("Nhập số b: "))

tu_so = (a + b) / (3 * math.sqrt(a) + 3 * math.sqrt(b))
mau_so = (math.pow(math.sqrt(a) - math.sqrt(b), 3))**2
ket_qua = tu_so / mau_so


print("Kết quả của biểu thức là:", ket_qua)