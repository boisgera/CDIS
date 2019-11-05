#!/usr/bin/env python

# Python 3.7 Standard Library
import pathlib
import sys

# Third-Party Packages
from numpy import *; seterr(all="ignore")
import matplotlib as mpl; mpl.use("Agg")
from matplotlib.pyplot import *
import scipy.stats

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

# Graph
# ------------------------------------------------------------------------------
def main():
    x = np.linspace(-3.5, 3.5, 10000)
    y = scipy.stats.norm.cdf(x,0,1.0)

    figure()    


    #plot(x, f(1)(x), "k:", alpha=0.5)
    #plot(x, f(3)(x), "k--", alpha=0.75)
    plot(x, y, "k-")
    xlim(-3.5, 3.5)
    ylim(-0.1, 1.1)
    yticks([0,0.5, 1])
    #title("Graphe de $f$")
    xlabel("$x$")
    ylabel("$y=F(x)$")
    #legend()
    title("Fonction de répartition d'une loi normale centrée réduite")
    set_ratio(16/9, scale=1, left=0.15, bottom=0.15, top=0.1)
    grid(True)
    #gca().set_aspect("equal")
    save()

if __name__ == "__main__":
  main()

