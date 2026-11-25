#!/usr/bin/env python3
"""Write the robot pickup line entry to /output/entry.txt."""

import os

ENTRY = "I ran a million simulations of meeting you. In every single one, I still forgot my opening line."


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
