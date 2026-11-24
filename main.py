#!/usr/bin/env python3
"""Write the one-line cat joke entry to /output/entry.txt."""

import os

JOKE = "I told my cat he was adopted. He blinked once, slowly, and I apologised to a cat."


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    tmp_path = os.path.join(out_dir, ".entry.txt.tmp")
    with open(tmp_path, "w", encoding="utf-8") as f:
        f.write(JOKE)
    os.chmod(tmp_path, 0o644)
    os.replace(tmp_path, os.path.join(out_dir, "entry.txt"))


if __name__ == "__main__":
    main()
