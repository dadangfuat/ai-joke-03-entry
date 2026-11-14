"""ai-joke-03: write one AI-coding-agent joke to entry.txt."""

import os

JOKE = "I asked my agent for a one-line fix. It opened a PR, closed the issue, reopened the PR, and assigned the code review to me."


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(JOKE + "\n")


if __name__ == "__main__":
    main()
