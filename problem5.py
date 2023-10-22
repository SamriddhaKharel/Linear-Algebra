# -*- coding: utf-8 -*-
"""
Created on Wed May  3 18:51:30 2023

@author: samdm
"""

import numpy as np
import matplotlib.pyplot as plt

plt.style.use('ggplot')

dataset =np.loadtxt('dataset2-1.txt')

x = dataset[:,0]
y = dataset[:,1]

a = np.vstack([x, np.ones(len(x))]).T
m, c = np.linalg.lstsq(a,y,rcond=None)[0]

plt.scatter(x,y)
plt.plot(x,m * x + c,color='b')
plt.xlabel('x')
plt.ylabel('y')
plt.show()
