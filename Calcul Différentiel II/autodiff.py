"""
    >>> from math import pi

    >>> print(sin(0.0))
    0.0
    >>> print("d_cos", d(cos)(0.0)(1.0))
    d_cos -0.0

--------------------------------------------------------------------------------

    >>> def f(x):
    ...     return x + 1
    >>> x = 2.0
    >>> df_x = d(f)(x)
    >>> df_x(1.0)
    1.0

    >>> def f(x):
    ...     return x * x + 2 * x + 1
    >>> x = 2.0
    >>> df_x = d(f)(x)
    >>> df_x(1.0)
    6.0

Derivative of f (manual computation)

    >>> def f(x):
    ...    return cos(x) * cos(x) + sin(x) * sin(x)
    >>> df = d(f)
    >>> def f_prime(x):
    ...    return df(x)(1.0)
    >>> f_prime(pi/4)
    0.0

Branching
--------------------------------------------------------------------------------

    >>> def f(x):
    ...     if x < 0.0:
    ...         return -x
    ...     else:
    ...         return x
    >>> df = d(f)
    >>> df(2.0)(1.0)
    1.0
    >>> df(-2.0)(1.0)
    -1.0

    >>> def f(x):
    ...     if x <= 0.0:
    ...         return 0.0
    ...     else:
    ...         return x * x
    >>> df = d(f)
    >>> df(-1.0)(1.0)
    0.0
    >>> df(1.0)(1.0)
    2.0

    >>> f = lambda x: (x >= 0) * x * x
    >>> df = d(f)
    >>> df(-1.0)(1.0)
    0.0
    >>> df(1.0)(1.0)
    2.0

"""

# TODO: 
#   - constant wrapping
#   - test management (branching)

# Python 3.7 Standard Library
import doctest
import inspect
import math 
import operator

# ------------------------------------------------------------------------------
class Node:
    def __init__(self, value, function=None, args=None):
         self.value = value
         self.function = function
         self.args = args if args is not None else []
    def __str__(self):
        if self.function is not None:
            function_name = self.function.__qualname__
            return f"Node({self.value}, {function_name}, {self.args})"
        else:
            return f"Node({self.value})"
    __repr__ = __str__

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
            output_node = Node(output_value, autodiff_function, node_args)
            return output_node
        else:
            return function(*args)        
    autodiff_function.__qualname__ = function.__qualname__
    return autodiff_function

# Function and Operators
# ------------------------------------------------------------------------------
functions  = ["exp", "log", "pow", "sqrt", "sin", "cos", "tan"]
operators  = ["add", "sub", "mul", "truediv", "neg", "pos"]
operators += ["lt", "le", "ge", "gt"] # not ne or eq ; fucks up the current
# topological sort. Of cours we could work with ids in the topological sort,
# or have a global flag to disable node outputs but it's overkill;
# x == y does generate "thin sets" in general where the differential
# cannot be computed.

globs = globals()
for function_name in functions:
    function = getattr(math, function_name)
    function = autodiff(function)
    globs[function_name] = function
for operator_name in operators:
    op = getattr(operator, operator_name)
    binary_op = (len(inspect.signature(op).parameters) == 2)
    op = autodiff(op)
    globs[operator_name] = op
    setattr(Node, f"__{operator_name}__", op)
    if binary_op:
        setattr(Node, f"__r{operator_name}__", op)
def _bool(x):
    if isinstance(x, Node):
        return bool(x.value)
    else:
        return bool(x)
Node.__bool__ = _bool


# Elementary Differentials 
# ------------------------------------------------------------------------------

differential = {}

# Derivative to Differential
def d_from_derivative(f_prime): # TODO: extend to partials ?
    def d_f(x):
        return lambda dx: f_prime(x) * dx
    return d_f

differential[exp] = d_from_derivative(exp)
differential[log] = d_from_derivative(lambda x: - 1.0 / x)
def d_pow(x, y):
    return lambda dx, dy: pow(x, y) * (y / x * dx + log(x) * dy)
differential[pow] = d_pow
differential[sqrt] = d_from_derivative(lambda x: 0.5 / sqrt(x))
differential[sin] = d_from_derivative(cos)
differential[cos] = d_from_derivative(lambda x: - sin(x))
differential[tan] = d_from_derivative(lambda x: 1.0 / (cos(x) * cos(x)))

differential[add] = lambda x, y: add
differential[sub] = lambda x, y: sub
def d_mul(x, y):
    return lambda dx, dy: dx * y + x * dy
differential[mul] = d_mul
def d_truediv(x, y):
    return lambda dx, dy: dx / y - x / y / y * dy 
differential[truediv] = d_truediv
differential[neg] = lambda x: neg
differential[pos] = lambda x: pos

def zero(dx, dy):
    return 0.0
differential[lt] = lambda x, y: zero
differential[le] = lambda x, y: zero
differential[ge] = lambda x, y: zero
differential[gt] = lambda x, y: zero

# Topological Sort
# ------------------------------------------------------------------------------
def sort_nodes(end_node):
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

# Automatic Differentation
# ------------------------------------------------------------------------------
def d(f):
    def df(*args): # args=(x1, x2, ...)
        start_nodes = [Node(arg) for arg in args]
        end_node = f(*start_nodes)
        if not isinstance(end_node, Node): # constant output
            end_node = Node(end_node)
        sorted_nodes = sort_nodes(end_node).copy()
        def df_x(*d_args): # d_args = (d_x1, d_x2, ...)
            for node in sorted_nodes:
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
    df.__qualname__ = "d_" + f.__qualname__
    return df

# Unit Tests
# ------------------------------------------------------------------------------
if __name__ == "__main__":
    doctest.testmod()