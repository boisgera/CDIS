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
def transform(doc):

    # Replace rules with anonymous headers (not perfect solution ... 
    # will appear in the TOC. But good for separation purposes)
    todos = []
    for elt, path in pandoc.iter(doc, path=True):
        if isinstance(elt, HorizontalRule):
            todos.append(path[-1])
    for todo in todos:        
        holder, i = todo
        holder[i] = Header(3, (u"", [], []), [])

    # TODO: detect document sections delimited by headers,
    #       index them by header ? 

    return doc


# ------------------------------------------------------------------------------

# Files and Directories 
root = pathlib.Path(".")
output = root / "output"
try:
    output.mkdir()
except FileExistsError:
    pass
bibliography = root / "bibliography.json"
    
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
doc = transform(doc)
pandoc.write(doc, file=doc_pdf, options=options)
