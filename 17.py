#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug 16 19:36:46 2020

@author: atomac
"""

a=10
b=39
c=20

if a>b:
    print('First if statement where a>b')
    if b<c:
        print('Second level statement where b<c')
    elif b>c:
        print('Second level statement where b>c')
elif a<=b:
    print('a is less than b')
