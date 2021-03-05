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
def eps(n):
    return 1.25/(n+1)

def fd_error():
    x = linspace(0, pi, 1000)
    y = sin(x)

    rem = y
    f_k = zeros_like(y)

    figure()
    fig, axes = subplots(2,2, sharex=True, sharey=True)
    xticks([0, pi/2, pi], ["0", r"$\pi/2$", r"$\pi$"])
    yticks([0, 1])
    for i in range(4):
        ax = ravel(axes)[i]
        if i >= 1:
            ax.fill_between(x, zeros_like(x), f_k, edgecolor="none", facecolor="black", alpha=0.125)
        delta = (rem >= eps(i)) * eps(i)
        f_k = f_k + delta
        rem = rem - delta
        ax.plot(x, y, "k--", alpha=0.5)
        ax.plot(x, f_k, "k", label=f"$f_{i}$")
        ax.legend()
        #ax.set_title(f"$f_{i}$")

    # figure()
    # plot(x, y, "k--", label="$f$")
    # ylim(-0.1, 1.1)
    # #title("Graphe de $f$")
    # xlabel("$x$")
    # ylabel("$y$")
    # xticks([0, pi/2, pi], ["0", r"$\pi/2$", r"$\pi$"])
    # yticks([0, 1])
    # title(r"$y=\sin(x)$")

    # vals = [1/2, 1/2 + 1/3, 1/2+1/3+1/4]
    # plot(0, 0, "k.")
    # plot(pi, 0, "k.")
    # plot([0, arcsin(1/2)], [0, 0], "k")
    # plot([pi-arcsin(1/2), pi], [0, 0], "k")
    # plot([arcsin(1/2), pi - arcsin(1/2)], [1/2, 1/2])

    # legend()

    grid(False)
    ylim(-0.1, 1.1)
    set_ratio(16/9, scale=1, left=0.1, bottom=0.1, top=0.1)
    save()

if __name__ == "__main__":
  fd_error()

