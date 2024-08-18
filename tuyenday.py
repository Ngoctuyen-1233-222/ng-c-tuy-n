# -*- coding: utf-8 -*-
"""
Created on Sun Aug 18 08:12:24 2024

@author: Student
"""

a = float (input("nhập hệ số a:"))
b= float (input("nhập hệ số b:"))
if a==0:
    if b==0:
        print ("phương trình có vô số nghiệm") 
    else:
        print("phương trình vô nghiệm")
else:
    x=-b/a
    print (f"nghiệm của phương tình là x={x}")
    