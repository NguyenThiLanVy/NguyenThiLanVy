# -*- coding: utf-8 -*-
"""
Created on Sat Aug 31 16:26:14 2024

@author: USER
"""
import datetime

def cong_tru_gio_datetime(time1, time2, phep_toan="+"):
  if phep_toan == "+":
    return time1 + time2
  else:
    return time1 - time2

# Ví dụ sử dụng
time1 = datetime.datetime(1900, 1, 1, 2, 30, 45)
time2 = datetime.datetime(1900, 1, 1, 1, 15, 30)

ket_qua_cong = cong_tru_gio_datetime(time1, time2)
ket_qua_tru = cong_tru_gio_datetime(time1, time2, "-")

print("Kết quả cộng:", ket_qua_cong)
print("Kết quả trừ:", ket_qua_tru)
