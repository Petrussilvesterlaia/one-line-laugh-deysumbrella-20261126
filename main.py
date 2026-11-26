#!/usr/bin/env python3
"""One Line, One Laugh - make.fun entry.

Writes one funny line to <MAKEFUN_OUTPUT_DIR>/entry.txt (no trailing
newline), then reads the file back to verify the gate: UTF-8 text,
1-140 characters, not only whitespace, exactly one line.
"""

import os
import sys

LINE = "The pigeon on my balcony stares at me like I owe it rent \u2014 and after three years of free breadcrumbs, it probably does."

MAX_CHARS = 140


def validate(text):
    """Gate check: 1-140 chars, not blank, single line, no trailing newline."""
    if not isinstance(text, str):
        raise ValueError("entry must be text, got %s" % type(text).__name__)
    if not text or not text.strip():
        raise ValueError("entry is empty or only whitespace")
    if len(text) > MAX_CHARS:
        raise ValueError("entry is %d characters, over the 140 cap" % len(text))
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be exactly one line")
    if text != text.strip():
        raise ValueError("entry must not start or end with whitespace")
    return True


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    validate(LINE)
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)
    # Read back and verify what actually landed on disk.
    with open(path, "r", encoding="utf-8", newline="") as f:
        written = f.read()
    validate(written)
    if written != LINE:
        raise ValueError("read-back mismatch")
    print("wrote %d characters to %s" % (len(written), path))
    return 0


if __name__ == "__main__":
    sys.exit(main())
