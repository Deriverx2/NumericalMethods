# -*- coding: utf-8 -*-
"""Gauss_elimination

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1bxOcCoSaCu64SwTEcRR8uA6R1fMirNgl
"""

import numpy as np

def gauss_elimination(A, b):
    n = len(b)
    # Forward Elimination
    for k in range(n-1):
        for i in range(k+1, n):
            if A[i,k] == 0:
                continue
            factor = A[i,k] / A[k,k]
            for j in range(k, n):
                A[i,j] = A[i,j] - factor * A[k,j]
            b[i] = b[i] - factor * b[k]

    # Back Substitution
    x = np.zeros(n)
    x[-1] = b[-1] / A[-1,-1]
    for i in range(n-2, -1, -1):
        sum_ax = 0
        for j in range(i+1, n):
            sum_ax += A[i,j] * x[j]
        x[i] = (b[i] - sum_ax) / A[i,i]

    return x

if __name__=="__main__":
  A = np.array([[4, 2, 3],
                [2, 2, 1],
                [1, 1, 1]], dtype=float)
  b = np.array([4, 6, 0], dtype=float)

  solution = gauss_elimination(A, b)
  print("Solution:", solution)