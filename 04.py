#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 14 19:40:32 2020

@author: atomac
"""

from skimage import io, filters
from matplotlib import pyplot as plt

img = io.imread('/Users/atomac/Documents/Python/image_processing/python_for_microscopists-master/images/Osteosarcoma_01.tif') 
gaussian_img = filters.gaussian(img,sigma=2)

plt.imshow(gaussian_img)