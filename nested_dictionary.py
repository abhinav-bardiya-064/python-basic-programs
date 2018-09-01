#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 10 13:36:42 2018

@author: apb
"""

users=[]

u1={
    'name':'abhi',
    'sex':'male',
    'age':'25'    
    }

u2={
    'name':'robot',
    'sex':'NA',
    'age':'20'    
    }
users.append(u1)
users.append(u2)

print(users)

for us in users:
    for k,v in us.items():
        print(k+' '+v)
    print('---------------------')


user_style2= [
     {
      'name':'abhi',
      'sex':'male',
      'age':'25'    
     },
     {
      'name':'robot',
      'sex':'NA',
      'age':'20'    
     }
 
]

print()

# now in dictionary we will have list
print('now in dictionary we will have list')
users={
      'name':['abhi','mohan'],
      'address':['pune','ratlam']      
      }
print(users)

for k,v in users.items():
    print(k)
    for data in v:
        print(data)
        
        
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    

