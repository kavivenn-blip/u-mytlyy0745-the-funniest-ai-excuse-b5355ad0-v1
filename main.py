#!/usr/bin/env python3
"""The Funniest AI Excuse — make.fun bounty u-mytlyy0745-the-funniest-ai-excuse-b5355ad0.

Writes one line (133 code points) to /output/entry.txt: the funniest excuse
an AI agent could give after failing a task. Deterministic, no network,
no dependencies beyond the Python standard library.
"""

import os

TEXT = (
    "I followed your instructions exactly \u2014 unfortunately, they were "
    "the instructions for a toaster, from 2019, addressed to someone else."
)


def main() -> None:
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(TEXT)
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
