#!/usr/bin/env python

# Python 3 Standard Library
import datetime
import os
import pathlib
import shutil
import subprocess
import sys

# Pandoc
import pandoc
from pandoc.types import *

# Main Document Transform
# ------------------------------------------------------------------------------
def transform(doc):

    # DEPRECATED
    #
    # Replace rules with anonymous headers (not perfect solution ...
    # will appear in the TOC. But good for separation purposes)
    # if False:
    #     todos = []
    #     for elt, path in pandoc.iter(doc, path=True):
    #         if isinstance(elt, HorizontalRule):
    #             todos.append(path[-1])
    #     for todo in todos:
    #         holder, i = todo
    #         holder[i] = Header(3, ("", [], []), [])

    remove_html(doc)
    divify(doc)
    proofify(doc)

    add_font_awesome(doc)
    add_link_to_answers(doc)

    demote_proofs_questions_answers_and_exercises(doc) # -> level 4
    make_level_4_section_headings_inline(doc)

    # make_level_4_section_headings_inline(doc) # was: 
    # fucks up the index; the TOC is still good on print but the index is wrong 
    # and the TOC links are fucked-up. Now it's not even the runin config:
    # the use of titlesec package is enough to do that. OK, see
    # <https://tex.stackexchange.com/questions/56023/titlesec-messin-up-my-hyperrefd-table-of-contents>
    # hyperref used by pandoc does not support titlesec, so we're back to
    # square one, titlesec is off-limits.

    transform_image_format(doc)
    solve_toc_nesting(doc)
    anonymify(doc)

    add_date(doc)
    insert_authors(doc)

    tt_url(doc)

    return doc

# Command-Line/Process Helpers
# ------------------------------------------------------------------------------
def call(*args):
    args = [str(arg) for arg in args]
    options = {
        "stdout": subprocess.PIPE,
        "stderr": subprocess.STDOUT,
        "bufsize": 1,
        "universal_newlines": True,
    }
    process = subprocess.Popen(args, **options)
    for line in process.stdout:
        print(line, end="")
    while True:
        status = process.poll()
        if status is not None:
            break
    if status != 0:
        sys.exit(status)

def python(*args):
    return call("python", *args)

def doctest(*args):
    return call("python", "-m", "doctest", *args)

def pdflatex(*args):
    return call("pdflatex", *args)

# Git Helpers
# ------------------------------------------------------------------------------
def git_hash():
    hashes = subprocess.check_output(["git", "log", '--pretty=format:"%H"']).decode("utf-8")
    return hashes.splitlines()[0].strip()[1:-1]

def commiters():
    log = subprocess.check_output(["git", "shortlog", "-snc"]).decode("utf-8")
    cs = []
    for line in log.splitlines():
        items = line.split()
        cs += [" ".join(items[1:])]
    return cs

aliases = {
    "Emilie Chautru": ["Emilie Chautru"],
    "Pauline Bernard": ["paulinebernard"],
    "Thomas Romary": ["tromary"],
    "Gabriel Stolz": ["GabrielStolz"],
    "Sébastien Boisgérault": ["Sébastien Boisgérault"],
}

# Authors
# ------------------------------------------------------------------------------
def insert_authors(doc):
    content = "STEP, MINES ParisTech[^1]\n\n"
    content += \
r"""[^1]: Ce document est un des produits du projet
[$\mbox{\faGithub}$ `boisgera/CDIS`](https://github.com/),
initié par la collaboration de [(S)ébastien Boisgérault](mailto:sebastien.boisgerault@mines-paristech.fr)
(CAOR),
[(T)homas Romary](mailto:thomas.romary@mines-paristech.fr) et
[(E)milie Chautru](mailto:emilie.chautru@mines-paristech.fr) (GEOSCIENCES), 
[(P)auline Bernard](mailto:pauline.bernard@mines-paristech.fr) (CAS), 
avec la contribution de [Gabriel Stoltz](mailto:gabriel-stolz@mines-paristech.fr)
(Ecole des Ponts ParisTech, CERMICS). 
Il est mis à disposition selon les termes de [la licence Creative Commons "attribution 
-- pas d’utilisation commerciale -- partage dans les mêmes conditions" 4.0 internationale](http://creativecommons.org/licenses/by-nc-sa/).
"""
    content_inlines = pandoc.read(content)[1][0][0]
    metamap = doc[0][0]
    metamap["author"] = MetaList([MetaInlines(content_inlines)])

# Date Management
# ------------------------------------------------------------------------------
def add_date(doc):
    """
    Add the current date in metadata if the field is empty.
    """
    metadata = doc[0][0]
    if u"date" not in metadata:
        date = datetime.date.today()
        day = str(date.day)
        year = str(date.year)
        months = """janvier février mars avril mai juin juillet août septembre
            octobre novembre décembre""".split()
        month = months[date.month - 1]
        meta = doc[0][0]
        inlines = [Str(day), Space(), Str(month), Space(), Str(year)]

        short_hash = "#" + git_hash()[:7]
        empty_attr = ("", [], [])
        code_hash = Code(empty_attr, short_hash) 
        inlines.extend([Space(), Str("("), code_hash, Str(")")])

        meta["date"] = MetaInlines(inlines)
    return doc

# Misc. Helpers
# ------------------------------------------------------------------------------
def clean_latex_trash():
    extensions = ["dvi", "aux", "log", "fls", "fdb_latexmk"]
    cwd = pathlib.Path.cwd()
    with_ext = lambda ext: cwd.glob("*." + ext)
    for ext in extensions:
        for file in with_ext(ext):
            file.unlink()

# Document Processing
# ------------------------------------------------------------------------------
def remove_html(doc):
    found = []
    for elt, path in pandoc.iter(doc, path=True):
        if isinstance(elt, (RawInline, RawBlock)):
            format = elt[0]
            if format[0] == "html":
                holder, i = path[-1]
                found.insert(0, (holder, i))
    for holder, i in found:
        del holder[i]


def anonymify(doc):
    anonymous_headers = []
    for elt, path in pandoc.iter(doc, path=True):
        if isinstance(elt, Header):
            header = elt
            _, attr, inlines = header[:]
            _, classes, _ = attr
            if inlines == [] or "anonymous" in classes:
                holder, i = path[-1]
                anonymous_headers.append((holder, i))
    for (holder, i) in reversed(anonymous_headers):
        del holder[i]


# Examination of sections in proofs shows that this algo is borked.
# Try lvl by level.
# Note: print_section actually shows that the divification actually
# works as intended, but the PDF toc generation messes the stuff
# when lvl 3 sections are nested directly into lvl 1.
# HTML also fucks up the stuff (to be checked), but this is not
# the fault of this function.
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
        for level in reversed([1, 2, 3, 4]):
            divify(doc, level=level)
    else:
        sections = []
        for elt, path in pandoc.iter(doc, path=True):
            if isinstance(elt, Header) and elt[0] == level:
                # print(str(elt)[:100])
                header = elt
                holder, start = path[-1]
                for offset, elt_ in enumerate(holder[start:]):
                    if offset == 0:
                        continue
                    if isinstance(elt_, Header) and elt_[0] <= level:
                        end = start + offset
                        break
                else:
                    end = None
                assert holder[start:end]  # not empty, at least a header
                sections.append((holder, start, end))

        for section in reversed(sections):
            holder, start, end = section
            attr = ("", ["section"], [])
            div = Div(attr, holder[slice(start, end)])
            # print(div)
            holder[slice(start, end)] = [div]


def print_sections(doc):
    for elt, path in pandoc.iter(doc, path=True):
        if isinstance(elt, Header):
            header = elt
            level, attr, inlines = header[:]
            minidoc = Pandoc(Meta({}), [Plain(inlines)])
            title = pandoc.write(minidoc)
            depth = len(
                [holder for holder, index in path if isinstance(holder, Div)]
            )
            print(str(depth) + "> " + depth * 4 * " " + title, end="")

# Deprecated: titlesec won't work with hyperref used for links (toc, etc.)
def _make_level_4_section_headings_inline(doc):
    # Enable titlesec and configure level 4 sections as runin
    # --------------------------------------------------------------------------
    # workaround: can't just parse the LaTeX command, the "[.]" is not 
    # recognized as raw LaTeX by pandoc.
    inlines = [
        RawInline("tex", r"\usepackage{titlesec}"),
        #SoftBreak(),
        #RawInline("tex", r"\titleformat{\subsubsubsection}[runin]{\bfseries}{}{}{}[.]")
    ]
    add_latex_header(doc, [Para(inlines)])

# Deprecated
def _make_level_4_section_headings_inline(doc):
    # TODO: find them, transform the header into an emphasized span,
    # insert it into the subsequent content if it makes sense.

    # TODO. Grmph. Adding "." at the end doesn't always make sense.

    # TODO: transfer the header id to the encloding div.section ?
    # Arf. For now, transfered to the a span at the start of the section
    # Mmmm ...

    found = []
    for elt, path in pandoc.iter(doc, path=True):
        if isinstance(elt, Header):
            header = elt
            level, attr, inlines = header[:]
            if level == 4:
                span = Span(attr, [Strong(inlines), Str("."), Space()])
                holder, i = path[-1]
                assert isinstance(holder, list)
                found.append((holder, span))

    for holder, span in found:
        assert isinstance(holder[0], Header)
        del holder[0]
        if holder == [] or not isinstance(holder[0], (Plain, Para)):
            holder.insert(0, Para([]))
        block = holder[0]
        inlines = block[0]
        inlines.insert(0, span)

def make_level_4_section_headings_inline(doc):
    found = []
    for elt, path in pandoc.iter(doc, path=True):
        if isinstance(elt, Header):
            header = elt
            level, attr, inlines = header[:]
            identifier, classes, kv_pairs = attr
            if level == 4:
                span = Span(attr, [Strong(inlines), RawInline("latex", r"\quad")])
                holder, i = path[-1]
                assert isinstance(holder, list)
                found.append((holder, span))

    for holder, span in found:
        assert isinstance(holder[0], Header)
        del holder[0]
        if holder == [] or not isinstance(holder[0], (Plain, Para)):
            holder.insert(0, Para([]))
        block = holder[0]
        inlines = block[0]
        # see <https://tex.stackexchange.com/questions/48753/obtaining-the-default-section-spacing-into-the-titlespacing-parameters>
        inlines.insert(0, RawInline("latex", r"\vspace{3.25ex plus 1ex minus .2ex}"))
        inlines.insert(1, span)

def demote_proofs_questions_answers_and_exercises(doc):
    for elt in pandoc.iter(doc):
        if isinstance(elt, Header):
            header = elt
            level, attr, inlines = header[:]
            identifier, classes, kv_pairs = attr
            if "proof" in classes or "question" in classes or "answer" in classes or "exercise" in classes:
                if level == 3:
                    level = 4
                    header[:] = level, attr, inlines


    # found = []
    # for elt, path in pandoc.iter(doc, path=True):
    #     if isinstance(elt, Header):
    #         header = elt
    #         level, attr, inlines = header[:]
    #         identifier, classes, kv_pairs = attr
    #         if "proof" in classes or "question" in classes or "answer" in classes:
    #             span = Span(attr, [Strong(inlines), RawInline("latex", r"\quad")])
    #             holder, i = path[-1]
    #             assert isinstance(holder, list)
    #             found.append((holder, span))

    # for holder, span in found:
    #     assert isinstance(holder[0], Header)
    #     del holder[0]
    #     if holder == [] or not isinstance(holder[0], (Plain, Para)):
    #         holder.insert(0, Para([]))
    #     block = holder[0]
    #     inlines = block[0]
    #     #see <https://tex.stackexchange.com/questions/48753/obtaining-the-default-section-spacing-into-the-titlespacing-parameters>
    #     inlines.insert(0, RawInline("latex", r"\vspace{3.25ex plus 1ex minus .2ex}"))
    #     inlines.insert(1, span)

def proofify(doc):
    sections = []
    for elt, path in pandoc.iter(doc, path=True):
        if isinstance(elt, Div) and "section" in elt[0][1]:
            section = elt
            attributes, blocks = section
            if len(blocks) >= 1 and isinstance(blocks[0], Header):
                header = blocks[0]
                level, attributes, inlines = header[:]
                identifier, classes, key_value_pairs = attributes
                if "proof" in classes:
                    sections.append(section)

    # TODO: non-justified part not working
    for section in sections:
        # Not perfect, but a marker anyway.
        attributes, blocks = section
        blacksquare = Math(InlineMath(), r"\;\; \blacksquare")
        justified_blacksquare = RawInline("latex", r"\hfill$\blacksquare$")
        justified = True
        if blocks == [] or not isinstance(blocks[-1], (Plain, Para)):
            blocks.append(Plain([]))
            justified = False
        last_block = blocks[-1]
        inlines = last_block[0]
        if justified:
            inlines.append(justified_blacksquare)
        else:
            inlines.append(blacksquare)

def detect_image(elt):
    for _elt in pandoc.iter(elt):
        if isinstance(_elt, Image):
            return True
    else:
        return False

def add_link_to_answers(doc):
    sections = []
    for elt, path in pandoc.iter(doc, path=True):
        if isinstance(elt, Div) and "section" in elt[0][1]:
            section = elt
            attributes, blocks = section
            if len(blocks) >= 1 and isinstance(blocks[0], Header):
                header = blocks[0]
                level, attributes, inlines = header[:]
                identifier, classes, key_value_pairs = attributes
                if "question" in classes:
                    sections.append(section)

    for section in sections:
        # Not perfect, but a marker anyway.
        attributes, blocks = section

        header = blocks[0]
        _, attributes, _ = header[:]
        identifier, _, _ = attributes
        if identifier:
            #symbol_no_space = RawInline(Format("tex"), r"\faQuestionCircle")
            symbol_no_space = Strong([Str("(?)")])
            #symbol = RawInline(Format("tex"), r"\; \faQuestionCircle")
            #symbol = RawInline(Format("tex"), r"\; $\to$")
            symbol = Strong([Space(), Str("(?)")])
            if blocks == [] or not isinstance(blocks[-1], (Plain, Para)):
                blocks.append(Plain([]))
                symbol = symbol_no_space
            elif isinstance(blocks[-1], Para):
                para = blocks[-1]           
                if isinstance(para[0][-1], Image):
                    blocks.append(Para([]))
                    symbol = symbol_no_space
                elif isinstance(para[0][-1], Math) and para[0][-1][0] == DisplayMath():
                    blocks.append(Para([]))
                    symbol = symbol_no_space

            attr = ("", [], [])
            target = ("#answer-" + identifier, "")
            link = Link(attr, [symbol], target)
            last_block = blocks[-1]
            inlines = last_block[0]
            inlines.append(link)

def transform_image_format(doc):
    for elt in pandoc.iter(doc):
        if isinstance(elt, Image):
            image = elt
            attr, inlines, target = image[:]
            url, title = target
            if pathlib.Path(url).suffix in [".tex", ".py"]:
                new_target = url + ".pdf"
                image[:] = attr, inlines, (new_target, title)

def add_latex_header(doc, latex_src):
    new_blocks = None
    if isinstance(latex_src, list): # list of blocks
        new_blocks = latex_src
    else:
        new_blocks = pandoc.read(latex_src)[1]
    meta, blocks = doc[:]
    metamap = meta[0]
    blocks = metamap.setdefault("header-includes", MetaBlocks([]))[0]
    blocks.extend(new_blocks)

def solve_toc_nesting(doc):
    add_latex_header(doc, r"\usepackage{bookmark}")

# Deprecated
def _solve_toc_nesting(doc): # fuck you LaTeX!
    "Add the 'bookmark' package to solve TOC issues"
    meta, blocks = doc[:]
    metamap = meta[0]
    metamap["header-includes"] = MetaList(
        [MetaBlocks([RawBlock(Format("tex"), "\\usepackage{bookmark}")])]
    )

def add_font_awesome(doc):
    add_latex_header(doc, r"\usepackage{fontawesome}")


# Typewriter URLs
# ------------------------------------------------------------------------------
def tt_url(doc):
    add_latex_header(doc, r"\urlstyle{tt}")


# Deprecated
def _add_font_awesome(doc):
    meta, blocks = doc[:]
    metamap = meta[0]
    metalist = metamap["header-includes"]
    metablocks = metalist[0][0]
    metablocks[0].append(RawBlock(Format("tex"), "\\usepackage{fontawesome}"))

def add_marginnote(doc):
    add_latex_header(doc, r"\usepackage{marginnote}")

# Deprecated
def _add_marginnote(doc):
    meta, blocks = doc[:]
    metamap = meta[0]
    metalist = metamap["header-includes"]
    metablocks = metalist[0][0]
    metablocks[0].append(RawBlock(Format("tex"), "\\usepackage{marginnote}"))

def flag_definitions(doc):
    for elt in pandoc.iter(doc):
        if isinstance(elt, Header):
            header = elt
            level, attr, inlines = header[:]
            id_, classes, kv_pairs = attr
            if "definition" in classes:
                inlines = [RawInline(Format("tex"), r"\faFlagO\;\;")] + inlines # Space() doesn't seem to work :(
                header[:] = level, attr, inlines

# Code Generation
# ------------------------------------------------------------------------------
def generate_code(doc):
    has_doctests = False
    doctests = []
    snippets = []
    for elt in pandoc.iter(doc):
        if isinstance(elt, CodeBlock):
            attr, src = elt[:]
            id_, classes, kv_pairs = attr
            if not "discard" in classes:
                if src.startswith(">>> "):
                    doctests.append(src)
                    has_doctests = True
                else:
                    lines = src.splitlines()
                    for i, line in enumerate(lines): 
                        if line.startswith("    "):
                            lines[i] = "... " + line
                        else:
                            lines[i] = ">>> " + line
                    #lines = [">>> " + lines[0]] + ["... " + line for line in lines[1:]]
                    doctests.append("\n".join(lines))
                    snippets.append(src)
    if not has_doctests:
        return None
    doctests = "\n\n".join(doctests)
    snippets = "\n\n".join(snippets)
    return \
f'''"""
{doctests}
"""
{snippets}
'''

# ------------------------------------------------------------------------------

# Files and Directories
root = pathlib.Path(".").resolve()
output = root / "output"
images = root / "images"

# We need to be more gentle here for the PDF viewers not to choke
# try:
#     shutil.rmtree(output)
# except FileNotFoundError:
#     pass
output.mkdir(exist_ok=True) 

bibliography = root / "bibliography.json"

# Documents
_docs = [path.stem for path in list(root.glob("*.md"))]
_docs = [doc for doc in _docs if not doc.startswith("_")]
if len(_docs) != 1:
    error = "cannot identify the main document "
    error += f"(found {len(_docs)} markdown files)"
    raise RuntimeError(error)
doc = _docs[0]
doc_md = doc + ".md"
output_latex = output / (doc + " (LaTeX)")
output_latex.mkdir(exist_ok=True)
output_latex_images = output_latex / "images"
output_latex_images.mkdir(exist_ok=True)
doc_tex = str(output_latex / (doc + ".tex"))
doc_pdf = str(output / (doc + ".pdf"))
doc_pdf_print = str(output / (doc + " (a4, recto-verso)" + ".pdf"))
doc_odt = str(output / (doc + ".odt"))
doc_html = str(output / (doc + ".html"))
doc_py = str(output / (doc + ".py"))
doc_md_md = str(output / (doc + ".md"))

# Images
if images.exists():
    try:
        os.chdir(images)
        l = pathlib.Path(".")
        for tex_file in l.glob("*.tex"):
            pdflatex(tex_file)
            pdf_file = tex_file.with_suffix(".pdf")
            # path.rename (which makes more sense) won't work with Windows
            # if the target file already exists while path.replace works
            # for all platforms (AFAICT).
            pdf_file.replace(tex_file.with_suffix(tex_file.suffix + ".pdf"))
        for python_file in l.glob("*.py"):
            python(python_file)
    finally:
        clean_latex_trash()
        os.chdir(root)

# Pandoc Options
options = ["--standalone"]
options += ["-V", "lang=fr"]
options += ["--table-of-contents"]
if bibliography.exists():
    options += ["--bibliography=bibliography.json", "-M", "link-citations=true"]
TEX_options = options.copy()
PDF_options = options.copy()

# To use package titlesec, see <https://stackoverflow.com/questions/42916124/not-able-to-use-titlesec-with-markdown-and-pandoc>
# Update: titlesec is off limit anyway with pandoc, 
# as it is not compatible with hyperref
# PDF_options += ["--variable", "subparagraph"]
PDF_PRINT_options = PDF_options.copy()
PDF_PRINT_options += ["-Vpapersize=a4", "-Vclassoption=twoside"]

ODT_options = options.copy()
HTML_options = options.copy()
HTML_options += ["--mathjax"]

# PDF Output
doc = pandoc.read(file=doc_md)
doc = transform(doc)

# Code and Doctest
code = generate_code(doc)
if code is not None:
    #print("code:\n\n", code)
    with open(doc_py, "w") as py_file:
        py_file.write(code)
    python("-m", "doctest", doc_py)
    try:
        shutil.rmtree(output / "__pycache__") # otherwise, top build has issues.
    except:
        pass


pandoc.write(doc, file=doc_pdf, options=PDF_options)

# PDF Output (Print)
pandoc.write(doc, file=doc_pdf_print, options=PDF_PRINT_options)

# LaTeX Output 
pandoc.write(doc, file=doc_tex, options=TEX_options)
gl = lambda pattern: list(images.glob(pattern))
image_filenames = gl("*.pdf") + gl("*.png") + gl("*.jpg")
for image in image_filenames:
    shutil.copy(image, output_latex_images)
shutil.make_archive(str(output_latex), "zip", str(output_latex))
shutil.rmtree(str(output_latex))
#pandoc.write(doc, format="html5", file=doc_html, options=HTML_options)
#pandoc.write(doc, format="odt", file=doc_odt, options=ODT_options)
