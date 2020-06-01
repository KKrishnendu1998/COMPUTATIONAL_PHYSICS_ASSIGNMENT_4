#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Problem 4: Python code to plot the random number obtained by C code

@author: krishnendu
"""
import numpy as np
import matplotlib.pyplot as plt

y1=np.loadtxt("Problem_4.txt",usecols=0)

count,bins,patches=plt.hist(y1,100,density=True)
plt.plot(bins,2*np.exp(-bins/0.5))
plt.title("Histogram")
plt.show()