#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 15 12:42:58 2020

@author: atomac
"""

from skimage import io
im2=io.imread('Osteosarcoma_01.tif')
io.imshow(im2)

import cv2
img2 = cv2.imread('Osteosarcoma_01.tif')


import numpy as np
a=np.ones((5,5))

import pandas as pd
df=pd.read_csv('other_files/image_measurements.csv')  
print(df.head())  

from matplotlib import pyplot as plt
plt.imshow(im2)