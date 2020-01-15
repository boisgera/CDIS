"""
>>> from numpy import inf
>>> from numpy.linalg import norm
>>> A = [[1.0, 2.0], [3.0, 4.0]]
>>> norm(A)
5.477225575051661
>>> norm(A, 1)
6.0
>>> norm(A, 2)
5.464985704219043
>>> norm(A, inf)
7.0
"""

