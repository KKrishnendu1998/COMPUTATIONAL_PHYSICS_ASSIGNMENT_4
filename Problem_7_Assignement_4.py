#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Problem 7 :chi-square test
    
Created on Sat May 30 15:38:34 2020

@author: krishnendu
"""

import scipy.stats
import numpy as np

obs_count1=np.array([4,10,10,13,20,18,18,11,13,14,13])
obs_count2=np.array([3,7,11,15,19,24,21,17,13,9,5])


exp_count=np.array([4,8,12,16,20,24,20,16,12,8,4])

V1=sum((obs_count1-exp_count)**2/exp_count)

V2=sum((obs_count2-exp_count)**2/exp_count)

percentage1=100*(1-scipy.stats.chi2.cdf(V1,10))

percentage2=100*(1-scipy.stats.chi2.cdf(V2,10))


print("Probability P(V>v) for the first data :",percentage1)

print("Probability P(V>v) for the first data :",percentage2)

print("Both the data are not sufficiently random")

""" So both tha data are not sufficiently random """