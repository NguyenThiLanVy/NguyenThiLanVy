# -*- coding: utf-8 -*-
"""
Created on Wed Aug 28 18:32:57 2024

@author: USER
"""
can_nang = float(input("Nhập cân nặng của bạn (kg):"))
chieu_cao = float(input("Nhập chiều cao của bạn (cm):"))
chieu_cao1 = chieu_cao / 100
bmi = can_nang / (chieu_cao1**2)
print ("Chỉ số BMI của bạn là: ", round(bmi,1))