#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Problem 9 : MCMC 

Created on Fri May 29 08:53:19 2020

@author: krishnendu
"""

import numpy as np
import matplotlib.pyplot as plt
def fun(x):
    if 3<=x<=7 :
        return 1
    else:
        return 0
theta=[]
theta.append(3)
nsteps=1000000
for i in range(nsteps-1):
    theta_prime=theta[i]+np.random.standard_normal()
    
    if fun(theta_prime)/fun(theta[i])> np.random.rand():
        theta.append(theta_prime)
    else:
        theta.append(theta[i])

plt.scatter(np.linspace(1,nsteps,nsteps),theta)
plt.title("Markov chain")
plt.xlabel("steps")
plt.ylabel("values of the function")

plt.show()
    
plt.hist(theta,bins=10,density=True)
plt.title("Histogram")
plt.show()

"""so obtained distribution matches quite nicely with the uniform distribution between 3 and 7 """