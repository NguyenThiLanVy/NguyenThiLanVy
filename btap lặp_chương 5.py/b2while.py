# -*- coding: utf-8 -*-
"""
Created on Sat Sep 14 22:55:54 2024

@author: USER
"""

count = 0
while True:
    try:
        n = float(input("Nhập vào một số thực trong khoảng [-89.9, 88.8]: "))
        if -89.9 <= n <= 88.8:
            print("Số bạn nhập hợp lệ!")
            break
        else:
            print("Số bạn nhập không hợp lệ. Vui lòng nhập lại!")
    except ValueError:
        print("Giá trị nhập vào không phải là số. Vui lòng nhập lại!")
count += 1
print("Bạn đã nhập", count, "lần.")