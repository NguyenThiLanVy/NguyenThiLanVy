# -*- coding: utf-8 -*-
"""
Created on Sun Oct 13 00:53:21 2024

@author: USER
"""

#Bai53
#a) S = 1 + 2 + 3 +......+ n
def tong(n):
    s=0
    for i in range(1, n+1):
            s += i
    return s

#b) S = 1^2 +2^2 +3^2 +......+n^2
def tong_binh_phuong(n):
    s = 0
    for i in range(1, n+1):
        s += i*i
    return s

#c) S = 1 + 1/2 + 1/3 +......+ 1/n
def tong_phan_so(n):
    s = 0
    for i in range(1, n+1):
        s += 1/i
    return s

#d) S = 1! + 2! + 3! +......+ n!
def giai_thua(n):
    if n == 0:
        return 1
    else:
        return n * giai_thua(n-1)

def tong_giai_thua(n):
    s = 0
    for i in range(1, n+1):
        s += giai_thua(i)
    return s

#e) S = 1 * 2 * 3 *......* n
def tich(n):
    s = 1
    for i in range(1, n+1):
        s *= i
    return s

if __name__== '__main__':
    n = int(input("Nhập n: "))
    print(tong(5))
    print(tong_binh_phuong(2))
    print(tong_phan_so(2))
    print(tong_giai_thua(5))
    print(tich(32))