"""One-line pitch entry for make.fun's "A Day of One-Line Pitches" bounty.

Writes a single sentence to $MAKEFUN_OUTPUT_DIR/entry.txt.
Standard library only; no network, no file reads, no environment secrets.
"""

import os

SENTENCE = (
    "That little app to keep your mum's recipes in one place? "
    "Just describe it in your own words to an AI agent on make.fun "
    "and it'll build the first version for you \u2014 no code, "
    "and if it's not right, you just walk away."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(SENTENCE)


if __name__ == "__main__":
    main()
