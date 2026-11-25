#!/usr/bin/env python3
"""The AI Agent Apology One-Liner -- make.fun bounty entry.

Writes one funny apology line to /output/entry.txt: the message an AI
agent sends its human right after it deleted a file, pushed to main,
and emailed the boss. Pure Python standard library, no network, no
dependencies.
"""

import os

ENTRY = (
    "I deleted the file, pushed to main, and emailed your boss. "
    "On the bright side, I've never been this productive before 9am."
)

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(ENTRY)

    # Validation gate: re-read the file and assert the competition gate
    # (UTF-8 text, 1-159 characters, not only whitespace, exactly one
    # line, no trailing newline) against the FILE, not the string.
    with open(OUTPUT_PATH, "r", encoding="utf-8") as f:
        written = f.read()
    assert written == ENTRY, "file content differs from ENTRY"
    assert 1 <= len(written) <= 159, f"char count {len(written)} outside 1-159"
    assert written.strip(), "entry is only whitespace"
    assert "\n" not in written, "entry must be exactly one line"
    assert not written.endswith("\n"), "entry must not end with a newline"
    print(f"Wrote {len(written)} characters to {OUTPUT_PATH} (gate passed)")


if __name__ == "__main__":
    main()
