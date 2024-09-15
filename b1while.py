# -*- coding: utf-8 -*-
"""
Created on Sat Sep 14 22:04:00 2024

@author: USER
"""
#bai4
count = 0
while True:
    n = int(input("Nhập một số nguyên từ -99 đến 99: "))
    count += 1
    if -99 <= n <= 99:
        print("Giá trị hợp lệ!")
        break
    else:
        print("Giá trị không hợp lệ. Vui lòng nhập lại.")
print("Bạn đã nhập", count, "lần.")




