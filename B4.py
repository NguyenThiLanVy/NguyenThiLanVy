# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
tongtien = 0
sokm = int(input("Nhập số km: "))
#1km
if (sokm == 1):
   tongtien = sokm * 20000
#3km
elif (sokm<=3):
   tongtien = sokm * 13000
elif (sokm<=8):
   tongtien = (3*13000) + (sokm-3)*12000
else:
   tongtien = tongtien = (3*13000) + (sokm-3)*12000 + (sokm-8)*10000
if (tongtien>100000):
   tongtien = tongtien = ((3*13000) + (sokm-3)*12000 + (sokm-8)*10000)*0.92
   
print("Tổng số tiền:", int(tongtien), "VND")