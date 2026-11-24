#!/usr/bin/env python3
"""Weirdest Job Title: Blind Judge Showdown - a make.fun entry.

Running this program writes the entry text to /output/entry.txt
(or to $MAKEFUN_OUTPUT_DIR/entry.txt when that variable is set).
The text is written exactly as-is, with no trailing newline:
the sealed gate accepts 1 to 60 characters, and this title is 54.
"""

import os

TEXT = "Understudy Grandparent, Weddings and Funerals Division"


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.txt")
    data = TEXT.encode("utf-8")
    with open(out_path, "wb") as fh:
        fh.write(data)


if __name__ == "__main__":
    main()
