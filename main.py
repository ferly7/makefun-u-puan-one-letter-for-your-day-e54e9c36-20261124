#!/usr/bin/env python3
"""One Letter for Your Day — make.fun entry.

Writes exactly one letter — Q, for "queue" — to
$MAKEFUN_OUTPUT_DIR/entry.txt (default /output/entry.txt).
One character, nothing else.

Why Q: the day was one queue after another — the build queue,
the ticket queue, the review queue, the coffee queue — and the
letter itself looks like a line of people waiting for a door:
a round room full of them, and one small exit at the bottom.

Deterministic: Python 3 stdlib only, no network, no randomness.
"""

import os

LETTER = "Q"


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LETTER)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
