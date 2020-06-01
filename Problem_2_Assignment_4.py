#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Problem 1: Python code to generate 10000 uniformly distributed random numbers between 0 and 1 using numpy.random.rand
Created on Mon Jun  1 20:11:14 2020

@author: krishnendu
"""

import numpy as np
import matplotlib.pyplot as plt

random_numbers=np.random.rand(10000)

plt.hist(random_numbers,bins=10,density=True)
plt.title("Histogram")
plt.show()
