#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 11 17:53:52 2018

@author: apb
"""

import numpy as nm

a=nm.ones((2,3,4),dtype=nm.int16)
print(a)
# one dimensional array
b=nm.array([1,3,5],dtype=None)

# two dimensional array
c=nm.array([[2.5,6.4,3.4],[3.5,6.6,8.8]],dtype=nm.float)
print(c)
# three dimensional array
d=nm.array([[[1.2,2.3]],[[32.23,3.2]]],dtype=nm.float)
print(d)
"""
three dimensional array with multiple rows
d=nm.array([[[1.2,2.3],[2.3,23.3,23.1]],[[32.23,3.2],[2,42,12]]],dtype=nm.float)
note above as given error because the design was not appropriate , it wont initialize
"""
e=nm.array([[[1.2,2.3,3.4],[2.3,23.3,23.1]],[[32.23,3.2,3.4],[2,42,12]]],dtype=nm.float)
print(e)

print(c)
print(sum(c))

print(sum(c,2))

""" h i this is a 
multiline
comment """

print('cool')

""" 
****************************************************************
now see how to genearte varity of matrices
****************************************************************
""" 

f=nm.zeros((2,3))
print(f)

g=nm.ones((2,3),dtype=nm.int32)
print(g)
"""the first one is tart, second is upto what, third one is step size"""
h=nm.arange(10,100,5)
print(h)
""" see here goes the third parameter as no of varibles you want """
i=nm.linspace(10,100,4)
print(i)

j=nm.full((2,3),'*')
print(j)

k=nm.eye(3)
print(k)

k=nm.eye(4,2)
print(k)

l=nm.random.random((2,4))
print(l)
"""
no of operations on file saving and closing.
"""
nm.save('myrandom.txt',l)
nm.savetxt('savetxt.txt',l)
nm.savez('savez',l,a)

z=nm.loadtxt('savetxt.txt')
print(z)









