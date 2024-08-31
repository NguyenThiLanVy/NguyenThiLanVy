# -*- coding: utf-8 -*-
"""
Created on Sat Aug 31 16:08:09 2024

@author: USER
"""

def sap_xep_so_tang_dan(N):

  list_so = [int(ch) for ch in str(N)]
  

  list_so.sort()
  so_moi = int(''.join(str(x) for x in list_so))
  
  return so_moi

N = int(input("Nhập số nguyên N: "))
ket_qua = sap_xep_so_tang_dan(N)
print("Số có các chữ số tăng dần:", ket_qua)