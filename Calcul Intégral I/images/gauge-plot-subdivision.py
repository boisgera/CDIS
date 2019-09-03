#!/usr/bin/env python

# Python 3.7 Standard Library
import pathlib
import sys

# Third-Party Packages
from numpy import *; seterr(all="ignore")
import numpy.linalg as la
import scipy.misc
import matplotlib as mpl; mpl.use("Agg")
from matplotlib.pyplot import *


#
# Matplotlib Configuration & Helper Functions
# ------------------------------------------------------------------------------
#
rc = {
    "text.usetex": True,
    "pgf.preamble": [r"\usepackage{amsmath,amsfonts,amssymb}"], 
    "font.family": "serif",
    #font.serif": [],
    #"font.sans-serif": [],
    "legend.fontsize": 10, 
    "axes.titlesize":  10,
    "axes.labelsize":  10,
    "xtick.labelsize": 10,
    "ytick.labelsize": 10,
}
mpl.rcParams.update(rc)

# Use PGF to render PDF with LaTeX fonts of the proper size.
from matplotlib.backends.backend_pgf import FigureCanvasPgf
mpl.backend_bases.register_backend("pdf", FigureCanvasPgf)

# The width of the standard LaTeX document is 345.0 pt.
width_in = 345 / 72.0 #345.0 / 72.0

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

# ------------------------------------------------------------------------------
def gauge_plot():
    figure()
    gca().set_aspect("equal")
    set_ratio(1.0, top=-0.1, bottom=-0.05)
    x = linspace(0.0, 1.0, 1000)
    plot(x, x, "-", color="#808080", lw=1.0)
    fill_betweenx(x, x-0.2, x+0.2, color="#d3d3d3")

    # Subdivision
    delta = 0.2
    x = r_[0.0:1.001:delta]
    t = 0.5 * (x[1:] + x[:-1])
    #print(x, t)
    # plot([0, 1], [0, 0], "k", lw=1.0)
    # plot(x, zeros_like(x), "k|")
    plot(t, zeros_like(t), "kx")

    for i in range(len(t)):
        plot([t[i], t[i]], [0, t[i]], "k--", lw=1.0)
        plot([x[i], x[i+1]], [t[i], t[i]], "k", lw=1.0)
        #plot([t[i]], [t[i]], "kx")
        plot([x[i]], [t[i]], "k|")
        plot([x[i+1]], [t[i]], "k|")




    xlabel("$t$")
    grid(True)
    save()

if __name__ == "__main__":
    gauge_plot()


