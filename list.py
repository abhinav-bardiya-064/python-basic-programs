#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 10 11:01:02 2018

@author: apb
"""

books=[]
books.append('c++')
books.append('java')
print(books)
books.reverse()
print(books)
books.insert(2,'new one')
print(books)

# del any book by index
del books[1]
print(books)

#remove books by name
books.remove('new one')
print(books)

books.append('circus')
books.append('alive')
books.append('fiction')
books.append('java')
print(books)
del books[-1]
print('pop normal: '+books.pop()) # remember last one bigger index
print('pop normal: '+books.pop(0)) # remember first one 
print(books)

# lets see how sorting works
books.append('circle')
books.append('home alone')
books.append('harry poter')
books.append('win win')
books.sort();               # sorted in ascending order
print(books)
books.sort(reverse=True);   # sorted in descending order
print(books)

# finding the length of no of books
print(len(books))


if ('circle' in books):
    print('still there')

if ('cir' in books):
    print('still there')
else:
    print('book not found')
