# -*- coding: utf-8 -*-
"""
Created on Sun Oct 13 01:09:33 2024

@author: USER
"""

def fibonacci(n):
    fib = [0, 1]
    while len(fib) < n:
       fib.append(fib[-1] + fib[-2])
    
    return fib

if __name__ == "__main__":
  n = int(input("Nhập số lượng số Fibonacci: "))
  print(fibonacci(n))
  
  
