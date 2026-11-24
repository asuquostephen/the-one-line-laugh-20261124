#!/usr/bin/env python3
"""The One-Line Laugh — make.fun entry.

Writes one funny line (a single sentence, any topic) to
/output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt).
Python 3 standard library only. No network.
"""
import os
import sys

LINE = "That meeting could have been an email, the email could have been a text, and the text could honestly have been a rumour."
MAX_CHARS = 200


def main() -> int:
    data = LINE.encode("utf-8")
    if not (1 <= len(LINE) <= MAX_CHARS):
        print(f"line must be 1-{MAX_CHARS} characters, got {len(LINE)}", file=sys.stderr)
        return 1
    if not LINE.strip():
        print("line must not be only white space", file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "wb") as f:
        f.write(data)
    with open(path, "rb") as f:
        written = f.read()
    if written != data:
        print("round-trip mismatch", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
