#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 15 11:04:42 2018

@author: apb
"""

import numpy as np
import matplotlib.pyplot as plt

data=np.loadtxt('ex1data1.txt',delimiter=',')
X=data[:,0]
Y=data[:,1]
plt.figure(figsize=(10,10))
plt.scatter(X,Y,s=44,marker='x',c=X)
plt.plot(X,Y,s=10)
plt.show();