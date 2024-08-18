# -*- coding: utf-8 -*-
"""
Created on Sun Aug 18 10:18:22 2024

@author: Student
"""

a=float(input("số km quãng đường đi được:"))
if a==1:
    st =20 
    print("tong tien :",st)
elif a<=3:
    st= a*13
    print("tong so tien:",st)
elif a<=8:
     st= 3*13+(a-3)*12
     print("tong so tien :",st)
else:
    st=3*13+5*12+(a-8)*10
    if st >100:
      s1=st*0.92
      print("tong so tien:",s1)
    else:
        print("tong so tien:",st)
        