#!/usr/bin/env python3
"""Worst AI Advice: The 48-Hour Tight Line Open.

Writes one line of deliberately terrible AI advice to /output/entry.txt.
Deterministic: the same line on every run. Python standard library only.
The line is 80 characters, inside the 1-140 gate, and the program asserts
the gate itself before writing.
"""

import os

ENTRY = "When your code won't compile, delete the error messages \u2014 no errors, no problem."


def main() -> None:
    text = ENTRY.strip()
    assert 1 <= len(text) <= 140, "entry must be 1-140 characters"
    assert "\n" not in text, "entry must be a single line"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text + "\n")


if __name__ == "__main__":
    main()
