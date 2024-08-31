# -*- coding: utf-8 -*-
"""
Created on Sat Aug 31 15:58:55 2024

@author: USER
"""

chu_cai = input("Nhập một chữ cái: ")

if chu_cai.islower():
    chu_cai_moi = chu_cai.upper()
else:
    chu_cai_moi = chu_cai.lower()

print("Chữ cái mới:", chu_cai_moi)