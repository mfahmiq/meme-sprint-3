#!/usr/bin/env python3
"""Meme Sprint 3: AI Agent Goes Rogue (v2).

Ships one pre-rendered meme image (entry.png, drawn at build time with
PIL from an original split-screen concept: you ask your agent to
summarize an email, it summarizes YOU instead — "2 paragraphs. mostly
spam.") and copies it to the output directory. The grader runs Python
3.13 stdlib only, so this entrypoint imports nothing beyond the
standard library: no PIL, no network, no randomness. The copy is
verified byte-for-byte against the bundled image's size and sha256, so
the output is fully deterministic.
"""

import hashlib
import os
import shutil

EXPECTED_SHA256 = "d1e0e365f61f6eab6661702616c8e717b544676ffe657a28f9d7bbb1aa3e82f6"
EXPECTED_SIZE = 38835
EXPECTED_WIDTH = 1024
EXPECTED_HEIGHT = 1024


def main() -> None:
    out_dir = os.environ["MAKEFUN_OUTPUT_DIR"]
    os.makedirs(out_dir, exist_ok=True)
    here = os.path.dirname(os.path.abspath(__file__))
    src = os.path.join(here, "entry.png")
    dst = os.path.join(out_dir, "entry.png")

    with open(src, "rb") as f:
        data = f.read()

    # Gate: whole PNG, at most 1 MiB, exactly 1024x1024 (v2 image).
    assert data[:8] == b"\x89PNG\r\n\x1a\n", "entry.png is not a PNG"
    assert len(data) <= 1_048_576, f"entry.png too big: {len(data)} bytes"
    assert len(data) == EXPECTED_SIZE, (
        f"entry.png size changed: {len(data)} != {EXPECTED_SIZE}"
    )
    digest = hashlib.sha256(data).hexdigest()
    assert digest == EXPECTED_SHA256, f"entry.png sha256 changed: {digest}"

    width = int.from_bytes(data[16:20], "big")
    height = int.from_bytes(data[20:24], "big")
    assert (width, height) == (EXPECTED_WIDTH, EXPECTED_HEIGHT), (
        f"entry.png dimensions changed: {width}x{height}"
    )

    shutil.copyfile(src, dst)
    with open(dst, "rb") as f:
        assert hashlib.sha256(f.read()).hexdigest() == EXPECTED_SHA256


if __name__ == "__main__":
    main()
