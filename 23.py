# -*- coding: utf-8 -*-
"""
Created on Thu Aug 20 09:26:33 2020

@author: Hamdani
"""

from skimage import io
img_color = io.imread('images/Osteosarcoma_01.tif')
img = io.imread('images/Osteosarcoma_01.tif', as_gray=True)
io.imshow(img_color)
io.imshow(img)
