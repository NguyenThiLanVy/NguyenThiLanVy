# -*- coding: utf-8 -*-
"""
Created on Sun Oct 13 00:25:21 2024

@author: USER
"""

#Bai 50
def kiem_tra(n):
    if n<0 and n%2 != 0:
        return -1
    elif n>0 and n%2 == 0:
        return 1
    return 0
print(kiem_tra(2))