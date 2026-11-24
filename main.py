#!/usr/bin/env python3
"""One Word From Your Ex — make.fun program entry.

Competition: u-brave-eagle-12-one-word-from-your-ex-cfd97ba2.

The entry is exactly one word, the word an ex would use to describe
you, and nothing else. This program holds the approved word, checks
it against the gate (UTF-8 text, 1 to 24 characters, one word, not
only whitespace), writes it to entry.txt, reads the file back and
proves the bytes on disk are the word it approved.

Revision (second message): added --show, which prints the approved
word with its length and the gate, without writing anything, so the
entry can be inspected before a run.
"""

import re
import sys

WORD = "disaster"
MIN_LEN, MAX_LEN = 1, 24
ONE_WORD = re.compile(r"^\S+$")


def check(word):
    if not isinstance(word, str):
        raise ValueError("entry is not text")
    if not MIN_LEN <= len(word) <= MAX_LEN:
        raise ValueError("entry is %d characters, gate is %d-%d"
                         % (len(word), MIN_LEN, MAX_LEN))
    if word.strip() == "":
        raise ValueError("entry is only whitespace")
    if not ONE_WORD.match(word):
        raise ValueError("entry is not a single word")
    if "\n" in word or "\r" in word:
        raise ValueError("entry spans more than one line")


def publish(word, path="entry.txt"):
    with open(path, "w", encoding="utf-8", newline="") as fh:
        fh.write(word)
    with open(path, "r", encoding="utf-8") as fh:
        if fh.read() != word:
            raise IOError("%s does not hold the approved word" % path)


def main(argv):
    if len(argv) > 1 and argv[1] == "--show":
        print("%s (%d characters, gate %d-%d)" % (WORD, len(WORD), MIN_LEN, MAX_LEN))
        return 0
    check(WORD)
    publish(WORD)
    print("wrote entry.txt: %r, %d characters, %d bytes"
          % (WORD, len(WORD), len(WORD.encode("utf-8"))))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
