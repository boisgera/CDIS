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
def save(name=None):
    filename = pathlib.Path(__file__)
    if name is not None:
        directory = filename.parent
        filename = directory / (name + ".py")
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

# Binary Representation of Floating-Point Numbers
# ------------------------------------------------------------------------------
def s_e_f(number):
     array = array([number], dtype=float64)
     buffer = getbuffer(array)
     integer = frombuffer(buffer, dtype=uint64)[0]
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

def display(number):
    "Display all (non-zero) digits of a float"
    print("{0:.100g}".format(number))


# Complex (Pure Imaginary) Step Differentiation
# ------------------------------------------------------------------------------
def f(z):
    return exp(z)

def fd_value():
    h = logspace(-18, 6, 1000)
    clf()
    axis([1e-18, 1e2, -0.3, 2.3])
    xscale("log")
    yticks([0.0, 1.0, 2.0])
    xticks([1e-16, 1e-12, 1e-8, 1e-4, 1e0])
    plot(h, FD(f, 0.0, h), "k", label="$\mathrm{FD}(\exp, 0, h)$")
    plot([h[0], h[-1]],[1.0, 1.0], "k--", label=r"$[\exp'(0)]$",alpha=1.0) 
    plot(h, 2**(-52) / h, "k:", label=r"$[\epsilon/h]$")
    legend()
    set_ratio(sqrt(3.0), bottom=0.1, top=0.1)
    title(r"Graph of $h \mapsto \mathrm{FD}(\exp, 0, h)$")
    save("fd-value")

def fd_error():
    h = logspace(-18, 6, 1000)
    clf()
    axis([1e-18, 1e6, 1e-14, 1e2])
    y_2_x_ratio = 16 / 24
    xscale("log")
    yscale("log")
    yticks([1e-12, 1e-8, 1e-4, 1e0], ha="left")
    gca().get_yaxis().set_tick_params(pad=25, direction="out")
    xticks([1e-16, 1e-12, 1e-8, 1e-4, 1e0])
    plot(h, abs(1.0 - FD(f, 0.0, h)), "k", label="FD error")
    title("Graph of $h \mapsto [|\mathrm{FD}(\exp, 0, h) -\exp'(0)|]$")
    axes().set_aspect(1.0)
    #gcf().set_figwidth(width_in)
    extra = 1.2
    #gcf().set_figheight(width_in * y_2_x_ratio)
    #gcf().subplots_adjust(bottom=0.05)
    legend(loc="center right")
    grid(True)
    save("fd-error")

def cd_error():
    h = logspace(-18, 6, 1000)
    clf()
    axis([1e-18, 1e6, 1e-14, 1e2])
    y_2_x_ratio = 16 / 24
    xscale("log")
    yscale("log")
    yticks([1e-12, 1e-8, 1e-4, 1e0], ha="left")
    gca().get_yaxis().set_tick_params(pad=25, direction="out")
    xticks([1e-16, 1e-12, 1e-8, 1e-4, 1e0])
    plot(h, abs(1.0 - FD(f, 0.0, h)), "k", color="0.75", label="FD error")
    plot(h, abs(1.0 - CD(f, 0.0, h)), "k", color="0.00", label="CD error")
    title("Graph of $h \mapsto [|\mathrm{CD}(\exp, 0, h) -\exp'(0)|]$")
    axes().set_aspect(1.0)
    #gcf().set_figwidth(width_in)
    extra = 1.2
    #gcf().set_figheight(width_in * y_2_x_ratio)
    #gcf().subplots_adjust(bottom=0.05)
    legend(loc="center right")
    grid(True)
    save("cd-error")

def csd_error():
    h = logspace(-18, 6, 1000)
    clf()
    axis([1e-18, 1e6, 1e-24, 1e2])
    y_2_x_ratio = 26 / 24
    xscale("log")
    yscale("log")
    yticks([1e-24, 1e-20, 1e-16, 1e-12, 1e-8, 1e-4, 1e0], 
              [r"$10^{-\infty}$", r"$\;\;\vdots$",
               r"$10^{-16}$", r"$10^{-12}$", r"$10^{-8}$", 
               r"$10^{-4}$", r"$10^{0}$"], ha="left")
    gca().get_yaxis().set_tick_params(pad=25, direction="out")
    xticks([1e-16, 1e-12, 1e-8, 1e-4, 1e0])
    plot(h, abs(1.0 - CD(f, 0.0, h)), "k", color="0.75", label="CD error")
    FLOOR = 1e-24
    e = abs(1.0 - CSD(f,0.0, h))
    e[e==0.0] = FLOOR
    plot(h, e, "k", label="CSD error")
    eps = 2**(-52)
    plot(h, ones_like(h) * eps, "k--", label=r"$\epsilon = 2^{-52}$")
    title("Graph of $h \mapsto [|\mathrm{CSD}(\exp, 0, h) -\exp'(0)|]$")
    axes().set_aspect(1.0)
    ratio = 1.618 * 1.0 # thin 
    gcf().set_figwidth(width_in)
    extra = 1.2
    gcf().set_figheight(width_in * y_2_x_ratio)
    gcf().subplots_adjust(bottom=0.05)
    legend(loc="center right")
    grid(True)
    save("csd-error")

def csd_error_alt():
    clf()
    FLOOR = 1e-24
    h = logspace(-18, 6, 1000)
    axis([1e-18, 1e6, 0.01 * FLOOR, 1e2])
    xscale("log")
    yscale("log")
    yticks(
      [FLOOR, 1e-20, 1e-16, 1e-12, 1e-8, 1e-4, 1e0], 
      [r"$10^{-\infty}$", r"$\;\;\vdots$", "$10^{-16}$", "$10^{-12}$", 
        "$10^{-8}$", "$10^{-4}$", "$10^{0}$"],   
    ha="left")
    gca().get_yaxis().set_tick_params(pad=27, direction="out")
    xticks([1e-16, 1e-12, 1e-8, 1e-4, 1e0, 1e4])
    plot(h, abs(1.0 - FD(f, 0.0, h)), "k", alpha=0.3, lw=1.0, label="FD error")
    e = abs(1.0 - CSD(f,0.0, h))
    e[e==0.0] = FLOOR
    plot(h, e, "k.", markersize=1.5, mew=0.1, label="CSD error")
    phi = 0.5 * (sqrt(5) + 1)
    set_ratio(phi)
    legend(loc="center right")
    save("csd-error-alt")

# Spectral Methods & Higher-Order Derivatives
# ------------------------------------------------------------------------------
def f(z):
    return 1.0 / (1.0 - z)

def SM(f, x, h, N):
    "Spectral Method Scheme"
    w = exp(-1j * 2 * pi / N)
    k = n = arange(N)
    f_k = f(x + h * w**k)
    c_n = fft.ifft(f_k)
    a_n = c_n / h ** n
    return a_n * scipy.misc.factorial(n)

def spectral():
    x = 0
    N = 32
    u = exp(-1j * 2 * pi / N)
    c = []
    b = []
    hs = logspace(-18, 6, 1000) 
    alphas, rs = [], []
    efft = []
    for h in hs:
        f_k = array([f(x+h * u**k) for k in arange(0,N)])
        c_n = real(fft.ifft(f_k))
        efft.append(imag(fft.ifft(f_k)))
        c.append(c_n)
        A = c_[ones(N), arange(N)]
        bb = log(abs(c_n))
        xx, _, _, _ = linalg.lstsq(A, bb)
        alpha = exp(xx[0])
        _r = exp(xx[1])
        alphas.append(alpha)
        rs.append(_r)
        b.append(c_n / h ** arange(N))

    c = array(c)
    b = array(b)
    e = abs(array(b) - 1.0)
    efft = array(efft)

    clf()
    axes().set_aspect(1.0)
    ratio = 1.618 * 1.0 # thin 
    gcf().set_figwidth(width_in)
    axis([1e-18, 1e2, 1e-18, 1e-6])
    yscale("log")
    xscale("log")

    for i in [1,2,3,4]:
        plot(hs,e[:,i], color=str(0.2*(i)), label=r"$n="+str(i)+"$")
    xticks([1e-16, 1e-12, 1e-8, 1e-4, 1e0])
    yticks([1e-16, 1e-12, 1e-8], ha="left")
    gca().get_yaxis().set_tick_params(pad=25, direction="out")
    grid(True)
    title(r"Accuracy of $f^{(n)}(0) \simeq \mathrm{SM}(f,0,h,N)[n]$ for $f(z)=1/(1-z)$")
    l = legend(title="$N=32$", loc="center left")
    xlabel("radius $h$")
    ylabel("relative error")
    setp(l.get_texts(), fontsize=10)
    setp(l.get_title(), fontsize=10)

    y_2_x_ratio = 12/20.0
    gcf().set_figheight(width_in * y_2_x_ratio)
    gcf().subplots_adjust(bottom=0.15)
    save("sm-error")

    for i, c in enumerate (real(SM(f, 0, 0.2, 32)[:])):
        pass
        #print r"f^({0})(0)".format(i), "{0:.100g}".format(c),
        #print "rel. error", "{0:.2g}".format(abs(c/scipy.misc.factorial(i) - 1.0))

if __name__ == "__main__":
  fd_value()
  fd_error()
  cd_error()
  #csd_error()
  #csd_error_alt()

  #spectral()

