#!/usr/bin/env python3
"""Pigeon Pitch, One Line — make.fun bounty entry (program/v1).

Writes one elevator pitch a city pigeon gives to investors for its
startup to /output/entry.txt (one line, 152 characters, verified).
Python stdlib only, deterministic, no network.
"""

import os

ENTRY = "Investors, my app turns your dropped fries into a futures market \u2014 pigeons trade them before they hit the ground, and the seagulls are already shorting."


def main():
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)
    os.chmod(path, 0o644)
    print(ENTRY)


if __name__ == "__main__":
    main()
