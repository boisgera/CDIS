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

def contour_demo():
    delta = 0.025
    x = arange(-3.0, 3.00001, delta)
    y = arange(-2.0, 2.00001, delta)
    X, Y = meshgrid(x, y)
    D = sqrt(X*X+Y*Y)
    Z = (D - 1) * (D >= 1) + (1-D) * (D < 1)

    FAKE = D - 1

    fig, ax = subplots()
    #CS = ax.contour(X, Y, Z, colors="k", levels=[0.5, 1.0, 1.5, 2.0], linestyles="solid")
    #ax.clabel(CS, inline=1, fmt= '%1.1f', fontsize=10)
    CS2 = ax.contour(X, Y, FAKE, colors="k", levels=[0.0], linestyles="solid")
    #ax.clabel(CS2, inline=1, fmt= '%1.1f', fontsize=10)

    plot(2, 1, "kx")
    text(2, 1.2, "$x$", horizontalalignment='center', verticalalignment='center')
    x, y = 2/sqrt(5), 1/sqrt(5)
    plot(x, y, "k.", ms=10)
    plot([0, x], [0, y], linestyle="--", lw=1, color="black")
    plot([x, 2], [y, 1], "k", lw=1)
    text(1.35, 0.9, "$d_C(x)$", horizontalalignment='center', verticalalignment='center', rotation=arctan(0.5)/pi*180, rotation_mode='anchor')

    #plot([2, 2], [1, 0], ls="--", color="grey", lw=1)
    #plot([2, 0], [1, 1], ls="--", color="grey", lw=1)

    text(0.25, 0.5, "$C$")
    ax.set_title("Détermination géométrique de $d_C(x)$")
    xlabel("$x_1$")
    ylabel("$x_2$")
    xlim(-3, 3); xticks([0])
    ylim(-2, 2); yticks([0])
    set_ratio(4/3, bottom=0.1, top=0.1)
    gca().set_aspect(1.0)
    grid(True)
    save()

if __name__ == "__main__":
    contour_demo()

