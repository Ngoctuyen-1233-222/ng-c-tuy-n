# -*- coding: utf-8 -*-
"""
Created on Sun Aug 18 10:01:16 2024

@author: Student
"""
a= float(input("nhap he so a:"))
b= float(input("nhap he so b:"))
c= float(input("nhap he so c:"))
if a==b==c:
    print("tam gác đều.")
elif a==b or a==c or b==c:
    print("tam giác cân") 
elif a**2 + b**2 == c**2 or b**2 + c**2 == a**2 or a**2 + c**2 == b**2:  
    print("Đây là tam giác vuông")
       
