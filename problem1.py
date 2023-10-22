# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.

Samriddha Kharel 1001918169

"""

import numpy as np
import scipy.linalg as lp1
import sympy

A = np.array([[3, 8, -5], [3, -6, -7], [3, 4, 2]])
B = np.array([-1, -1, 3])
A_sympy = sympy.Matrix(A)

# Computes the reduced row echelon form of A
A_rref, pivots = A_sympy.rref()
A_rref = np.array(A_rref).astype(float)

print("Reduced row echelon form of A:\n",A_rref)

# Finds the column space of A
M_columnspace = np.array(A_sympy.columnspace())
M_columnspace = M_columnspace.T
print("\nColumn space of A:\n",M_columnspace)

# Solves the matrix equation Ax=b
x = lp1.solve(A,B)
print("Solution x for Ax = B:\n",x)

# Computes Nul A
nullA = lp1.null_space(A)
print("\nNull space of A:\n",nullA)

