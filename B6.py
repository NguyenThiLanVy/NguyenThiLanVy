# -*- coding: utf-8 -*-
"""
Created on Thu Aug 15 19:17:50 2024

@author: Student
"""

import random

luachon = ["Kéo", "Búa", "Bao"]
nguoichoi =input("Nhập kéo, búa, bao:" )
may = random.choice(luachon)
print("máy chọn", format(may))

if nguoichoi == may:
    print("Hòa")
elif nguoichoi == "Kéo" and may == "Bao" or\
     nguoichoi == "Búa" and may == "Kéo" or\
     nguoichoi == "Bao" and may == "Búa":
    print("Người chơi thắng")
else:
    print("Người chơi thua")