#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug  7 22:35:31 2018

@author: apb
"""

print("welcome to my firt prog")
######################################
print('######################################')
mylist=['sham','78','sundar']
######################################
print('######################################')
for name in mylist:
    print(name+str(10))

print('after for loop')    
######################################
print('######################################')
mylist[1]='abhi'
######################################
print('######################################')
del mylist[2]
######################################
print('######################################')
for x in range(2,6):
    print(x**2)

######################################
print('######################################')

cool=[x*2 for x in range(3,6)]

######################################
print('######################################')
      
game=cool[1:2]
print(game)
