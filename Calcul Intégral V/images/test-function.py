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


# Graph
# ------------------------------------------------------------------------------
def main():
    x = 1
    eps= 0.2
    t = linspace(-0.1, x+0.1, 10000)
    h = (x+0.2) / 10000
    y = (0 <= t) * (t <= eps) * (-6 / eps**3) * t * (t- eps) \
        + (t >= x - eps)*(t <= x) * (6 / eps**3) * (t - x + eps) * (t - x)


    figure()    
    fig, (ax1, ax2) = subplots(1,2, sharex=True)
    #plot(x, f(1)(x), "k:", alpha=0.5)
    #plot(x, f(3)(x), "k--", alpha=0.75)
    ax1.plot(t, h * cumsum(y), "k", label="$|x|")
    #ax1.set_aspect("equal")
    ax1.set_xlim(t[0], t[-1])
    #ax1.set_ylim(-1.5, 1.5)
    #ax1.set_xticks([0, 1], ["0", r"$x=1$"])
    xticks([0, 1], ["0", r"$1$"])
    ax1.set_yticks([0, 1])
    ax1.grid(True)
    ax1.set_title(r"$y = \varphi_{\varepsilon}(t)$")
    ax1.set_xlabel(r"$t$")
    ax1.set_ylabel(r"$y$")


    #plot(x, f(1)(x), "k:", alpha=0.5)
    #plot(x, f(3)(x), "k--", alpha=0.75)
    ax2.plot(t, y, "k", label="$|x|")
    #ax1.set_aspect("equal")
    ax2.set_xlim(t[0], t[-1])
    #ax1.set_ylim(-1.5, 1.5)
    #ax1.set_xticks([-1, 0, 1])
    #ax1.set_yticks([-1, 0, 1])
    ax2.grid(True)
    ax2.set_xlabel(r"$t$")
    ax2.set_title(r"$y =  \psi_{\varepsilon}(t) = \varphi'_{\varepsilon}(t)$")





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

