# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np

A = np.array([[1, 0, 4],[-2, 3, -2],[-2, 0, 6]])

m, n =A.shape
rank =np.linalg.matrix_rank(A)

if rank < n:
    print(f"Matrix rank {rank} is smaller than the number of columns {n}")

Q = np.zeros((m, n))

for i in range(n):
    column = A[:, i]
    Q[:, i] = column

    for j in range(i):
        prev = Q[:, j]
        Q[:, i] -=(prev @ column) / (prev @ prev) * prev

    Q[:, i] /= np.linalg.norm(Q[:, i])

R = Q.T @ A

print('  Matrix A:\n', A)
print('\nThe QR Factorization:')
print('Q:\n', Q)
print('R:\n', R)
