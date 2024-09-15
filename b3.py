# -*- coding: utf-8 -*-
"""
Created on Sat Sep 14 21:59:38 2024

@author: USER
"""

#bai3
import random

min_length = 20
max_length = 30

length = random.randint(min_length, max_length)

numbers = []
for _ in range(length):
    number = random.uniform(18, 99)  
    numbers.append(number**2)

print(numbers)