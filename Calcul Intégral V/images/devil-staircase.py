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

# Test Function
# ------------------------------------------------------------------------------
def f(n):
    def f_n(x):
        if n == 0:
            return x * (0 <= x) * (x <= 1) + (1 < x)
        else:
            return 0.5 * f(n-1)(3*x) * (x <= 1/3) + \
                0.5 * (1/3 < x) * (x <= 2/3) + \
                (0.5 + 0.5 * f(n-1)(3*x - 2)) * (2/3 < x)           
    return f_n
# Graph
# ------------------------------------------------------------------------------
def main():
    x = np.linspace(-0.5, 1.5, 10000)

    figure()    


    #plot(x, f(1)(x), "k:", alpha=0.5)
    #plot(x, f(3)(x), "k--", alpha=0.75)
    plot(x, f(5)(x), "k", label="$y=f_5(x)$")
    xlim(-0.5, 1.5)
    ylim(-0.1, 1.1)
    #title("Graphe de $f$")
    xlabel("$x$")
    ylabel("$y$")
    legend()
    title('Fonction de Cantor (escalier du diable)')
    set_ratio(16/9, scale=1, left=0.1, bottom=0.15, top=0.1)
    grid(True)
    gca().set_aspect("equal")
    save()

if __name__ == "__main__":
  main()

