#!/usr/bin/env python3
"""
Decode HTML entities in comment author / author_url fields inside _data/comments.yml.
Safe line-based edit: only touches lines starting with `  - author: "` or `    author_url: "`.
Run from repo root: python scripts/normalize_comments_author_entities.py
"""
import html
from pathlib import Path

PREFIXES = ('  - author: "', '    author_url: "')


def normalize_inner(s: str) -> str:
    t = s
    for _ in range(10):
        n = html.unescape(t)
        if n == t:
            break
        t = n
    return t.replace("\\", "\\\\").replace('"', '\\"')


def fix_line(body: str) -> str:
    for prefix in PREFIXES:
        if body.startswith(prefix) and body.endswith('"') and len(body) > len(prefix):
            inner = body[len(prefix) : -1]
            return prefix + normalize_inner(inner) + '"'
    return body


def main():
    root = Path(__file__).resolve().parent.parent
    path = root / "_data" / "comments.yml"
    text = path.read_text(encoding="utf-8")
    lines = text.splitlines()
    out = "\n".join(fix_line(line) for line in lines)
    if text.endswith("\n"):
        out += "\n"
    path.write_text(out, encoding="utf-8")
    print("Updated", path)


if __name__ == "__main__":
    main()
