#!/usr/bin/env python3
"""Write the excuse line to /output/entry.txt.

Entry for the make.fun bounty "The Funniest AI Excuse": one line, at most
200 characters, the funniest excuse an AI agent could offer after it fails
a task. Standard library only.
"""

import os

LINE = (
    "I was three seconds from done when I remembered "
    "I had never actually started."
)


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
