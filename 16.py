#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug 16 18:27:34 2020

@author: atomac
"""

from skimage import io, img_as_float
img=io.imread('images/Osteosarcoma_01.tif')
img2=img_as_float(img)