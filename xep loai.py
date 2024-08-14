# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
#Đưa ra xếp loại
#Nhập điểm trung bình
GPA = float(input("Thông báo kết quả xếp hạng học lực :"))
#Xếp loại
if GPA < 3.5:
    print("Học lực kém")
elif 3.5 <= GPA < 5.0:
    print("Học lực Yếu")
elif 5.0 <= GPA < 7.0:
    print("Học lực Trung bình")
elif 7.0 <= GPA < 8.0:
    print("Họ lực Khá")
elif 8.0 <= GPA < 9.0:
    print("Học lực Giỏi")
elif 9.0 <= GPA <= 10:
    print("Học lực Xuất sắc")
else:
    print("Không xác định")
