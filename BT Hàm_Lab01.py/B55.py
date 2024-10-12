# -*- coding: utf-8 -*-
"""
Created on Sun Oct 13 01:02:20 2024

@author: USER
"""

def tinh_chu_vi(chieu_dai, chieu_rong):
  chu_vi = 2 * (chieu_dai + chieu_rong)
  return chu_vi

def tinh_dien_tich(chieu_dai, chieu_rong):
  dien_tich = chieu_dai * chieu_rong
  return dien_tich

def ve_hinh_chu_nhat(chieu_dai, chieu_rong):
  for i in range(chieu_rong):
    for j in range(chieu_dai):
      print("*", end="")
    print()

if __name__ == "__main__":
  chieu_dai = int(input("Nhập chiều dài: "))
  chieu_rong = int(input("Nhập chiều rộng: "))

  chu_vi = tinh_chu_vi(chieu_dai, chieu_rong)
  dien_tich = tinh_dien_tich(chieu_dai, chieu_rong)

  print("Chu vi hình chữ nhật:", chu_vi)
  print("Diện tích hình chữ nhật:", dien_tich)
  print("Hình chữ nhật:")
  ve_hinh_chu_nhat(chieu_dai, chieu_rong)