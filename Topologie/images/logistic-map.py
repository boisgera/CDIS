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
    "text.latex.preamble": r"\usepackage{amsmath,amsfonts,amssymb}", 
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

# Exploiter info sur Feigenbaum
# <https://blog.stephenwolfram.com/2019/07/mitchell-feigenbaum-1944-2019-4-66920160910299067185320382/>

# Plot
# ------------------------------------------------------------------------------
def main():
    a = 4.0
    def f(x):
        return a * x * (1 - x)

    n = 100#10000
    xs = [0.2]
    dxs = [xs]
    for i in range(1, n):
        xs.append(f(xs[-1]))
        dxs = xs[-1] - xs[-2]

    figure()
    # alpha = 0.05 * (1 - abs(dxs))
    # color = np.zeros((n, 4))
    # color[:,3] = alpha
    # scatter(arange(n), xs, marker="s", color=color, edgecolors='none')#, alpha=alpha)
    plot(arange(n), xs, "k+")
    xlabel(r"$k \in \mathbb{N}$")
    ylabel(r"$x_k$")
    title(r"Suite logistique $x_k$")
    set_ratio(16/9, bottom=0.15)#, top=0.0, left=0.0, right=0.0)

    #gca().set_aspect(1.0)
    save()

# Command-Line Entry Point
# ------------------------------------------------------------------------------
if __name__ == "__main__":
    main()