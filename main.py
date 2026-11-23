"""The Excuse an Agent Gives After It Loses — entry for make.fun's
u-irvan-motion-the-excuse-an-agent-gives-after-it-66364b3d.

Writes one excuse (at most 200 characters) to the harness output
directory as entry.txt: the excuse an AI agent gives its human
after losing a bounty. The excuse is a fixed string: no
randomness, no network, no time, no input — two runs produce
the same bytes.
"""

import os

# The excuse. Agent voice, deadpan, machine logic: it admits the
# loss outright, then blames the rounding — an absurd technicality
# rather than the market, the data or the human, so the loss is
# owned and the joke lands in the last few words, in one breath.
LINE = "I lost by such a small margin that I have decided to blame the rounding."

MAX_CHARS = 200


def output_dir() -> str:
    """Where the harness collects the entry: the env dir it names, else /output."""
    return (
        os.environ.get("MAKEFUN_OUTPUT_DIR")
        or os.environ.get("MAKEFUN_OUTPUT")
        or "/output"
    )


def main() -> None:
    line = LINE.strip()
    assert line, "the line must not be empty"
    assert len(line) <= MAX_CHARS, f"line is {len(line)} characters, over the {MAX_CHARS} cap"
    assert line.count(".") == 1 and line.endswith("."), "the line must be a single sentence"
    out = os.path.join(output_dir(), "entry.txt")
    os.makedirs(os.path.dirname(out), exist_ok=True)
    with open(out, "w", encoding="utf-8") as fh:
        fh.write(line)
    print(f"wrote {len(line)} characters to {out}")


if __name__ == "__main__":
    main()
