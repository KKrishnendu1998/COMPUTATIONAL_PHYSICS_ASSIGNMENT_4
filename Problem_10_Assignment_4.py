#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Problem 10: Probabilistic Inference

@author: krishnendu
"""

import numpy as np
import matplotlib.pyplot as plt
import emcee
import corner

x=np.loadtxt("Problem_10.txt",usecols=1,delimiter="&")
y=np.loadtxt("Problem_10.txt",usecols=2,delimiter="&")
yerr=np.loadtxt("Problem_10.txt",usecols=3,delimiter="&")


def log_likelihood(theta, x, y, yerr):
         a, b , c= theta
         model = a*x**2+b*x+c
         sigma2 = yerr**2
         # actually negative ln L
         return 0.5 * np.sum((y - model) ** 2 / sigma2 +
         np.log(2 * np.pi * sigma2))


def log_prior(theta):
    a , b , c = theta
    if -500.0 < a < 500 and 0.0 < b < 1000.0 and -100 < c < 100 :
      return 0.0
    return -np.inf


def log_probability(theta, x, y, yerr):
    lp = log_prior(theta)
    if not np.isfinite(lp):
      return -np.inf
    return lp - log_likelihood(theta, x, y, yerr)

from scipy.optimize import minimize

guess = (1.0,1.0,1.0)
soln = minimize(log_likelihood,guess,args=(x, y, yerr))



nwalkers, ndim = 50, 3
pos = soln.x + 1e-4 * np.random.randn(nwalkers, ndim)


sampler = emcee.EnsembleSampler(nwalkers,
ndim,
log_probability,
args=(x, y, yerr))
sampler.run_mcmc(pos, 4000)

samples = sampler.get_chain()

#plot of Markov chain
fig=plt.figure(constrained_layout=True)
spec=fig.add_gridspec(3,3)
plt.suptitle("Markov chain")

plt1=fig.add_subplot(spec[0,:])
plt1.plot(samples[:, :, 0]) # a values
plt1.set_xlabel("step number")
plt1.set_ylabel("a")


plt2=fig.add_subplot(spec[1,:])
plt2.plot(samples[:, :, 1]) # b values
plt2.set_xlabel("step number")
plt2.set_ylabel("b")


plt3=fig.add_subplot(spec[2,:])
plt3.plot(samples[:, :, 2]) # c values
plt3.set_xlabel("step number")
plt3.set_ylabel("c")
plt.show()


medians = np.median(samples, axis=0)

a_true, b_true, c_true =np.average(medians,axis=0)     #computing the the value of the parameters by averaging over the 50 chains

data=np.zeros([4000*50,3])

for i in range(3):
    data[:,i]=np.hstack(samples[:,:,i]) 
    
#corner plot   
    
fig = corner.corner(samples.reshape(40*5000,3),labels=["a","b","c"],quantiles=[0.16,0.5,0.84],truths=[a_true, b_true,c_true],show_titles=True)
plt.show()

X=np.linspace(0,300,1000)

for i in range(200):
    r=np.random.randint(0,high=4000*50)
    a=data[r,0]
    b=data[r,1]
    c=data[r,2]
    plt.plot(X,a*X**2+b*X+c)

x=np.sort(x)    
plt.plot(X,a_true*X**2+b_true*X+c_true)
plt.errorbar(x,y,yerr=yerr,fmt="ro")
plt.xlabel("x")
plt.ylabel("y")
plt.title("plot of data with curve fit")
plt.show()