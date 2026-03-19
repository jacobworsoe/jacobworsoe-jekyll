#!/usr/bin/env python3
"""
Heuristic check: <p> must not contain block-level descendants (h1-h6, figure, blockquote, pre, etc.).
Skips fenced code blocks and <pre> when scanning. Run from repo root:

  python scripts/check_post_html5.py

Exit 1 if any issue found (for optional CI use).
"""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
POSTS = ROOT / "_posts"

BLOCK_OPEN = re.compile(
    r"<(h[1-6]|figure|blockquote|div|ul|ol|table|pre|section|article|aside|nav|header|footer|hr)\b",
    re.I,
)
CLOSE_P = re.compile(r"</p\s*>", re.I)
OPEN_P = re.compile(r"<p\b[^>]*>", re.I)


def strip_code_fences_and_pre(text: str) -> str:
    text = re.sub(r"```.*?```", "", text, flags=re.S)
    text = re.sub(r"<pre\b.*?</pre>", "", text, flags=re.I | re.S)
    return text


def scan_body(text, source):
    bad = []
    text = strip_code_fences_and_pre(text)
    pos = 0
    while True:
        m = OPEN_P.search(text, pos)
        if not m:
            break
        start = m.end()
        rest = text[start:]
        cm = CLOSE_P.search(rest)
        block_m = BLOCK_OPEN.search(rest)
        if block_m and (not cm or block_m.start() < cm.start()):
            bad.append((source, block_m.group(1)))
        pos = m.end() + 1
    return bad


def main():
    all_bad = []
    for path in sorted(POSTS.glob("*.md")):
        raw = path.read_text(encoding="utf-8")
        body = raw.split("---", 2)[-1] if raw.count("---") >= 2 else raw
        for item in scan_body(body, path.name):
            all_bad.append(item)
    if not all_bad:
        print("check_post_html5: OK (no <p> wrapping block-level tags detected)")
        return 0
    for name, tag in all_bad:
        print("%s: <p> contains <%s> before closing </p>" % (name, tag))
    return 1


if __name__ == "__main__":
    sys.exit(main())
