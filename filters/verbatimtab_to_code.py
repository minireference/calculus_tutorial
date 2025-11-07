#!/usr/bin/env python3
import re
import panflute as pf

# Recognize the raw LaTeX verbatimtab environment with optional \small/\normalsize
VERB_RE = re.compile(
    r'(?s)^\s*(?:\\small\s*)?\\begin{verbatimtab}\s*\n?(.*?)\n?\\end{verbatimtab}\s*(?:\\normalsize\s*)?\s*$'
)

def to_codeblock(text, lang="python"):
    """Create a CodeBlock preserving indentation, quotes, and newlines."""
    code = text.rstrip("\n")
    return pf.CodeBlock(code, classes=[lang])

def concat_text(elems):
    """Flatten a list of inline elements into raw text without escaping."""
    out = []
    for el in elems:
        if isinstance(el, pf.Str):
            out.append(el.text)
        elif isinstance(el, pf.Space):
            out.append(" ")
        elif isinstance(el, pf.SoftBreak):
            out.append("\n")
        elif isinstance(el, pf.LineBreak):
            out.append("\n")
        # ignore formatting (Emph, Strong, etc.)
    return "".join(out)

def convert(elem, doc):

    # --- 1. Raw LaTeX block case ------------------------------------------
    if isinstance(elem, pf.RawBlock) and elem.format in ("latex", "tex"):
        m = VERB_RE.match(elem.text)
        if m:
            return to_codeblock(m.group(1))

    # --- 2. Pandoc Div-based fallback -------------------------------------
    if isinstance(elem, pf.Div) and ("verbatimtab" in elem.classes):
        # Collect all inline elements found inside block elements
        lines = []
        for block in elem.content:
            if isinstance(block, pf.Plain) or isinstance(block, pf.Para):
                lines.append(concat_text(block.content))
            elif isinstance(block, pf.CodeBlock):
                return pf.CodeBlock(block.text, classes=["python"])  # rare case
        return to_codeblock("\n".join(lines))

    # --- 3. Remove size toggles -------------------------------------------
    if isinstance(elem, (pf.RawInline, pf.RawBlock)) and elem.format in ("latex","tex"):
        if elem.text.strip() in (r"\small", r"\normalsize"):
            return []

    return None

if __name__ == "__main__":
    pf.run_filter(convert)
