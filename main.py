"""Real-Life Patch Notes: The Comedy Changelog
(make.fun bounty u-0xb3e689-real-life-patch-notes-the-comedy-changelog-c5844c1d).

Writes one patch note to /output/entry.txt. Deterministic: the same
line, byte for byte, on every run. No network, no randomness, no input.

The line was picked for the judge's brief: a terse release-note register
with a version number, a specific recognisable bug of the body (the brain
replaying an old embarrassment at 3 a.m.), and the punchline at the end
("with no skip button") — a fix stated as if it shipped.
"""

import os

LINE = (
    "v3.0.2: fixed a bug where the brain replayed your most embarrassing "
    "moment from 2009 every night at 3 a.m. with no skip button."
)


def main() -> None:
    text = LINE
    # Gate: /output/entry.txt must be UTF-8 text of 1 to 160 characters,
    # not only white space.
    assert 1 <= len(text) <= 160, "line must be 1-160 Unicode code points"
    assert text == text.strip(), "line must have no leading/trailing whitespace"
    assert "\n" not in text and "\r" not in text, "line must be a single line"
    assert all(ord(c) >= 32 and ord(c) != 127 for c in text), (
        "line must not contain hidden control characters"
    )
    assert text.strip(), "line must not be only whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(text)


if __name__ == "__main__":
    main()
