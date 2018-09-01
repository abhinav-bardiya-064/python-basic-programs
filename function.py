#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug  9 09:34:14 2018

@author: apb
"""
print('-----------------------------------------------')

def cool():
    print('hi man how you doing! ')
    
def cool_again(name='abhi'):
    print('collest person on earth is: '+name)

print('my prog begins')

cool()
cool_again('sambu')
cool_again()

print('-----------------------------------------------')
"""
lets try with mix of position & keyword argument
"""

def drink(time,value='water'):
    print('hi the time is: '+time)
    print('The value is: '+value)

drink('10AM','sharbat')
drink('9AM',)
drink('7AM')
drink('6pm',value='Lassi')
print('-----------------------------------------------')
"""
lets try with mix of position & keyword argument part 2
"""
def drink(time,value='water',quantity='1 ltr'):
    print('hi the time is: '+time)
    print('The value is: '+quantity)
    #print('The value is: '+value+' '+quantity)
    mydic={'time:':time,'value':value,'quatn':quantity}
    return mydic


drink('10AM','sharbat')
"""
drink('9AM',,'2 ltr') #note its not leting the work fonulvaluel r 
"""
drink('7AM')
see_dict=drink('6pm',None,quantity='3 ltr')
print(see_dict)
print('-----------------------------------------------')
"""

"""
print('-----------------------------------------------')
"""
lets try with call by refrence
a example of list which will get modified nad which won't modify
"""
def xchng(arg1,arg2):
    while arg1:
        name=arg1.pop()
        print('operate on '+name)
        arg2.append(name)
        
        
    
lista=['abhi','jain','shyam']
listb=[]
xchng(lista,listb)
print(lista)
print(listb)

print('-----------------------------------------------')
"""
lets try with call by value
a example of list which will get modified nad which won't modify
"""
def xchng(arg1,arg2):
    while arg1:
        name=arg1.pop()
        print('operate on '+name)
        arg2.append(name)
        
        
    
lista=['abhi','jain','shyam']
listb=[]
xchng(lista[:],listb)
print(lista)
print(listb)
