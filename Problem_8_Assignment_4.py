#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Python code to calculate the area of a circle the calculate the volume of a ten dimensional sphere

@author: krishnendu
"""

import numpy as np

def fun(x,y):
    if x**2+y**2<=1:
        return 1
    else :
        return 0
n=1000000
x=np.random.rand(n)
y=np.random.rand(n)
result=0
for i in range(n):
    result+=fun(x[i],y[i])
I=4*result/n
print("The area of the circle is :",I)

#volume of an ten dimensional sphere 

def func(x):
    if sum(x**2)<=1:
        return 1
    else :
        return 0

k=10*n
x=np.zeros(k).reshape(10,n)
for i in range(10):
    x[i]=np.random.rand(n)

vol=0
for i in range(n):
    vol+=func(x[:,i])
vol=(2**10)*vol/n
print("the volume of the ten dimensional sphere is :",vol)


