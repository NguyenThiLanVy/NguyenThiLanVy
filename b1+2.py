# -*- coding: utf-8 -*-
"""
Created on Sat Sep 14 21:23:13 2024

@author: USER
"""
   
 #bai1
n = int(input("Nhập số nguyên dương n: "))
giaithua = 1
for i in range (1, n+1):
    giaithua *= i
    print ("Giai thừa của n là: ", giaithua)
    

#bai2
for i in range(2, 10):  
    for j in range(1, 11): 
        print(str(j) + " x " + str(i) + " = " + str(j * i))
    print()  
   

