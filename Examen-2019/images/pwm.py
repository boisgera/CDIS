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


def main():
    k = arange(0, 50)
    xk = cumsum(r_[0.0, array([2.0**(-_k-1) for _k in k])])
    #print(xk)

    figure()
    sign = 1
    for _k in k[:-1]:
        #print([xk[_k], xk[_k+1]], sign*array([1.0, 1.0]), "k+")
        plot([xk[_k]], [sign], "k.")
        plot([xk[_k], xk[_k+1]], sign*array([1.0, 1.0]), "k-")
        sign *= -1
    plot([-0.5, 0.0], [0.0, 0.0], "k")
    plot([1.0], [0.0], "k.")
    plot([1.0, 5.0], [0.0, 0.0], "k")
    
    xticks(r_[-0.25:1.5:0.25])
    yticks([-1,0,1])
    xlim(-0.5, 1.5)
    ylim(-1.1, 1.1)
    xlabel("$x$")
    ylabel("$y$")
    # legend()
    title("$y=f(x)$")
    set_ratio(3.0, scale=1.0, left=0.15, bottom=0.2, top=0.15)
    grid(True)
    save()

if __name__ == "__main__":
    main()

