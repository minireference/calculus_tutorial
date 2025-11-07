#!/usr/bin/env bash
set -e

# Ensure output directory exists
mkdir -p md

# Python filter for removing \label{...}
FILTER=""

for SRC in "$@"; do
    BASENAME="$(basename "$SRC" .tex)"
    OUTFILE="md/${BASENAME}.md"

    pandoc "$SRC" \
        -f latex \
        -t markdown-simple_tables-multiline_tables-grid_tables-auto_identifiers-implicit_header_references \
        --wrap=preserve \
        --filter ./filters/verbatimtab_to_code.py \
        --filter ./filters/remove_labels.py \
        -o "$OUTFILE"

    echo "Converted $SRC → $OUTFILE"
done

