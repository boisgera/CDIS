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
def set_ratio(ratio, bottom=0.1, top=0.1, left=0.1, right=0.1):
    # The width of the standard LaTeX document is 345.0 pt.
    width_in = 345.0 / 72.0
    height_in = (1.0 - left - right)/(1.0 - bottom - top) * width_in / ratio
    gcf().set_size_inches((width_in, height_in))
    gcf().subplots_adjust(bottom=bottom, top=1.0-top, left=left, right=1.0-right)

# Plot
# ------------------------------------------------------------------------------
def main():
    df = 8000.0
    dt = 1.0 / df
    N = 1000
    f = linspace(0.0, df/2, N)
    z_f = exp(1j * 2 * pi * f * dt)
    h_f = z_f / (z_f - 0.5)

    figure()
    plot(f, abs(h_f), "k")
    xticks([0.0, 1000.0, 2000.0, 3000.0, 4000.0])
    yticks([0.0, 0.5, 1.0, 1.5, 2.0])
    xlabel(r"$f$ in Hz")
    ylabel(r"$|h(f)|$")
    title(r"AR Filter Frequency Response -- Magnitude")
    axis([0.0, 4000.0, 0.0, 2.1])
    grid(True)

    set_ratio(2.0, bottom=0.2, left=0.15)

    save()

# Command-Line Entry Point
# ------------------------------------------------------------------------------
if __name__ == "__main__":
    main()