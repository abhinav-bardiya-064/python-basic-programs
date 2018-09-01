#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 15 10:04:05 2018

@author: apb
"""
"""
remember to import matplotlib  - > pyplot 

Here in first example the order of points is important

"""
import matplotlib.pyplot as plt
import numpy as np
x=[3,8,2,7]
y=[1,2,1,0]
plt.plot(x,y)
plt.show()
"""
rem s=2 is the width of line 

"""
print('lets see scater ploting')

x=list(range(10,100))
y=[i**2 for i in x]
plt.scatter(x,y,s=1)
plt.show()
"""
look how the combination worked , combined scatter and plot
"""
print('lets see customized ploting')
year=[1,2,3,4,5]
pop=[250,360,888, 1099, 2550]
plt.scatter(year,pop)
plt.plot(year,pop)
plt.title('Population growth',fontsize=20)
plt.xlabel('no of years in 2000')
plt.ylabel('no of citizens',fontsize=10)
plt.tick_params(axis='both', which='major',labelsize=9)
plt.show()

"""
look how to adjust axis
"""
print('adjust axis')
year=[1,2,3,4,5]
pop=[250,360,888, 1099, 2550]
plt.scatter(year,pop)
plt.plot(year,pop)
plt.title('Population growth',fontsize=20)
plt.xlabel('no of years in 2000')
plt.ylabel('no of citizens',fontsize=10)
plt.tick_params(axis='both', which='major',labelsize=9)
plt.axis([1,5,100,3000]) # remember this must be list
plt.show()

"""
look how to adjust clouring
note: The c=pop stands for vary color with changes in POP
and cmap= color variation

"""
print('adjust colouring of points')
year=[1,2,3,4,5,8,6,9]
print(year)
year=np.array([1,2,3,4,5,8,6,9],dtype=np.int16)
print(year)
pop=np.array([250,360,888, 1099, 2550,3500,2050,5000])
year_m=year.mean()
pop_m=pop.mean()
plt.scatter(year_m,pop_m,s=25,cmap=plt.cm.Blues,c='red')
plt.scatter(year,pop,c=year,s=20,cmap=plt.cm.Blues)
plt.scatter(year[0],pop[0],c='black',s=30)
plt.scatter(year[-1],pop[-1],c='orange',s=30)
#plt.scatter(year,pop,c='red',s=20,cmap=plt.cm.Blues)
plt.plot(year,pop)
plt.title('Population growth',fontsize=20)
plt.xlabel('no of years in 2000')
plt.ylabel('no of citizens',fontsize=10)
plt.show()

"""
lets try hiding the axises

important note the below method

"""
print('lets try hiding the axises')

plt.scatter(year,pop)
plt.axes().get_xaxis().set_visible(False)
plt.plot()

"""
now to increase the size of plot and dpi setting and save the plot
note: first scale the plotting canvas then plot something :P else you wont
see anything
"""
plt.figure(figsize=(5,5))
plt.scatter(year,pop)
plt.plot()
plt.savefig('myplot.png',bbox_inches='tight')
plt.savefig('myplot2.png')



