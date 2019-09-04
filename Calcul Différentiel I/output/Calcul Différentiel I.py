"""
>>> from numpy import *

>>> x = array([1, 2, 3])
>>> x.ndim
1
>>> shape(x)
(3,)
>>> size(x)
3

>>> 2 * x
array([2, 4, 6])

>>> A = array([[1, 2, 3], [4, 5, 6]])
>>> A
array([[1, 2, 3],
       [4, 5, 6]])
>>> A.ndim
2
>>> shape(A)
(2, 3)
>>> size(A)
6

>>> A
array([[1, 2, 3],
       [4, 5, 6]])
>>> a = reshape(A, (6,))
>>> a
array([1, 2, 3, 4, 5, 6])
>>> reshape(a, (2, 3))
array([[1, 2, 3],
       [4, 5, 6]])

>>> A = array([[1, 2, 3], [4, 5, 6]])
>>> B = array([[1, 0, 0], [0, 1, 0], [0, 0, 1]])
>>> A.dot(B)
array([[1, 2, 3],
       [4, 5, 6]])

>>> A
array([[1, 2, 3],
       [4, 5, 6]])
>>> transpose(A)
array([[1, 4],
       [2, 5],
       [3, 6]])

>>> A = array([[1, 2, 3], [4, 5, 6]])
>>> x = array([7, 8, 9])
>>> A.dot(x)
array([ 50, 122])
"""

