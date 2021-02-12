#!/usr/bin/env python

# Python 3.7 Standard Library
import pathlib
import sys

# Third-Party Packages
from numpy import *; seterr(all="ignore")
import matplotlib as mpl; mpl.use("Agg")
from mpl_toolkits.mplot3d import Axes3D # fix "3d" keyerror ? (https://stackoverflow.com/questions/56222259/valueerror-unknown-projection-3d-once-again)
from matplotlib.pyplot import *
from matplotlib import cm

# Matplotlib Configuration
# ------------------------------------------------------------------------------
rc = {
    "text.usetex": True,
    "pgf.preamble": r"\usepackage{amsmath,amsfonts,amssymb}", 
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
def f(x, y):
    return exp(-x*x - y*y)

def main():
    #fig = figure()
    fig = figure(figsize=figaspect(2/3)*2/3) #Adjusts the aspect ratio and enlarges the figure (text does not enlarge)
    ax = fig.add_subplot(1, 1, 1, projection='3d')
    X = linspace(-2, 2, 50, endpoint=True)
    xlen = len(X)
    Y = linspace(-2, 2, 50, endpoint=True)
    ylen = len(Y)
    X, Y = np.meshgrid(X, Y)
    Z = f(X, Y)



    surf = ax.plot_surface(X, Y, Z, rstride=1, cstride=1, color="white", alpha=1.0,
                        linewidth=0, antialiased=False)

    #for i in range(len(X[0])):
    # for i in [10, 15]:
    #    plot(X[i], Y[i], f(X[i], Y[i])+0.001, color="black", zorder=100, lw=1.0)
    x = linspace(-2, 2, 1000, endpoint=True);
    # for v in [-1.2, -1.1, -1, -0.9, -0.8]:
    #     y = v * ones_like(x)
    #     ax.plot(x, y, zs=f(x, y), color="#868e96", lw=1.0, zorder=100)
        #ax.text(-0.5, -1, f(0, -1), r"$z = f(x, -1)$")
    for v in [-1.5, -1, -0.5]:
        y = v * ones_like(x)
        ax.plot(x, y, zs=f(x, y), color="black", lw=1.0, zorder=100)
        ax.text(-0.5, 0, f(0, 0), r"$z = f(x, y)$", zorder=200)

    # y = linspace(-2, 2, 1000, endpoint=True);
    # x = 1.5 * ones_like(x)
    # ax.plot(x, y, zs=f(x, y), color="black", lw=1.0, zorder=100)
    # ax.text(1.5, 0, f(1.5, 0), r"$y \mapsto f(1.5, y)$", rotation=90, rotation_mode="anchor")


    #ax.plot_wireframe(X, Y, Z, rstride=1, cstride=1, color="black", lw=0.5)
    xlabel("$x$")
    ylabel("$y$")
    ax.set(zlabel="$z$")
    xticks([-2, -1, 0, 1, 2])
    yticks([-2, -1, 0,1, 2])
    ax.set_zticks([0 ,1])
    ax.set_zlim(0,1.0)


    #ax.set_zlim3d(-1, 1)

    save()

if __name__ == "__main__":
  main()

