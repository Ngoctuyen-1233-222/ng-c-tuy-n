# -*- coding: utf-8 -*-
"""
Created on Sun Aug 18 09:36:38 2024

@author: Student
"""

a=float(input(" nhap he so a: "))
b=float(input(" nhap he so b:"))
c=float(input("nhap he so c:"))
if a+b>c and a+c>b and c+b>a:
    print(" a,b,c có thể là ba cạnh của một tam giác.")
else:
    print("a,b,c không phải là ba cạnh của một tam giác")