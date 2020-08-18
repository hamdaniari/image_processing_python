# -*- coding: utf-8 -*-
"""
Created on Tue Aug 18 17:24:16 2020

@author: Hamdani
"""


from skimage import io, img_as_float, img_as_ubyte

img = io.imread('images/Osteosarcoma_01.tif')
print(img.shape) #y, x, c

img2 = img_as_float(img)

img3 = img/255

img_8bit = img_as_ubyte(img2)