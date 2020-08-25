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
#plot histogram
"""
from skimage import io, img_as_ubyte

img_gray = io.imread('images/test_image.jpg', as_gray=True)
img_gray_8bit = img_as_ubyte(img_gray)

#plt.imshow(img_gray, cmap='gray')
plt.hist(img_gray_8bit.flat,bins=100, range=(0,255) )
"""

#plot line and symbols
"""
a=np.array([1,2,3,4,5])
b=np.array([1,4,9,16,25])
plt.plot(a, b)
plt.plot(a,b,'bo') #blue dots. Also try:'r--' 'g^'
plt.axis([0,6,0,50])
plt.xlabel('x')
plt.ylabel('y')
"""

#various type of plots
"""
wells = ['well1','well2','well3','well4','well5']
cells = [80,62,88,110,90]

fig = plt.figure(figsize=(10,5)) 
plt.bar(wells,cells)
plt.scatter(wells, cells)
plt.plot(wells, cells)
"""

"""
a = np.array([1,2,3,4,5])
b = np.array([1,4,9,16,25])

plt.plot(a, b, lw=5.0)
#use setp() tos define multiple parameters
fig = plt.plot(a,b)
plt.setp(fig, color='r', linewidth=4.0)
plt.show()
"""

#adding labels and annotations
"""
wells = [1,2,3,4,5]
cells = [80,62,88,110,90]

font = {'family': 'serif',
        'name':'Times New Roman',
        #'color':  'darkred',
        'weight': 'normal',
        'size': 16,
        }

plt.figure(figsize=(8,8))

plt.plot(wells,cells)
plt.xlabel('well #', fontdict=font)
plt.ylabel('# dead cells', fontdict=font)
plt.title('Dead cells in each well')
plt.axis(1,6, 60,120)
plt.grid(True)
plt.show()
"""

#plot two figures
"""
x = [1,2,3,4,5]
y = [10,125,1350,11250,100500]

plt.figure(figsize=(12,6),fontsize=20)

#linear
plt.subplot(1,2,1)
plt.plot(x,y)
plt.yscale('linear')
plt.title('linear')
plt.grid(True)

#log
plt.subplot(1,2,2)
plt.plot(x, y)
plt.yscale('log')
plt.title('log')
plt.grid(True)
"""

#multiple plots
wells = ['well1','well2','well3','well4','well5']
cells = [80,62,88,110,90]
#Innitialize the plot and subplots
#Initialize the plot 
fig = plt.figure(figsize=(16,6))
ax1 = fig.add_subplot(1,3,1)
ax1.set(title='vertical bar',xlabel='Well #', ylabel='# dead cells')

ax2 = fig.add_subplot(1,3,2)
ax2.set(title='horizontal bar',xlabel='# dead cells', ylabel='Well #')

ax3 = fig.add_subplot(1,3,3)

#Plot the data
ax1.bar(wells,cells)
ax2.barh(wells,cells)
ax3.plot(wells,cells)

plt.savefig('images/my_plot.jpg')

