# -*- coding: utf-8 -*-
"""
Created on Fri Aug 21 09:44:19 2020

@author: Hamdani
"""

import numpy as np
from matplotlib import pyplot as plt
"""
x = np.arange(6)
y = np.arange(6,27,4)
y1= x**2

plt.plot(x, y)
plt.plot(x, y1)
"""
from skimage import io, img_as_ubyte

img_gray = io.imread('images/test_image.jpg', as_gray=True)
img_gray_8bit = img_as_ubyte(img_gray)

#plt.imshow(img_gray, cmap='gray')
plt.hist(img_gray_8bit.flat,bins=100, range=(0,255) )