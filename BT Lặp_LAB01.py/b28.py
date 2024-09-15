# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
n = int(input("Nhập vào một số nguyên dương: "))

while n <= 0:
  print("Số nhập vào không hợp lệ. Vui lòng nhập lại!")
  n = int(input("Nhập vào một số nguyên dương: "))

uoc_so = []
for i in range(1, n+1):
  if n % i == 0:
      uoc_so.append(i)
print("Các ước số của", n, "là:", uoc_so)
