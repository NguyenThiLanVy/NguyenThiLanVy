# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 00:26:51 2024

@author: USER
"""

numbers = []
for num in range(2020, 3839):  # range(2020, 3839) để bao gồm cả số 3838
    if num % 2 != 0:
        continue  # Bỏ qua số lẻ
    if num % 9 != 0:
        continue  # Bỏ qua số không chia hết cho 9
    numbers.append(num)

print(*numbers, sep="\t")