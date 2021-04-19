# -*- coding: utf-8 -*-
"""
Created on Mon Jun 24 05:35:32 2019

@author: Sanvi
"""

"""We can create matrix using the matrix() method from numpy array or input data 

"""
import numpy as np
arr =np.array([[1,2,3],[4,5,6],[6,7,9]])
mat1q =np.matrix(arr)
print(mat1q)
print(type(mat1q))

"""
First we need to pass string as an input 
Each element is separated by space
Each row is separated by semicolon

"""
mat2 = np.matrix('1 2 3;4 5 6;6 7 8')

"""
Matrix Operations 


"""
print(mat2 + mat1q)
print(mat2 * mat1q)
print(mat2.diagonal())
print(mat2.max())
print(mat2.sum())
print(mat2.size)

mat3 = np.matrix('3 5;6 7')
mat2*mat3
"""
ValueError: shapes (3,3) and (2,2) not aligned: 3 (dim 1) != 2 (dim 0)
"""
"""
We need to matrix multiplication manually
"""