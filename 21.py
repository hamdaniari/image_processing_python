# -*- coding: utf-8 -*-
"""
Created on Tue Aug 18 15:32:47 2020

@author: Hamdani
"""

"""
def squared(x):
    return x**2
print(squared(2))

a = lambda b: b**2
print(a(5))

c = lambda d:d/10
print(c(35))

k = lambda i,j,dummy=0: 2*i + 3*j
print(k(2,2)) 
"""

def distance_eqn(u,a):
     return lambda t: u*t + (0.5*a*t**2)

#1st way of implementing
dist = distance_eqn(5, 10) #Create a dist object/function
print(dist(20))

#2nd way of implementing
print(distance_eqn(5, 10)(20))

time=[]
dist=[]

for t in range(0, 22,2):
    d = distance_eqn(5, 10)(t)
    time.append(t)
    dist.append(d)
from matplotlib import pyplot as plt
plt.plot(time,dist)
plt.xlabel('time')
plt.ylabel('distance')