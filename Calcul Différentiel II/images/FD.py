#!/usr/bin/env python
"""
Complex-Step Differentiation
"""

# Python 2.7 Standard Library
from __future__ import division
import os
import sys

# Third-Party Packages
import numpy as np; np.seterr(all="ignore")
import scipy.misc
import matplotlib as mpl; mpl.use("Agg")
import matplotlib.pyplot as pp

#
# Matplotlib Configuration & Helper Functions
# ------------------------------------------------------------------------------
#
rc = {
    "text.usetex": True,
    "pgf.preamble": [r"\usepackage{amsmath,amsfonts,amssymb}"], 
    "font.family": "serif",
    "font.serif": [],
    "font.sans-serif": [],
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
width_in = 345.0 / 72.0

def save(name, dpi=None):
    options = {}
    if dpi:
        options["dpi"] = dpi
    cwd = os.getcwd()
    root = os.path.dirname(os.path.realpath(__file__))
    os.chdir(root)
    pp.savefig(name + ".pdf", **options)
    pp.savefig(name + ".png", **options)
    pp.savefig(name + ".pgf")
    pp.savefig(name + ".svg")
    os.chdir(cwd)

def set_ratio(ratio, bottom=0.1, top=0.1, left=0.1, right=0.1):
    height_in = (1.0 - left - right)/(1.0 - bottom - top) * width_in / ratio
    pp.gcf().set_size_inches((width_in, height_in))
    pp.gcf().subplots_adjust(bottom=bottom, top=1.0-top, left=left, right=1.0-right)

# Binary Representation of Floating-Point Numbers
# ------------------------------------------------------------------------------
def s_e_f(number):
#    number = np.float64(number)
#    if sys.byteorder == "little":
#        number = number.byteswap()
#    binary = np.getbuffer(number)
#    return str(binary)
     array = np.array([number], dtype=np.float64)
     buffer = np.getbuffer(array)
     integer = np.frombuffer(buffer, dtype=np.uint64)[0]
     return bin(integer) # would need padding for the first bytes,
     # otherwise it works.

def s_e_f2(number):
    import bitstream
    stream = bitstream.BitStream(number, float)
    s = stream.read(bool)
    e = 0
    for bit in stream.read(bool, 11):
        e = (e << 1) + bit
    f = stream.read(bool, 52)
    return s, e, f


# Differentiation Schemes (First Derivative)
# ------------------------------------------------------------------------------

def FD(f, x, h):
    "Forward Difference"
    return (f(x+h) - f(x)) / h

def CD(f, x, h):
    "Central Difference"
    return 0.5 * (f(x+h) - f(x-h)) / h

def CSD(f, x, h):
    "Complex-Step Differentation"
    return np.imag(f(x+1j*h)) / h

def display(number):
    "Display all (non-zero) digits of a float"
    print "{0:.100g}".format(number)


# Complex (Pure Imaginary) Step Differentiation
# ------------------------------------------------------------------------------
def f(z):
    return np.exp(z)

def fd_value():
    h = np.logspace(-18, 6, 1000)
    pp.clf()
    pp.axis([1e-18, 1e2, -0.3, 2.3])
    pp.xscale("log")
    pp.yticks([0.0, 1.0, 2.0])
    pp.xticks([1e-16, 1e-12, 1e-8, 1e-4, 1e0])
    pp.plot(h, FD(f, 0.0, h), "k", label="$\mathrm{FD}(\exp, 0, h)$")
    pp.plot([h[0], h[-1]],[1.0, 1.0], "k--", label=r"$[\exp'(0)]$",alpha=1.0) 
    pp.plot(h, 2**(-52) / h, "k:", label=r"$[\epsilon/h]$")
    pp.legend()
    set_ratio(np.sqrt(3.0), bottom=0.1, top=0.1)
    pp.title(r"Graph of $h \mapsto \mathrm{FD}(\exp, 0, h)$")
    save("fd-value", dpi=600)

def fd_error():
    h = np.logspace(-18, 6, 1000)
    pp.clf()
    pp.axis([1e-18, 1e6, 1e-14, 1e2])
    y_2_x_ratio = 16 / 24
    pp.xscale("log")
    pp.yscale("log")
    pp.yticks([1e-12, 1e-8, 1e-4, 1e0], ha="left")
    pp.gca().get_yaxis().set_tick_params(pad=25, direction="out")
    pp.xticks([1e-16, 1e-12, 1e-8, 1e-4, 1e0])
    pp.plot(h, abs(1.0 - FD(f, 0.0, h)), "k", label="FD error")
    pp.title("Graph of $h \mapsto [|\mathrm{FD}(\exp, 0, h) -\exp'(0)|]$")
    pp.axes().set_aspect(1.0)
    pp.gcf().set_figwidth(width_in)
    pp.extra = 1.2
    pp.gcf().set_figheight(width_in * y_2_x_ratio)
    pp.gcf().subplots_adjust(bottom=0.05)
    pp.legend(loc="center right")
    pp.grid(True)
    save("fd-error", dpi=600)

def cd_error():
    h = np.logspace(-18, 6, 1000)
    pp.clf()
    pp.axis([1e-18, 1e6, 1e-14, 1e2])
    y_2_x_ratio = 16 / 24
    pp.xscale("log")
    pp.yscale("log")
    pp.yticks([1e-12, 1e-8, 1e-4, 1e0], ha="left")
    pp.gca().get_yaxis().set_tick_params(pad=25, direction="out")
    pp.xticks([1e-16, 1e-12, 1e-8, 1e-4, 1e0])
    pp.plot(h, abs(1.0 - FD(f, 0.0, h)), "k", color="0.75", label="FD error")
    pp.plot(h, abs(1.0 - CD(f, 0.0, h)), "k", color="0.00", label="CD error")
    pp.title("Graph of $h \mapsto [|\mathrm{CD}(\exp, 0, h) -\exp'(0)|]$")
    pp.axes().set_aspect(1.0)
    pp.gcf().set_figwidth(width_in)
    pp.extra = 1.2
    pp.gcf().set_figheight(width_in * y_2_x_ratio)
    pp.gcf().subplots_adjust(bottom=0.05)
    pp.legend(loc="center right")
    pp.grid(True)
    save("cd-error", dpi=600)

def csd_error():
    h = np.logspace(-18, 6, 1000)
    pp.clf()
    pp.axis([1e-18, 1e6, 1e-24, 1e2])
    y_2_x_ratio = 26 / 24
    pp.xscale("log")
    pp.yscale("log")
    pp.yticks([1e-24, 1e-20, 1e-16, 1e-12, 1e-8, 1e-4, 1e0], 
              [r"$10^{-\infty}$", r"$\;\;\vdots$",
               r"$10^{-16}$", r"$10^{-12}$", r"$10^{-8}$", 
               r"$10^{-4}$", r"$10^{0}$"], ha="left")
    pp.gca().get_yaxis().set_tick_params(pad=25, direction="out")
    pp.xticks([1e-16, 1e-12, 1e-8, 1e-4, 1e0])
    pp.plot(h, abs(1.0 - CD(f, 0.0, h)), "k", color="0.75", label="CD error")
    FLOOR = 1e-24
    e = abs(1.0 - CSD(f,0.0, h))
    e[e==0.0] = FLOOR
    pp.plot(h, e, "k", label="CSD error")
    eps = 2**(-52)
    pp.plot(h, np.ones_like(h) * eps, "k--", label=r"$\epsilon = 2^{-52}$")
    pp.title("Graph of $h \mapsto [|\mathrm{CSD}(\exp, 0, h) -\exp'(0)|]$")
    pp.axes().set_aspect(1.0)
    ratio = 1.618 * 1.0 # thin 
    pp.gcf().set_figwidth(width_in)
    pp.extra = 1.2
    pp.gcf().set_figheight(width_in * y_2_x_ratio)
    pp.gcf().subplots_adjust(bottom=0.05)
    pp.legend(loc="center right")
    pp.grid(True)
    save("csd-error", dpi=600)

def csd_error_alt():
    pp.clf()
    FLOOR = 1e-24
    h = np.logspace(-18, 6, 1000)
    pp.axis([1e-18, 1e6, 0.01 * FLOOR, 1e2])
    pp.xscale("log")
    pp.yscale("log")
    pp.yticks(
      [FLOOR, 1e-20, 1e-16, 1e-12, 1e-8, 1e-4, 1e0], 
      [r"$10^{-\infty}$", r"$\;\;\vdots$", "$10^{-16}$", "$10^{-12}$", 
        "$10^{-8}$", "$10^{-4}$", "$10^{0}$"],   
    ha="left")
    pp.gca().get_yaxis().set_tick_params(pad=27, direction="out")
    pp.xticks([1e-16, 1e-12, 1e-8, 1e-4, 1e0, 1e4])
    pp.plot(h, abs(1.0 - FD(f, 0.0, h)), "k", alpha=0.3, lw=1.0, label="FD error")
    e = abs(1.0 - CSD(f,0.0, h))
    e[e==0.0] = FLOOR
    pp.plot(h, e, "k.", markersize=1.5, mew=0.1, label="CSD error")
    phi = 0.5 * (np.sqrt(5) + 1)
    set_ratio(phi)
    pp.legend(loc="center right")
    save("csd-error-alt", dpi=600)

# Spectral Methods & Higher-Order Derivatives
# ------------------------------------------------------------------------------
def f(z):
    return 1.0 / (1.0 - z)

def SM(f, x, h, N):
    "Spectral Method Scheme"
    w = np.exp(-1j * 2 * np.pi / N)
    k = n = np.arange(N)
    f_k = f(x + h * w**k)
    c_n = np.fft.ifft(f_k)
    a_n = c_n / h ** n
    return a_n * scipy.misc.factorial(n)

def spectral():
    x = 0
    N = 32
    u = np.exp(-1j * 2 * np.pi / N)
    c = []
    b = []
    hs = np.logspace(-18, 6, 1000) 
    alphas, rs = [], []
    efft = []
    for h in hs:
        f_k = np.array([f(x+h * u**k) for k in np.arange(0,N)])
        c_n = np.real(np.fft.ifft(f_k))
        efft.append(np.imag(np.fft.ifft(f_k)))
        c.append(c_n)
        A = np.c_[np.ones(N), np.arange(N)]
        bb = np.log(abs(c_n))
        xx, _, _, _ = np.linalg.lstsq(A, bb)
        alpha = np.exp(xx[0])
        _r = np.exp(xx[1])
        alphas.append(alpha)
        rs.append(_r)
        b.append(c_n / h ** np.arange(N))

    c = np.array(c)
    b = np.array(b)
    e = np.abs(np.array(b) - 1.0)
    efft = np.array(efft)

    pp.clf()
    pp.axes().set_aspect(1.0)
    ratio = 1.618 * 1.0 # thin 
    pp.gcf().set_figwidth(width_in)
    pp.axis([1e-18, 1e2, 1e-18, 1e-6])
    pp.yscale("log")
    pp.xscale("log")

    for i in [1,2,3,4]:
        pp.plot(hs,e[:,i], color=str(0.2*(i)), label=r"$n="+str(i)+"$")
    pp.xticks([1e-16, 1e-12, 1e-8, 1e-4, 1e0])
    pp.yticks([1e-16, 1e-12, 1e-8], ha="left")
    pp.gca().get_yaxis().set_tick_params(pad=25, direction="out")
    pp.grid(True)
    pp.title(r"Accuracy of $f^{(n)}(0) \simeq \mathrm{SM}(f,0,h,N)[n]$ for $f(z)=1/(1-z)$")
    l = pp.legend(title="$N=32$", loc="center left")
    pp.xlabel("radius $h$")
    pp.ylabel("relative error")
    pp.setp(l.get_texts(), fontsize=10)
    pp.setp(l.get_title(), fontsize=10)

    y_2_x_ratio = 12/20.0
    pp.gcf().set_figheight(width_in * y_2_x_ratio)
    pp.gcf().subplots_adjust(bottom=0.15)
    save("sm-error", dpi=600)

    for i, c in enumerate (np.real(SM(f, 0, 0.2, 32)[:])):
        pass
        #print r"f^({0})(0)".format(i), "{0:.100g}".format(c),
        #print "rel. error", "{0:.2g}".format(abs(c/scipy.misc.factorial(i) - 1.0))

if __name__ == "__main__":
  fd_value()
  fd_error()
  cd_error()
  csd_error()
  csd_error_alt()

  spectral()

