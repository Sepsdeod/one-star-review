#!/usr/bin/env python3
"""One-Star Review of Something Essential — the sun.

Writes one single-line deadpan one-star review, at most 160 characters,
of an everyday essential to /output/entry.txt.

Angle: filed in earnest against a thing that cannot be fixed — the sun's
one true daily grievance is that it rises straight into your eyes, and
the sting lands in the last few words.
"""

import os

LINE = "The sun rises on time every morning, which would be admirable if it did not insist on doing it directly into my eyes."

OUTPUT_PATH = "/output/entry.txt"
MAX_CHARS = 160


def build_line() -> str:
    """Return the review, validated as a single line within the cap."""
    line = LINE.strip()
    assert "\n" not in line, "entry must be a single line"
    assert 1 <= len(line) <= MAX_CHARS, "entry must be 1-160 characters"
    return line


def main() -> None:
    line = build_line()
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as fh:
        fh.write(line)
    print(f"wrote {len(line)} chars to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
