# -*- coding: utf-8 -*-
"""
Created on Sun Aug 18 09:12:01 2024

@author: Student
"""

import math
print("ax^2 + bx + c =0")
a= float(input("nhap a:"))
b= float(input("nhap b:"))
c=float(input("nhap c:"))
delta = b**2 - (4*a*c)
if delta <0 :
    print ("phuong trinh vo nghiem")
elif delta==0:
    print  ("phuong trinh co nghiem kép x1=x2=",-(b/(2*a)))
else:
    print("phương trình có hai nghiệm phân biệt")
    x1= (-(b) + (math.sqrt(delta)))/(2*a)
    x2= (-(b)-(math.sqrt(delta)))/(2*a)
    print("x1=", x1) 
    print("x2=",x2)

    