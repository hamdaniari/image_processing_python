# -*- coding: utf-8 -*-
"""
Created on Thu Aug 20 09:50:01 2020

@author: Hamdani
"""

from skimage import io, filters, img_as_ubyte
from matplotlib import pyplot as plt

img = io.imread('images/Osteosarcoma_01.tif')

gaussian_img = filters.gaussian(img,sigma=3)

io.imsave('images/exported/Osteosarcoma_gaussian.jpg',gaussian_img) #no probelem when saving in jpg format

#when saving in the .tif format, the images must be converted from float64 to unint8
gaussian_img_8bit = img_as_ubyte(gaussian_img)

io.imsave('images/exported/Osteosarcoma_gaussian.tif',gaussian_img_8bit)

################################
import cv2
cv2.imwrite('images/exported/Osteosarcoma_gaussian.tif',gaussian_img_8bit)
################################

plt.imsave('images/exported/Osteosarcoma_gaussian_saved_using_pyplot.jpg',gaussian_img_8bit)