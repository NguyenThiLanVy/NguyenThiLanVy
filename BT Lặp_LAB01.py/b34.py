# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 01:05:12 2024

@author: USER
"""

n = int(input("Nhập vào một số nguyên dương: "))

if n <= 1:
    print(n, "không phải là số nguyên tố")
else:
    is_prime = True
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            is_prime = False
            break
    if is_prime:
        print(n, "là số nguyên tố")
    else:
        print(n, "không phải là số nguyên tố")
    
    
    
    
    
   