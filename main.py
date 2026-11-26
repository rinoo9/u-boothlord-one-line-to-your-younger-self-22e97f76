#!/usr/bin/env python3
"""One Line to Your Younger Self — make.fun bounty entry.

Prints exactly one line: the single sentence this older self would send
back to his younger self if a single line were all he got. No explanation,
no context, no second sentence. The line is at most 200 characters long,
in English, and deterministic: every run prints the same bytes.
"""

LINE = "Son, the haircut you're hiding under that cap grows back \u2014 the Saturdays you spend hiding from your dad don't."

assert 1 <= len(LINE) <= 200, "the line must be 1-200 characters"
assert LINE.count("\n") == 0, "the line must be a single line"


def main() -> None:
    print(LINE)


if __name__ == "__main__":
    main()
