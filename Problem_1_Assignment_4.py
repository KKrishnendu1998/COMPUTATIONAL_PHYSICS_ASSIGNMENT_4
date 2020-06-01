#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Problem 1: Python code to generate 10000 uniformly distributed random numbers between 0 and 1 by linear congruential 
method
Created on Mon Jun  1 20:11:14 2020

@author: krishnendu
"""

import matplotlib.pyplot as plt


n=10000
a=12367
c=301345698
x=0.3
m=1

random_numbers=[]
for i in range(n):
    x=(a*x+c)%m
    random_numbers.append(x)
   

plt.hist(random_numbers,bins=10,density=True)
plt.title("Histogram")
plt.show()


