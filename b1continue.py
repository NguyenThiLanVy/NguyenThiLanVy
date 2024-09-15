# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 00:15:24 2024

@author: USER
"""

numbers = []
for num in range(2018, 2829):
    if num % 2 != 0 or num % 5 != 0:
        continue  
    numbers.append(num)

print(numbers)