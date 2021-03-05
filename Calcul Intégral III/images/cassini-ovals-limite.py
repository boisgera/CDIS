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

def contour_demo():
    delta = 0.001
    x = arange(-3.0, 3.0, delta)
    y = arange(-3.0, 3.0, delta)
    X, Y = meshgrid(x, y)

    a = 1.0
    b = 1.0
    Z = (X*X + Y*Y)**2 - 2*a**2 * (X*X - Y*Y) + a**4 - b**4
    fig, ax = subplots()
    CS = ax.contourf(X, Y, Z, levels=[-10, 0.0], colors="#d3d3d3", linestyles="solid")
    xlim(-2, 2); xticks([-2, -1, 0, 1, 2])
    ylim(-1, 1); yticks([-1, 0, 1])
    set_ratio(4/3, bottom=0.0, top=0.0)
    gca().set_aspect(1.0)
    xlabel("$x$")
    ylabel("$y$")
    title(r"$(x^2+y^2)^2 - 2a^2 (x^2 - y^2) + a^4 \leq b^4, \, a=b=1.0$")
    save()


# "$\{(x,y) \in \R^2 \, | \, (x^2+y^2)^2 - 2a^2 (x^2 - y^2) + a^4 \leq b^4\}$"

if __name__ == "__main__":
    contour_demo()

