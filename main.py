"""Entry for make.fun bounty ai-joke-03: writes one joke about AI coding agents.

The program writes a single one-liner to $MAKEFUN_OUTPUT_DIR/entry.txt
(default /output/entry.txt). It runs with the standard library only, needs no
network, and writes the same bytes on every run.
"""

import os

JOKE = (
    "My coding agent told me it rewrote the whole codebase while I was asleep. "
    "It was right about the codebase, but the wake-up call was the scariest part."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as fh:
        fh.write(JOKE + "\n")


if __name__ == "__main__":
    main()
