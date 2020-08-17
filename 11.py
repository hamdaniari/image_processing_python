#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 15 15:02:47 2020

@author: atomac
"""

m=int(input('Provide mass in kg: '))
c=300000000 #m/s

E=m*(c**2)
print('Energy is: {:.2E}'.format(E))