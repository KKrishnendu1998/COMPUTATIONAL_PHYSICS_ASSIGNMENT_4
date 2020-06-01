#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Problem 3 : Python code to compute the time taken to generate 10000 random numbers by two methods mentioned 
in probelm 1 and problem 2

@author: krishnendu
"""
import numpy as np
import matplotlib.pyplot as plt
import time
t1=time.time()
n=10000
a=12367
c=301345698
x=0.3
m=1

result=[]
for i in range(n):
    x=(a*x+c)%m
    result.append(x)
t2=time.time()
    

plt.hist(result,bins=10,density=True)
plt.show()
print("The time taken by linear congruential method :",t2-t1)

t3=time.time()
result2=np.random.rand(10000)
t4=time.time()
plt.hist(result2,bins=10,density=True)
plt.show()
print("The time taken by numpy.random.rand",t4-t3)