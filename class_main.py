#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug  9 09:37:30 2018

@author: apb
"""

class Dog():
    height=20
    col='black'
    def __init__(self,name):
        self.name=name
        print('default fun of Dog called\n')
        
    def bark(self):
        print('bark dear '+self.name+'\n')
        self.height='23'
        self.col='white'
        
"""
when pug(Dog) is used then it means it inherits Dog class

"""
class pug(Dog):
    height='normal'
    def __init__(self,name):
        print('pug class called')
        super().__init__(name)
        self.food=food()  #note the insatnce of food class
        
    def myspec(self):
        self.height='small'

"""
lets create a food class and makes its instance an
attribute of pug class
"""
class food():
    def __init__(self):
        print('food class invoked')
        self.name='biscuits'

mydog=Dog('bull')
print(mydog.name)
print(mydog.height)
mydog.bark()
print(mydog.height)
print(mydog.col)
mypug=pug('sheru')
print(mypug.height)
print('lets overwrite')
mypug.myspec()
print(mypug.height)

mypug.bark()
print(mypug.height)

mypug.myspec()
print(mypug.height)

mypug.food
print(mypug.food.name)

