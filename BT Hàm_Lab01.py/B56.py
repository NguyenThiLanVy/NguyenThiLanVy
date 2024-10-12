# -*- coding: utf-8 -*-
"""
Created on Sun Oct 13 01:06:09 2024

@author: USER
"""

def tinh_hinh(hinh, *args, **kwargs):
    if hinh == "vuong":
    canh = args[0]
    if kwargs.get("tinh") == "cv":
      return 4 * canh
    elif kwargs.get("tinh") == "dt":
      return canh * canh
  elif hinh == "chu_nhat":
    chieu_dai, chieu_rong = args
    if kwargs.get("tinh") == "cv":
      return 2 * (chieu_dai + chieu_rong)
    elif kwargs.get("tinh") == "dt":
      return chieu_dai * chieu_rong
  elif hinh == "tron":
    ban_kinh = args[0]
    if kwargs.get("tinh") == "cv":
      import math
      return 2 * math.pi * ban_kinh
    elif kwargs.get("tinh") == "dt":
      import math
      return math.pi * ban_kinh * ban_kinh
  else:
    return "Hình không hợp lệ"


ket_qua1 = tinh_hinh("vuong", 10, tinh="cv")
print("Chu vi hình vuông:", ket_qua1)

ket_qua2 = tinh_hinh(18, hinh="tron", tinh="dt")
print("Diện tích hình tròn:", ket_qua2)

ket_qua3 = tinh_hinh(20, 30, hinh="chu_nhat", tinh="cv")
print("Chu vi hình chữ nhật:", ket_qua3)
