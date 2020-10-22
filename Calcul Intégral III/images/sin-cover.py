#!/usr/bin/env python

# Python 3.7 Standard Library
import pathlib
import sys

# Third-Party Packages
from numpy import *; seterr(all="ignore")
import matplotlib as mpl; mpl.use("Agg")
from matplotlib.pyplot import *

# Matplotlib Configuration
# ------------------------------------------------------------------------------
rc = {
    "text.usetex": True,
    "pgf.preamble": r"\usepackage{amsmath,amsfonts,amssymb}", 
    "font.family": "serif",
    #"font.serif": [],      # use latex default serif font
    #"font.sans-serif": [], # use a specific sans-serif font
    "legend.fontsize": 10, # "medium" / 10 (equivalent)
    "axes.titlesize":  10,
    "axes.labelsize":  10,
    "xtick.labelsize": 10, # alt: "small",
    "ytick.labelsize": 10, # alt: "small",
}
mpl.rcParams.update(rc)

# Save the Picture
# ------------------------------------------------------------------------------
def save():
    filename = pathlib.Path(__file__)
    output = filename.with_suffix(filename.suffix + ".pdf") 
    savefig(output)

# Layout Helper
# ------------------------------------------------------------------------------
def set_ratio(ratio, scale=1.0, bottom=0.1, top=0.1, left=0.1, right=0.1):
    # The width of the standard LaTeX document is 345.0 pt.
    width_in = 345.0 / 72.0 * scale
    height_in = (1.0 - left - right)/(1.0 - bottom - top) * width_in / ratio
    gcf().set_size_inches((width_in, height_in))
    gcf().subplots_adjust(bottom=bottom, top=1.0-top, left=left, right=1.0-right)

# Forward Differentiation Scheme
# ------------------------------------------------------------------------------
def FD(f, x, h):
    "Forward Difference"
    return (f(x+h) - f(x)) / h

# Test Function
# ------------------------------------------------------------------------------
def f(x):
    return exp(x)

# Error Graph
# ------------------------------------------------------------------------------
def fd_error():

    n = 12
    x = linspace(0, 2*pi, 1000)
    y = sin(x)

    figure()
    plot(x, y, "k")
    ylim(-1.1, 1.1)
    #title("Graphe de $f$")
    xlabel("$x$")
    ylabel("$y$")
    title(r"$G = \{(x, \sin x) \; | \; x \in [0, 2\pi]\}$")

    for k in range(n):
        c = 2*k*pi/n + pi /n
        yc = sin(c) 
        x = [c - pi/n, c + pi/n, c + pi/n, c - pi/n, c-pi/n]
        y = [yc - pi/n, yc - pi/n, yc + pi/n, yc + pi/n, yc-pi/n]
        plot(x, y, "#495057", lw=1.0)
        fill_between(x[:2], y[:2], y[3:1:-1], color="#e9ecef")

    set_ratio(3, scale=1, left=0.15, bottom=0.20, top=0.15)
    grid(True)
    gca().axis("equal")
    save()

if __name__ == "__main__":
  fd_error()

