# -*- coding: utf-8 -*-
"""
Created on Thu Aug 29 18:58:59 2024

@author: USER
"""


ngay = int(input("Nhập ngày: "))
thang = int(input("Nhập tháng: "))
nam = int(input("Nhập năm: "))

# Định dạng a: Ngày/tháng/năm
dinh_dang_a = str(ngay) + "/" + str(thang) + "/" + str(nam)
print("Định dạng a:", dinh_dang_a)

# Định dạng b: Ngày/tháng/năm (năm 2 chữ số)
dinh_dang_b = str(ngay) + "/" + str(thang) + "/" + str(nam)[-2:]
print("Định dạng b:", dinh_dang_b)

# Định dạng c: Năm/tháng/ngày
dinh_dang_c = str(nam) + "/" + str(thang) + "/" + str(ngay)
print("Định dạng c:", dinh_dang_c)
