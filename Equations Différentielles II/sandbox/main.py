
from autograd import *
from autograd.numpy import *
import numpy.linalg as linalg
from matplotlib.pyplot import *

def root(f, x):
    x = array(x)
    for i in range(100):
        fx = f(x)
        Jfx = jacobian(f)(x)
        x = x - linalg.solve(Jfx, fx)
    return x

def explicit_euler_step(fun, x, t, dt):
    return x + dt * fun(t, x)

def implicit_euler_step(fun, x, t, dt):
    F = lambda x_next: x_next - x - dt * fun(t, x_next)
    return root(F, x)

def basic_solve_ivp(fun, t_0, x_0, dt, t_f, method):
    ts, xs = [t_0], [x_0]
    while ts[-1] < t_f:
        t, x = ts[-1], xs[-1]
        t_next, x_next = t + dt, method(fun, x, t, dt)
        ts.append(t_next); xs.append(x_next)

    return (array(ts), array(xs).T)

# ------------------------------------------------------------------------------

def test_1():

    a = -100.0

    def fun(t, x):
        return a * x

    dt = 0.025
    t_0, t_f = 0.0, 1.0
    x_0 = array([1.0])


    ts, xs = basic_solve_ivp(fun, t_0, x_0, dt, t_f, method=implicit_euler_step)

    plot(ts, exp(a*ts), "k:")
    plot(ts, xs[0], "b")

    ts, xs = basic_solve_ivp(fun, t_0, x_0, dt, t_f, method=explicit_euler_step)

    plot(ts, xs[0], "r")
    ylim(-1.0, 1.0)

    show()


def test_2():


    def fun(t, x):
        return array([-x[0], -100*x[1]])

    dt = 0.025
    t_0, t_f = 0.0, 1.0
    x_0 = array([1.0, 1.0])

    ts, xs = basic_solve_ivp(fun, t_0, x_0, dt, t_f, method=implicit_euler_step)

    plot(ts, xs[0], "b")
    plot(ts, xs[1], "g")

    ts, xs = basic_solve_ivp(fun, t_0, x_0, dt, t_f, method=explicit_euler_step)

    plot(ts, xs[0], "c")
    plot(ts, xs[1], "y")
    ylim(-1.0, 1.0)

    show()

#test_1()
test_2()