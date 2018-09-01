#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 10 11:43:19 2018

@author: apb
"""

#
# this is second part of list which dealss with range , slicing, copying.. etc 
#

courses=['ml','num py','pandas','sci-kit','pandas','pygal','matploit']
print(courses)

for number in range(3,6):
    print(courses[number])

for number in range(25):
    print(number)
    
# lets create a list dynamically
print(list(range(3,9))) # note range(3,9) just printed as it is

age_dist=[23,45,56,4,32,54,67,87,98]

print('min age: '+str(min(age_dist)))
print('max age: '+str(max(age_dist)))
print('sum age: '+str(sum(age_dist)))
print('avg age: '+str(sum(age_dist)/len(age_dist)))

# lets learning slicing of list
new_list=age_dist[2:6]   # note 6 pos wont come as always -1 is taken into account
print(new_list)

# tackling with list comprehensions

squares=[x**2 for x in range(1,11)]
print(squares)

print(courses)
# use of uppercase function
courses_u=[name.upper() for name in courses]
print(courses_u)