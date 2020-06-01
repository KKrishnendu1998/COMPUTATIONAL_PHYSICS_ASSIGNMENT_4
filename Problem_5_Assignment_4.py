#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Problem 5: Use Box-Muller method in Python code to producre 10000 random numbers distributed according to an Gaussian 
distribution with mean 0 and variance 1.

@author: krishnendu
"""
import numpy as np
import matplotlib.pyplot as plt

x1=np.random.rand(100000)
x2=np.random.rand(100000)

y1=np.sqrt(-2*np.log(x1))*np.cos(2*np.pi*x2)

y2=np.sqrt(-2*np.log(x1))*np.sin(2*np.pi*x2)

count,bins,patches=plt.hist(y1,100,density=True)

plt.plot(bins,np.exp(-(bins**2)/2)/np.sqrt(2*np.pi))
plt.show()

count,bins,patches=plt.hist(y2,100,density=True)


plt.plot(bins,np.exp(-(bins**2)/2)/np.sqrt(2*np.pi))
plt.show()