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
    "pgf.preamble": [r"\usepackage{amsmath,amsfonts,amssymb}"], 
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

# Graph
# ------------------------------------------------------------------------------
def main():
    x = np.linspace(-1.5, 1.5, 1000)

    figure()    
    fig, (ax1, ax2) = subplots(1,2, sharex=True, sharey=True)
    #plot(x, f(1)(x), "k:", alpha=0.5)
    #plot(x, f(3)(x), "k--", alpha=0.75)
    ax1.plot(x, x>=0, "k")
    #ax1.set_aspect("equal")
    ax1.set_xlim(-1.5, 1.5)
    ax1.set_ylim(-0.1, 1.1)
    #ax1.set_xticks([-1, 0, 1])
    ax1.set_yticks([-1, 0, 1])
    ax1.grid(True)
    ax1.set_title(r"$e(t) = 1_{\left[0,+\infty \right[}(t)$")
    ax1.set_xlabel("$t$")

    ax2.plot(x, x * (x >=0), "k")
    #xp = x[x>=0]
    #xn = x[x<=0]
    #ax2.plot(xp, sign(xp), "k")
    #ax2.plot(xn, sign(xn), "k")
    #ax2.plot(0, 0, "k.")
    #ax2.set_aspect("equal")
    ax2.set_xlim(-1.5, 1.5)
    ax2.set_ylim(-0.1, 1.1)
    ax2.set_xticks([-1, 0, 1])
    #ax2.set_yticks([-1, 0, 1])
    ax2.grid(True)
    ax2.set_title("$x(t) = t e(t)$")
    ax2.set_xlabel("$t$")




    # #xlim(0.0, 1.0)
    # #ylim(0.0, 1.0)
    # #title("Graphe de $f$")
    # xlabel("$x$")
    # ylabel("$y$")
    # legend()
    #title("Escalier du diable (fonction de Cantor)")
    set_ratio(2, scale=1, left=0.1, bottom=0.15, top=0.1)
    save()

if __name__ == "__main__":
  main()

