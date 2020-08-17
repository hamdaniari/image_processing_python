# -*- coding: utf-8 -*-
"""
Created on Mon Aug 17 09:44:21 2020

@author: Hamdani
"""

"""
def my_function(name='default_name'):
    print('your name is: ', name)

my_function()
my_function('Ari')
my_function('John')
my_function(4121)
"""

"""
def my_microcope(mic):
    for x in mic:
        print(x)
        
mic = ['AxioImager','Elyra','LSM','Versa']

my_microcope(mic)
"""

from skimage import io,filters
from matplotlib import pyplot as plt

def gaussian_of_img(img,sigma=1):
    gaussian_img=filters.gaussian(img,sigma)
    return(gaussian_img)

my_image=io.imread('images/Osteosarcoma_01.tif')
filtered_img = gaussian_of_img(my_image,3)

plt.imshow(filtered_img)