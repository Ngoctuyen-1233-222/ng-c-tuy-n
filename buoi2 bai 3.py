# -*- coding: utf-8 -*-
"""
Created on Sun Aug 18 07:29:43 2024

@author: Student
"""
distance=float(input("nhập độ dài đoạn đường đến trường(m):"))
if distance <300:
    print("đường đến trường quá gần.thôi!đi bộ")
elif distance>1200:
    print("đường đến trường quá xa.thôi!đi xe máy")
elif distance>=300 and distance<=700:
    print("đường đến trường không xa.thôi!đi xe đạp")
else:
    print("không xác định")    