#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Problem 5: Python code to produce random number distributed according to Gaussian distribution 
Created on Sat May 23 04:51:17 2020

@author: krishnendu
"""

import numpy as np
import matplotlib.pyplot as plt

def fun(x):    #defining the function
    return np.sqrt(2/np.pi)*np.exp(-x**2/2)

x=np.linspace(0,10,1000)
random=np.random.rand(10000)

Z=-np.log(random)    #creating the exponential distribution 
X1=[]
Y1=[]

for i in range(len(random)):
    c=1.5*np.exp(-Z[i])*np.random.rand(1)
 
        
    if(c<fun(Z[i])):                  #checking
        X1.append(Z[i])
        Y1.append(c)
   
        

counts,bins,patches=plt.hist(X1,10,density=True)
plt.plot(bins,fun(bins))
plt.plot("Histogram")
plt.show()


