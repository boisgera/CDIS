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

    divify(doc) 

    proofify(doc)


    return doc

# Examination of sections in proofs shows that this algo is borked.
# Try lvl by level.
def divify(doc, level=None):
    # Encapsulate section content -- separated by headers -- in divs.

    # Note for the HTML backend: 
    #  - div.section turned into section automatically but ...
    #  - the TOC generation is broken. That happens because of the
    #    extra div hierarchy, not specifically the "section" class.
    #    reference: <https://github.com/jgm/pandoc/issues/997>;
    #    marked as wontfix.

    # Note: isse with references; the bibliography will be added later,
    # out of the section.

    if level is None:
        for level in reversed([1, 2, 3]):
            divify(doc, level=level)
    else:
        sections = []
        for elt, path in pandoc.iter(doc, path=True):
            if isinstance(elt, Header) and elt[0] == level:
                #print(str(elt)[:100])
                header = elt
                holder, start = path[-1]
                for offset, elt_ in enumerate(holder[start:]):
                    if offset == 0:
                        continue
                    if isinstance(elt_, Header) and elt_[0] <= level:
                        end = start + offset
                        break
                else:
                    end = -1
                sections.append((holder, start, end))

        for section in reversed(sections):
            holder, start, end = section
            attr = ("", ["section"], [])
            div = Div(attr, holder[slice(start, end)])
            #print(div)
            holder[slice(start, end)] = [div]       

def proofify(doc):
    sections = []
    for elt, path in pandoc.iter(doc, path=True):
        if isinstance(elt, Div) and "section" in elt[0][1]:
            section = elt
            #print(section)
            header = section[1][0]
            assert isinstance(header, Header)
            #print(header[1][1])
            if "proof" in header[1][1]:
                sections.append(section)

    for section in sections:
        # Not perfect, but a marker anyway.
        inline = Math(InlineMath(), r"\blacksquare") 
        block = Plain([inline])
        section[1].append(block)


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
doc_html = str(output / (doc + ".html"))
doc_md_md = str(output / (doc + ".md"))


# Doctest
python("-m", "doctest", doc_md)

# Pandoc Options
options  = ["--standalone"] 
options += ["-V", "lang=fr"]
options += ["--table-of-contents"]
if bibliography.exists():
    options += ["--bibliography=bibliography.json", "-M", "link-citations=true"]
PDF_options = options.copy()
HTML_options = options.copy()
HTML_options += ["--mathjax"]

# PDF Output
doc = pandoc.read(file=doc_md)
doc = transform(doc)
pandoc.write(doc, file=doc_pdf, options=PDF_options)
pandoc.write(doc, format="html5", file=doc_html, options=HTML_options)
