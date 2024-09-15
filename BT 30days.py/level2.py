# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 22:04:46 2024

@author: USER
"""

#BT1 for từ 0->100 in tổng chữ số
tong = 0
for number in range(101):
    tong += number

print("Tổng các số từ 0 đến 100 là:", tong)

#BT2 0-> 100 in tổng số chẵn và lẻ
tong_so_chan = 0
tong_so_le = 0

for number in range(101):
    if number % 2 == 0:  # Kiểm tra xem số đó có chia hết cho 2 không (là số chẵn)
       tong_so_chan  += number
    else:
       tong_so_le += number

print("Tổng các số chẵn từ 0 đến 100 là:", tong_so_chan )
print("Tổng các số lẻ từ 0 đến 100 là:",tong_so_le)