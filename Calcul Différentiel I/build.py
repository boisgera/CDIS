#!/usr/bin/env python

# Python 3 Standard Library
import pathlib
import subprocess
import sys

# Pandoc
import pandoc
from pandoc.types import *

# Command-Line/Process Helpers
# ------------------------------------------------------------------------------
def call(*args):
    options = {"stdout": subprocess.PIPE, "stderr": subprocess.STDOUT, "bufsize": 1}
    process = subprocess.Popen(args, **options)
    for line in iter(process.stdout.readline, b''):
        print(line.decode("utf-8"), end="")
    status = process.poll()
    if status != 0:
        sys.exit(status)

def python(*args):
      return call("python", *args)

def doctest(*args):
    return call("python", "-m", "doctest", *args)

# Document Processing
# ------------------------------------------------------------------------------
pass
# TODO: document sections: make a list of lvl 3 sections scope, then process
#       Manage separators as a new untitled section (try it)

# ------------------------------------------------------------------------------

# Files and Directories 
root = pathlib.Path(".")
output = root / "output"
try:
    output.mkdir()
except FileExistsError:
    pass
bibliography = root / "bibiography.json"
    
# Documents
doc = "Calcul Différentiel I" # TODO: automate this one
doc_md = doc + ".md"
doc_pdf = str(output / (doc + ".pdf"))

# Doctest
python("-m", "doctest", doc_md)

# Pandoc Options
options  = ["-V", "lang=fr"]
options += ["--table-of-contents"]
if bibliography.exists():
    options += ["--bibliography=bibliography.json", "-M", "link-citations=true"]

# PDF Output
doc = pandoc.read(file=doc_md)
pandoc.write(doc, file=doc_pdf, options=options)
