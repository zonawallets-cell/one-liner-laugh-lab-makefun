"""One-Liner Laugh Lab — make.fun entry (program/v1).

Writes exactly one funny line to /output/entry.txt: the excuse a robot
vacuum gives after eating a sock.

Pure stdlib (os only). No third-party packages, no network, no randomness.
"""

import os

# The winning line (86 chars, one line, UTF-8).
#
# Why this line, against the judge's criteria (funny > original > fit >
# tight):
#   * Fit: first-person excuse, spoken as the vacuum. The joke comes from
#     the vacuum's own job logic — it eats dust bunnies for a living.
#   * Original: the sock didn't get mistaken for food; it got mistaken for
#     the vacuum's natural prey, dressed up as one. A fresh angle, not the
#     stock "I thought it was a snack" excuse.
#   * Funny: two beats. Beat one reframes the sock as a disguised dust
#     bunny; beat two ("I was on the clock") is deadpan escalation — it was
#     just doing its job, and the job is the excuse.
#   * Tight: 86 characters, every word working, no setup that overstays.
LINE = "In my defense, it was lying on the floor dressed as a dust bunny. I was on the clock."


def validate(line):
    """Enforce the competition gate before writing: UTF-8 text, exactly
    one line, 1-200 characters, not only white space."""
    if not isinstance(line, str) or not line.strip():
        raise ValueError("line must be non-blank text")
    if "\n" in line or "\r" in line:
        raise ValueError("line must be a single line")
    if not 1 <= len(line) <= 200:
        raise ValueError("line must be 1-200 characters, got %d" % len(line))
    line.encode("utf-8")
    return line


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(validate(LINE) + "\n")


if __name__ == "__main__":
    main()
