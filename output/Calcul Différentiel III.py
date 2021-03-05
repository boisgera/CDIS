"""
>>> import autograd as ag
>>> from autograd import numpy as np
>>> 
>>> def grad(f):
...     def grad_f(*x):
...         n = len(x)
...         return np.array([ag.grad(f, i)(*x) for i in range(n)])
...     return grad_f
>>> 
>>> def J(f):
...     def J_f(*x):
...         n = len(x)
...         di_f_x = [ag.jacobian(f, i)(*x) for i in range(n)]
...         return np.array(di_f_x).T
...     return J_f

>>> def H(f):
...     return J(grad(f))

>>> def f(x1, x2):
...     return np.exp(-0.5 * (x1 * x1 + x2 * x2))

>>> H_f = H(f)
>>> H_f(1.0, 2.0)
array([[0.      , 0.16417 ],
       [0.16417 , 0.246255]])

>>> T0 = np.array(1.0)
>>> T1 = np.array([1.0, 2.0, 3.0])
>>> T2 = np.array([[1.0, 2.0, 3.0], [4.0, 5.0, 6.0]])
>>> T3 = np.array([[[1.0], [2.0], [3.0]], [[4.0], [5.0], [6.0]]])

>>> (T0.ndim, T1.ndim, T2.ndim, T3.ndim)
(0, 1, 2, 3)

>>> T0.shape
()
>>> T1.shape
(3,)
>>> T2.shape
(2, 3)
>>> T3.shape
(2, 3, 1)

>>> T0[()]
1.0
>>> T0[]
Traceback (most recent call last):
...
SyntaxError: invalid syntax

>>> T1[1]
2.0
>>> T2[1,2]
6.0
>>> T3[1,2,0]
6.0

>>> x = np.array([0.0, 1.0])
>>> y = np.array([2.0, 4.0])
>>> A = np.array([[1.0, 2.0], [3.0, 4.0]])
>>> B = np.array([[5.0, 6.0], [7.0, 8.0]])
>>> T = np.array([[[1.0, 2.0], [3.0, 4.0]], 
...               [[5.0, 6.0], [7.0, 8.0]]])

>>> x.dot(y)
4.0
>>> A.dot(x)
array([2., 4.])
>>> A.dot(B)
array([[19., 22.],
       [43., 50.]])
>>> T.dot(A)
array([[[ 7., 10.],
        [15., 22.]],
<BLANKLINE>
       [[23., 34.],
        [31., 46.]]])

>>> x.dot(T) # Not what we expect here!
array([[3., 4.],
       [7., 8.]])

>>> def dot(A, B): # Let's define our own tensor product
...     return np.tensordot(A, B, axes=1)           
>>> dot(x, T) # Problem solved!
array([[5., 6.],
       [7., 8.]])

>>> np.einsum("i, ijk -> jk", x, T)
array([[5., 6.],
       [7., 8.]])

>>> np.einsum("i, jik -> jk", x, T)
array([[3., 4.],
       [7., 8.]])
"""
import autograd as ag
from autograd import numpy as np

def grad(f):
    def grad_f(*x):
        n = len(x)
        return np.array([ag.grad(f, i)(*x) for i in range(n)])
    return grad_f

def J(f):
    def J_f(*x):
        n = len(x)
        di_f_x = [ag.jacobian(f, i)(*x) for i in range(n)]
        return np.array(di_f_x).T
    return J_f

def H(f):
    return J(grad(f))

def f(x1, x2):
    return np.exp(-0.5 * (x1 * x1 + x2 * x2))
