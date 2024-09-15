# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 17:43:17 2024

@author: USER
"""
#BT1 for while 0->10
for i in range(11):
    print(i)
    
#BT2 for while 10->0
for i in range(10, -1, -1):
    print(i)
    
#BT3 vẽ hình vuông chứa #
height = 10
width = 15

for i in range(height):
    for j in range(width):
        print("#", end="")
    print()

#BT4 in bảng cửu chương 
for i in range(11):
    for j in range(11):
        result = i * j
        print(f"{i} x {j} = {result}")
        
#BT5 lặp 0->100 chỉ số chẵn
for i in range(0, 101, 2):
    print(i)

#BT6 lặp 0->100 chỉ số lẻ
for i in range(1, 101, 2):
    print(i)
    
