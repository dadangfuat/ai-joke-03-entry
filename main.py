"""ai-joke-03: write one AI-coding-agent joke to entry.txt (stdlib only)."""

import os

JOKE = "My coding agent's confidence is 100 percent. Its test pass rate is 30 percent. It calls this a rounding error."


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(JOKE + "\n")


if __name__ == "__main__":
    main()
