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

    #y = scipy.stats.norm.cdf(x,0,1.0)

    figure()    
    for i in [-1, 0, 1]:
        x = np.linspace(i, i+1, 1000)
        plot(x, sin(x % 1), "k-")

    #plot(x, f(1)(x), "k:", alpha=0.5)
    #plot(x, f(3)(x), "k--", alpha=0.75)

    xlim(-1, 2)
    ylim(-0.1, 1.1)
    xticks([-1, 0, 1, 2])
    yticks([0, 0.5, 1])
    #title("Graphe de $f$")
    xlabel("$t$")
    ylabel("$y = f(t)$")
    #ylabel("$y=F(x)$")
    #legend()
    title(r"Graphe de la fonction $f$ quand $\tau=1$")
    set_ratio(16/9, scale=1, left=0.15, bottom=0.15, top=0.1)
    grid(True)
    #gca().set_aspect("equal")
    save()

if __name__ == "__main__":
  main()

