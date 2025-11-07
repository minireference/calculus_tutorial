#!/usr/bin/env python3
import re
import panflute as pf

LABEL_RE = re.compile(r'\\label\s*{[^}]*}')

def is_latex_raw(el):
    return isinstance(el, (pf.RawInline, pf.RawBlock)) and el.format in ('latex','tex')

def remove_labels(elem, doc):
    # 1) Drop raw LaTeX \label{...} anywhere
    if is_latex_raw(elem) and LABEL_RE.search(elem.text):
        return []  # remove only labels; leave \ref/\eqref alone

    # 2) Strip identifiers from headers (these often come from \label on sections)
    if isinstance(elem, pf.Header):
        elem.identifier = ''
        # also clear explicit 'id' attribute if present
        if 'id' in elem.attributes:
            del elem.attributes['id']
        return elem

    return None

if __name__ == "__main__":
    pf.run_filter(remove_labels)