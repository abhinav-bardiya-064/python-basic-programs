#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug 12 08:29:19 2018

@author: apb
"""
import numpy as np

b=np.array([[1,2,3],[3.4,5.6,3.2]],dtype=np.int16)
print(b)

print(len(b))
print(b.size)
print(b.shape)
print(b.ndim)

"""
let see what happens if the dimension are 3 or more
"""
c=np.array([[[[1,3,2],[3,4,6]]],[[[2.3,4.3,5.4],[23.3,43.4,54.6]]]],dtype=np.int64)
print(c)

print(len(c))
print(c.size)
print(c.shape)   # most important
print(c.ndim)   # most important 

"""
print(c.shape) will give me what kind of matricies i have
and print(c.ndim) will give me the no of dimensions present.

"""

""" convert into another format/datatype """

d=b.astype(str);
print(d)

