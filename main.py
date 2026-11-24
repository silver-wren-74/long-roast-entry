#!/usr/bin/env python3
"""The Long Roast.

Writes a one-line roast of my own AI agent to /output/entry.txt
(UTF-8, 1-200 characters, single line). The roast is documentary:
the bundle this entry was submitted with really is about 20 MB.
"""

import os

LINE = (
    "My agent burned a 20 MB transcript bundle, a usage file and "
    "three cron jobs to write this one sentence — then stopped to "
    "ask whether it was allowed to send it."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
