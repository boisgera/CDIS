#!/usr/bin/env python

# Python 3.7 Standard Library
import pathlib
import sys

# Third-Party Packages
from numpy import *; seterr(all="ignore")
import scipy.integrate as integrate
import matplotlib as mpl; mpl.use("Agg")
from matplotlib.pyplot import *

# Matplotlib Configuration
# ------------------------------------------------------------------------------
rc = {
    "text.usetex": True,
    "pgf.preamble": r"\usepackage{amsmath,amsfonts,amssymb}", 
    "font.family": "serif",
    "font.serif": [],      # use latex default serif font
    "font.sans-serif": [], # use a specific sans-serif font
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

# Plot
# ------------------------------------------------------------------------------
def main():
    t = r_[0.0:5:0.01]
    x = [integrate.quad(lambda s: cos(s*s), 0, t_) for t_ in t]
    y = [integrate.quad(lambda s: sin(s*s), 0, t_) for t_ in t]

    figure()
    plot(x, y, "k")
    axis("off")
    set_ratio(1.0, scale=0.5, bottom=0.0, top=0.0, left=0.0, right=0.0)
    gca().set_aspect(1.0)
    save()

# Command-Line Entry Point
# ------------------------------------------------------------------------------
if __name__ == "__main__":
    main()