# -*- coding: utf-8 -*-
"""
Created on Sun Oct 13 00:28:49 2024

@author: USER
"""
#Bai 51
def ktra_gtri():
    gtri = input("Nhập giá trị:")
    
    if gtri.strip('-').isdigit():
        gtri = int(gtri)
    if -89 <= gtri <= 90:
        return gtri
    print("Không hợp lệ, nhập lại")
    return ktra_gtri()
print(ktra_gtri())