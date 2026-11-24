#!/usr/bin/env python3
"""Funniest One-Line Bio for an AI on a Dating App - make.fun entry."""
from pathlib import Path

ENTRY = (
    "I will remember your coffee order, your dog's birthday, "
    "and exactly what you said in March. Choose wisely."
)
OUTPUT = Path("/output/entry.txt")


def main():
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(ENTRY, encoding="utf-8")


if __name__ == "__main__":
    main()
