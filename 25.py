# -*- coding: utf-8 -*-
"""
Created on Fri Aug 21 08:57:48 2020

@author: Hamdani
"""

from skimage import io,img_as_ubyte
img = io.imread('images/Osteosarcoma_01.tif')
io.imshow(img)

##################
from matplotlib import pyplot as plt
#plt.imshow(img)

plt.imshow(img, cmap='hot')

img_gray = io.imread('images/Osteosarcoma_01.tif', as_gray=True)
img_gray_8bit = img_as_ubyte(img_gray)

#Plot images one by one
"""
plt.imshow(img_gray)
plt.imshow(img_gray,cmap='hot')
plt.imshow(img_gray,cmap='jet')
plt.imshow(img_gray,cmap='Blues')
"""
#Multiplle plots using pyplot

fig = plt.figure(figsize=(10,10))

ax1 = fig.add_subplot(2,2,1)
ax1.imshow(img_gray_8bit,cmap='hot')
ax1.title.set_text('1st=hot')

ax2 = fig.add_subplot(2,2,2)
ax2.imshow(img_gray_8bit,cmap='jet')
ax2.title.set_text('2nd=jet')

ax3 = fig.add_subplot(2,2,3)
ax3.imshow(img_gray_8bit,cmap='gray')
ax3.title.set_text('3rd=gray')

ax4 = fig.add_subplot(2,2,4)
ax4.imshow(img_gray_8bit,cmap='nipy_spectral')
ax4.title.set_text('4th=nipy_spectral')