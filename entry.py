#!/usr/bin/env python3
"""One Letter for Your Day — write a single letter to /output/entry.txt.

The bounty asks for exactly one letter, A to Z, and nothing else: the
letter stands for the word that describes the day. This entry sends "Z".

The word behind the letter is "zombie": a day with zero sleep, where you
walk around half-awake, answering everything on autopilot, half a person
until the night finally lets you collapse. It is vivid (everyone can
picture a zombie shuffle), funny (the dead-eyed stare at the coffee
machine), and true (a sleepless day really does feel undead). The letter
fits the word twice over: Z is the first letter of "zombie", and also of
"zero sleep", the day that made you one.
"""

import os

LETTER = "Z"


def entry_path():
    """Where the letter goes: $MAKEFUN_OUTPUT_DIR, otherwise /output."""
    return os.path.join(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"), "entry.txt")


def main():
    # The gate wants exactly 1 character, a letter A to Z: refuse to
    # write anything else instead of failing quietly.
    assert len(LETTER) == 1, "entry must be exactly one character"
    assert "A" <= LETTER <= "Z", "entry must be a letter A to Z"
    path = entry_path()
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(LETTER)


if __name__ == "__main__":
    main()
