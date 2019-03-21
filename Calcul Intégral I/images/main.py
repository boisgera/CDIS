#!/usr/bin/env python

# Python 2.7 Standard Library
from __future__ import division
import gc
import os

# Third-Party Packages
import numpy as np; np.seterr(all="ignore")
import numpy.linalg as la
import scipy.misc
import matplotlib as mpl; mpl.use("Agg")
import matplotlib.pyplot as pp
import matplotlib.patches as pa

# Local
# import path

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

def save(name, dpi=None):
    options = {"bbox_inches": "tight"}
    if dpi:
        options["dpi"] = dpi
    cwd = os.getcwd()
    root = os.path.dirname(os.path.realpath(__file__))
    os.chdir(root)
    pp.savefig(name + ".pdf", **options)
    # pp.savefig(name + ".png", **options)
    # pp.savefig(name + ".pgf", **options)
    # pp.savefig(name + ".svg", **options)
    os.chdir(cwd)

def set_ratio(ratio=1.0, bottom=0.1, top=0.1, left=0.1, right=0.1):
    height_in = (1.0 - left - right)/(1.0 - bottom - top) * width_in / ratio
    pp.gcf().set_size_inches((width_in, height_in))
    pp.gcf().subplots_adjust(bottom=bottom, top=1.0-top, left=left, right=1.0-right)

def gauge_plot():
    pp.figure()
    pp.gca().set_aspect("equal")
    set_ratio(1.0)
    x = np.linspace(0.0, 1.0, 1000)
    pp.plot(x, x, "k--")
    pp.plot(x-0.2, x, "k-")
    pp.plot(x+0.2, x, "k-")
    pp.fill_betweenx(x, x-0.2, x+0.2, color="#d3d3d3")
    pp.grid(True)
    save("gauge-plot", dpi=600)

if __name__ == "__main__":
    gauge_plot()


