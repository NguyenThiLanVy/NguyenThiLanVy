# -*- coding: utf-8 -*-
"""
Created on Thu Aug 22 18:45:51 2024

@author: USER
"""
chuoi="Đại học Quốc gia, Khu phố 6, P. Linh Trung, Q. Thủ Đức, Tp. HCM"

print=(chuoi.replace(", ","\n"))
                       
print=chuoi.replace(", ","\n").replace("P. ","").replace("Q. ","").replace("Tp.", "")