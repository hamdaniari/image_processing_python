#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug 16 12:53:14 2020

@author: atomac
"""

import numpy as np

a=np.array([1,2,3,4,5])
b=np.array([[6,7,8,9],[4,5,6,7]])
c=np.array([10,11,12,13,14])
d=np.array([[6,7,8,9],[4,5,6,7]],dtype=np.float64) #no need to change the data type
e=b/2
f=d/2

from skimage import io

"""
img1=io.imread('images/Osteosarcoma_01.tif')
print(type(img1))
img2=img1/2
io.imshow(img2)
io.imshow(img1)
"""

g=np.ones((3,3))
#h=np.ones_like(img1)

i=np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12]])
print(np.shape(i))

j=i[:2]
k=i[:2,1:3]
t=i.T
