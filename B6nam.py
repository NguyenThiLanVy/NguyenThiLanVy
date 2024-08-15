# -*- coding: utf-8 -*-
"""
Created on Thu Aug 15 19:54:24 2024

@author: Student
"""

nhapvao= input("nhập vào ngày tháng năm: ")
dd, mm, yyyy= map(int,nhapvao.split("/"))

if yyyy % 4 == 0 and yyyy % 100 !=0 or  yyyy % 400 == 0:
    print("năm nhuận")
else:
    print( "năm không nhuận")
if mm == 4 or mm == 6 or mm == 9 or mm == 11:
    songaymax=30
if mm == 1 or mm == 3 or mm == 5 or mm == 7 or mm == 8 or mm == 10 or mm == 12:
    songaymax=31
if dd < 1 and dd > songaymax:
    False
if mm < 1 and mm > 12:
    False
if yyyy <1 and yyyy>1000000000:
    False

    print("thời gian nhập không hợp lệ")
else:
    print("thời gian nhập hợp lệ")