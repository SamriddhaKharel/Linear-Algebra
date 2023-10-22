# -*- coding: utf-8 -*-
"""
Created on Wed May  3 18:53:22 2023

@author: samdm
"""

import numpy as np
import matplotlib.pyplot as plt

A = np.array([[1,-2],[-4,1]])

eigenvalues, eigenvectors = np.linalg.eig(A)

Abasis1 = np.array([1,0])
Abasis2 = np.array([-4,-7])

e1 = np.array([1,0])
e2 = np.array([0,1])

# Plotting basis vectors and matrix A
plt.quiver([0,0],[0,0],[e1[0],e2[0]],[e1[1], e2[1]],angles='xy',scale_units='xy',scale=1,color=['m','m'],label=['e1','e2'])
plt.quiver([0,0],[0, 0],A[0, :], A[1, :],angles='xy',scale_units='xy',scale=1,color=['c','c'],label=['a1','a2'])

# Plotting eigenvectors of A
plt.quiver([0,0],[0,0],eigenvectors[:,0], eigenvectors[:,1], angles='xy',scale_units='xy',scale=1,color=['y','y'],label=['v1','v2'])

plt.xlabel('x')
plt.ylabel('y')
plt.xlim([-5,5])
plt.ylim([-8,4])
plt.title('Basis Vectors and Matrix A')
plt.legend()
plt.show()

# Print eigenvalues and eigenvectors of A
print("\nEigenvalues:\n{}\n".format(eigenvalues))
print("Eigenvectors:\n{}".format(eigenvectors))
