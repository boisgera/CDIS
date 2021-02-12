"""
>>> from numpy import *

>>> pi
3.141592653589793

>>> number = eval("3.141592653589793") 
>>> number == pi 
True

>>> def print_exact_number(number):
...     print(f"{number:.100g}")    
>>> print_exact_number(pi)
3.141592653589793115997963468544185161590576171875

>>> import mpmath
>>> mpmath.mp.dps = 49; mpmath.mp.pretty = True
>>> +mpmath.pi
3.141592653589793238462643383279502884197169399375

>>> after_one = nextafter(1.0, +inf)
>>> after_one
1.0000000000000002
>>> print_exact_number(after_one)
1.0000000000000002220446049250313080847263336181640625
>>> eps = after_one - 1.0
>>> print_exact_number(eps)
2.220446049250313080847263336181640625e-16

>>> print_exact_number(finfo(float64).eps)
2.220446049250313080847263336181640625e-16

>>> print_exact_number(2**(-52))
2.220446049250313080847263336181640625e-16

>>> 0.3
0.3

>>> 0.1 + 0.2
0.30000000000000004

>>> def f(x):
...     y = exp(-2.0 * x)
...     u = 1.0 - y
...     v = 1.0 + y
...     w = u / v
...     return w

>>> def g(x):
...     y = exp(-2.0 * x)
...     u = 1.0 - y
...     v = 1.0 + y
...     w = u / v
...     dx = 1.0
...     dy = -2.0 * exp(-2.0 * x) * dx
...     du = 0.0 - dy
...     dv = 0.0 + dy
...     dw = du / v + u * (- dv) / (v * v)  
...     return dw

>>> import autograd
>>> from autograd.numpy import *

>>> def f(x):
...     y = exp(-2.0 * x)
...     return (1.0 - y) / (1.0 + y)
>>> deriv_f = autograd.grad(f)  
>>> deriv_f(1.0)
0.419974341614026

>>> def f(x, y):
...     return sin(x) + 2.0 * sin(y)
>>> def grad_f(x, y):
...     g = autograd.grad
...     return array([g(f, 0)(x, y), g(f, 1)(x, y)])
>>> grad_f(0.0, 0.0)
array([1., 2.])

>>> def f(x, y):
...     return array([1.0 * x + 2.0 * y, 3.0 * x + 4.0 * y])
>>> def J_f(x, y):
...     j = autograd.jacobian
...     return array([j(f, 0)(x, y), j(f, 1)(x, y)]).T
>>> J_f(0.0, 0.0)
array([[1., 2.],
       [3., 4.]])

>>> def FD(f, x, h):
...     return (f(x + h) - f(x)) / h

>>> FD(exp, 0, 1e-4)
1.000050001667141
>>> FD(exp, 0, 1e-8)
0.999999993922529
>>> FD(exp, 0, 1e-12)
1.000088900582341

>>> def CD(f, x, h):
...     return 0.5 * (f(x + h) - f(x - h)) / h

>>> def add(x, y):
...     return x + y

>>> add(1.0, 2.0)
3.0

>>> add(1, 2)
3
>>> add(array([1.0, 1.0]), array([2.0, 2.0]))
array([3., 3.])
>>> add("un", "deux")
'undeux'

>>> from dis import dis
>>> dis(add)
  2           0 LOAD_FAST                0 (x)
              2 LOAD_FAST                1 (y)
              4 BINARY_ADD
              6 RETURN_VALUE

>>> class Float(float):
...     def __add__(self, other):
...         print(f"trace: {self} + {other}")
...         return super().__add__(other)

>>> x = Float(2.0) + 1.0
trace: 2.0 + 1.0
>>> x
3.0

>>> class Float(float):
...     def __add__(self, other):
...         print(f"trace: {self} + {other}")
...         return Float(super().__add__(other))

>>> import math

>>> def cos(x):
...     print(f"trace: cos({x})")
...     return Float(math.cos(x))

>>> cos(pi) + 1.0
trace: cos(3.141592653589793)
trace: -1.0 + 1.0
0.0

>>> 1.0 + cos(pi)
trace: cos(3.141592653589793)
0.0

>>> class Node:
...     def __init__(self, value):
...         self.value = value

>>> class Node:
...     def __init__(self, value, function=None, *args):
...         self.value = value
...         self.function = function
...         self.args = args

>>> def cos(x):
...     if isinstance(x, Node):
...         cos_x_value = math.cos(x.value)
...         cos_x = Node(cos_x_value, cos, x)
...         return cos_x
...     else:
...         return math.cos(x) 

>>> def add(x, y):
...     if isinstance(x, Node) or isinstance(y, Node):
...         if not isinstance(x, Node):
...             x = Node(x)
...         if not isinstance(y, Node):
...             y = Node(y)
...         add_x_y_value = x.value + y.value
...         return Node(add_x_y_value, add, x, y)
...     else:
...         return x + y

>>> Node.__add__ = add
>>> Node.__radd__ = add

>>> def autodiff(function):
...     def autodiff_function(*args):
...         if any([isinstance(arg, Node) for arg in args]):
...             node_args = []
...             values = []
...             for arg in args:
...                 if isinstance(arg, Node):
...                     node_args.append(arg)
...                     values.append(arg.value)
...                 else:
...                     node_args.append(Node(arg)) 
...                     values.append(arg)
...             output_value = function(*values)
...             output_node = Node(
...                output_value, autodiff_function, *node_args
...             )
...             return output_node
...         else:
...             return function(*args)        
...     autodiff_function.__qualname__ = function.__qualname__
...     return autodiff_function

>>> sin = autodiff(math.sin)

>>> def multiply(x, y):
...     return x * y
>>> multiply = autodiff(multiply)
>>> Node.__mul__ = Node.__rmul__ = multiply

>>> def trace(f, args):
...     args = [Node(arg) for arg in args]
...     end_node = f(*args)
...     return end_node

>>> def node_str(node):
...     if node.function is None:
...         return str(node.value)
...     else:
...         function_name = node.function.__qualname__
...         args_str = ", ".join(str(arg) for arg in node.args)
...         return f"{function_name}({args_str})"

>>> Node.__str__ = node_str

>>> def node_repr(node):
...     reprs = [repr(node.value)]
...     if node.function is not None:
...         reprs.append(node.function.__qualname__)
...     if node.args:
...         reprs.extend([repr(arg) for arg in node.args])
...     args_repr = ", ".join(reprs)
...     return f"Node({args_repr})"
>>> Node.__repr__ = node_repr

>>> def f(x):
...    return 1.0 + cos(x)
>>> end = trace(f, [pi])
>>> end
Node(0.0, add, Node(-1.0, cos, Node(3.141592653589793)), Node(1.0))
>>> print(end)
add(cos(3.141592653589793), 1.0)

>>> def f(x, y):
...     return x * (x + y)
>>> t = trace(f, [1.0, 2.0])
>>> t
Node(3.0, multiply, Node(1.0), Node(3.0, add, Node(1.0), Node(2.0)))
>>> print(t)
multiply(1.0, add(1.0, 2.0))

>>> differential = {} 

>>> def d_add(x, y):
...     return add
>>> differential[add] = d_add

>>> def d_multiply(x, y):
...     def d_multiply_xy(dx, dy):
...         return x * dy + dx * y
...     return d_multiply_xy
>>> differential[multiply] = d_multiply

>>> def d_cos(x):
...     def d_cos_x(dx):
...         return - sin(x) * dx
...     return d_cos_x
>>> differential[cos] = d_cos

>>> def d_from_deriv(g):
...     def d_f(x):
...         def d_f_x(dx):
...             return g(x) * dx
...         return d_f_x
...     return d_f

>>> differential[sin] = d_from_deriv(cos)

>>> def find_and_sort_nodes(end_node):
...     todo = [end_node]
...     nodes = []
...     while todo:
...         node = todo.pop()
...         nodes.append(node)
...         for parent in node.args:
...             if parent not in nodes + todo:
...                 todo.append(parent) 
...     done = []
...     while nodes:
...         for node in nodes[:]:
...             if all([parent in done for parent in node.args]):
...                 done.append(node)
...                 nodes.remove(node)
...     return done

>>> def d(f):
...     def df(*args): # args=(x1, x2, ...)
...         start_nodes = [Node(arg) for arg in args]
...         end_node = f(*start_nodes)
...         if not isinstance(end_node, Node): # constant value
...             end_node = Node(end_node)
...         nodes = find_and_sort_nodes(end_node).copy()
...         def df_x(*d_args): # d_args = (d_x1, d_x2, ...)
...             for node in nodes:
...                 if node in start_nodes:
...                     i = start_nodes.index(node)
...                     node.d_value = d_args[i]
...                 elif node.function is None: # constant node
...                     node.d_value = 0.0
...                 else:
...                     _d_f = differential[node.function]
...                     _args = node.args
...                     _args_values = [_node.value for _node in _args]
...                     _d_args = [_node.d_value for _node in _args]
...                     node.d_value = _d_f(*_args_values)(*_d_args)
...             return end_node.d_value
...         return df_x
...     return df

>>> def deriv(f):
...     df = d(f)
...     def deriv_f(x):
...         return df(x)(1.0)
...     return deriv_f

>>> def f(x):
...     return pi
>>> g = deriv(f)
>>> g(0.0)
0.0
>>> g(1.0)
0.0

>>> def f(x):
...     return 2 * x + 1.0
>>> g = deriv(f)
>>> g(0.0)
2.0
>>> g(1.0)
2.0
>>> g(2.0)
2.0

>>> def f(x):
...     return x * x + 2 * x + 1
>>> g = deriv(f)
>>> g(0.0)
2.0
>>> g(1.0)
4.0
>>> g(2.0)
6.0

>>> def f(x):
...    return cos(x) * cos(x) + sin(x) * sin(x)
>>> g = deriv(f)
>>> g(0.0)
0.0
>>> g(pi/4)
0.0
>>> g(pi/2)
0.0

>>> def f(x):
...     return sin(x) * cos(x)
>>> g = deriv(f)
>>> def h(x):
...     return cos(x) * cos(x) - sin(x) * sin(x)
>>> g(0.0) == h(0.0)
True
>>> g(pi/4) == h(pi/4)
True
>>> g(pi/2) == h(pi/2)
True

>>> def grad(f):
...     df = d(f)
...     def grad_f(*args):
...         n = len(args)
...         grad_f_x = n * [0.0]
...         df_x = df(*args)
...         for i in range(0, n):
...             e_i = n * [0.0]; e_i[i] = 1.0
...             grad_f_x[i] = df_x(*e_i)
...         return grad_f_x  
...     return grad_f

>>> def f(x, y):
...     return 1.0
>>> grad(f)(0.0, 0.0)
[0.0, 0.0]
>>> grad(f)(1.0, 2.0)
[0.0, 0.0]

>>> def f(x, y):
...     return x + 2 * y + 1
>>> grad(f)(0.0, 0.0)
[1.0, 2.0]
>>> grad(f)(1.0, 2.0)
[1.0, 2.0]

>>> def f(x, y):
...     return x * x + y * y
>>> grad(f)(0.0, 0.0)
[0.0, 0.0]
>>> grad(f)(1.0, 2.0)
[2.0, 4.0]

>>> FD(exp, 0.0, h=1e-12)
1.000088900582341

>>> FD(exp, 0.0, h=9.999778782798785e-13)
1.0001110247585212

>>> FD(exp, 0.0, h=9.99866855977416e-13)
1.0

>>> eps = 2**(-52)
>>> e4 = eps / 4
>>> s1 = 1.0 + e4 + e4 + e4 + e4
>>> s2 = (((1.0 + e4) + e4) + e4) + e4
>>> s3 = 1.0 + (e4 + (e4 + (e4 + e4)))
>>> print_exact_number(s1)
1
>>> print_exact_number(s2)
1
>>> print_exact_number(s3)
1.0000000000000002220446049250313080847263336181640625

>>> eps = 2**-52
>>> floor(1e-12 / eps) * eps
9.99866855977416e-13

>>> 0.5 * eps / 1e-12 
0.00011102230246251565

>>> (floor(1e-12 / eps) + 0.5) * eps
9.999778782798785e-13
"""
def f(x):
    y = exp(-2.0 * x)
    u = 1.0 - y
    v = 1.0 + y
    w = u / v
    return w

def g(x):
    y = exp(-2.0 * x)
    u = 1.0 - y
    v = 1.0 + y
    w = u / v
    dx = 1.0
    dy = -2.0 * exp(-2.0 * x) * dx
    du = 0.0 - dy
    dv = 0.0 + dy
    dw = du / v + u * (- dv) / (v * v)  
    return dw

def FD(f, x, h):
    return (f(x + h) - f(x)) / h

def CD(f, x, h):
    return 0.5 * (f(x + h) - f(x - h)) / h

def add(x, y):
    return x + y

class Float(float):
    def __add__(self, other):
        print(f"trace: {self} + {other}")
        return super().__add__(other)

class Float(float):
    def __add__(self, other):
        print(f"trace: {self} + {other}")
        return Float(super().__add__(other))

import math

def cos(x):
    print(f"trace: cos({x})")
    return Float(math.cos(x))

class Node:
    def __init__(self, value):
        self.value = value

class Node:
    def __init__(self, value, function=None, *args):
        self.value = value
        self.function = function
        self.args = args

def cos(x):
    if isinstance(x, Node):
        cos_x_value = math.cos(x.value)
        cos_x = Node(cos_x_value, cos, x)
        return cos_x
    else:
        return math.cos(x) 

def add(x, y):
    if isinstance(x, Node) or isinstance(y, Node):
        if not isinstance(x, Node):
            x = Node(x)
        if not isinstance(y, Node):
            y = Node(y)
        add_x_y_value = x.value + y.value
        return Node(add_x_y_value, add, x, y)
    else:
        return x + y

Node.__add__ = add
Node.__radd__ = add

def autodiff(function):
    def autodiff_function(*args):
        if any([isinstance(arg, Node) for arg in args]):
            node_args = []
            values = []
            for arg in args:
                if isinstance(arg, Node):
                    node_args.append(arg)
                    values.append(arg.value)
                else:
                    node_args.append(Node(arg)) 
                    values.append(arg)
            output_value = function(*values)
            output_node = Node(
               output_value, autodiff_function, *node_args
            )
            return output_node
        else:
            return function(*args)        
    autodiff_function.__qualname__ = function.__qualname__
    return autodiff_function

sin = autodiff(math.sin)

def multiply(x, y):
    return x * y
multiply = autodiff(multiply)
Node.__mul__ = Node.__rmul__ = multiply

def node_str(node):
    if node.function is None:
        return str(node.value)
    else:
        function_name = node.function.__qualname__
        args_str = ", ".join(str(arg) for arg in node.args)
        return f"{function_name}({args_str})"

Node.__str__ = node_str

def node_repr(node):
    reprs = [repr(node.value)]
    if node.function is not None:
        reprs.append(node.function.__qualname__)
    if node.args:
        reprs.extend([repr(arg) for arg in node.args])
    args_repr = ", ".join(reprs)
    return f"Node({args_repr})"
Node.__repr__ = node_repr

differential = {} 

def d_add(x, y):
    return add
differential[add] = d_add

def d_multiply(x, y):
    def d_multiply_xy(dx, dy):
        return x * dy + dx * y
    return d_multiply_xy
differential[multiply] = d_multiply

def d_cos(x):
    def d_cos_x(dx):
        return - sin(x) * dx
    return d_cos_x
differential[cos] = d_cos

def d_from_deriv(g):
    def d_f(x):
        def d_f_x(dx):
            return g(x) * dx
        return d_f_x
    return d_f

differential[sin] = d_from_deriv(cos)

def find_and_sort_nodes(end_node):
    todo = [end_node]
    nodes = []
    while todo:
        node = todo.pop()
        nodes.append(node)
        for parent in node.args:
            if parent not in nodes + todo:
                todo.append(parent) 
    done = []
    while nodes:
        for node in nodes[:]:
            if all([parent in done for parent in node.args]):
                done.append(node)
                nodes.remove(node)
    return done

def d(f):
    def df(*args): # args=(x1, x2, ...)
        start_nodes = [Node(arg) for arg in args]
        end_node = f(*start_nodes)
        if not isinstance(end_node, Node): # constant value
            end_node = Node(end_node)
        nodes = find_and_sort_nodes(end_node).copy()
        def df_x(*d_args): # d_args = (d_x1, d_x2, ...)
            for node in nodes:
                if node in start_nodes:
                    i = start_nodes.index(node)
                    node.d_value = d_args[i]
                elif node.function is None: # constant node
                    node.d_value = 0.0
                else:
                    _d_f = differential[node.function]
                    _args = node.args
                    _args_values = [_node.value for _node in _args]
                    _d_args = [_node.d_value for _node in _args]
                    node.d_value = _d_f(*_args_values)(*_d_args)
            return end_node.d_value
        return df_x
    return df

def deriv(f):
    df = d(f)
    def deriv_f(x):
        return df(x)(1.0)
    return deriv_f

def grad(f):
    df = d(f)
    def grad_f(*args):
        n = len(args)
        grad_f_x = n * [0.0]
        df_x = df(*args)
        for i in range(0, n):
            e_i = n * [0.0]; e_i[i] = 1.0
            grad_f_x[i] = df_x(*e_i)
        return grad_f_x  
    return grad_f
