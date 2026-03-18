#!/usr/bin/env python3
"""
One-off / repeatable: replace WordPress-hosted URLs in Markdown with Jekyll relative_url.
Run from repo root: python scripts/rewrite_markdown_off_wordpress.py
"""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

_WP_MEDIA = re.compile(
    r"(?:https?:)?//www\.jacobworsoe\.dk/wp-content/uploads/([^\s\"\'<>\)]+)",
    re.IGNORECASE,
)

# Same-site HTML links (not uploads)
_SAME_SITE_ATTR = re.compile(
    r'(\b(?:href|src)=)(["\'])(?:https?:)?//www\.jacobworsoe\.dk(?!/wp-content)(/[^"\']*)\2',
    re.IGNORECASE,
)


def liquid_asset(path_under_uploads: str) -> str:
    full = "/assets/images/" + path_under_uploads.lstrip("/")
    return "{{ '" + full.replace("'", "\\'") + "' | relative_url }}"


def process_body(body: str) -> str:
    def up(m):
        return liquid_asset(m.group(1).strip())

    body = _WP_MEDIA.sub(up, body)

    def same(m):
        attr, q, path = m.group(1), m.group(2), m.group(3)
        if not path.startswith("/"):
            path = "/" + path
        liq = "{{ '" + path.replace("'", "\\'") + "' | relative_url }}"
        return "%s%s%s%s" % (attr, q, liq, q)

    body = _SAME_SITE_ATTR.sub(same, body)
    return body


def process_file(path: Path) -> bool:
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---"):
        new_body = process_body(text)
        if new_body == text:
            return False
        path.write_text(new_body, encoding="utf-8")
        return True
    parts = text.split("---", 2)
    if len(parts) < 3:
        return False
    fm, body = parts[1], parts[2]
    new_body = process_body(body)
    if new_body == body:
        return False
    path.write_text("---" + fm + "---" + new_body, encoding="utf-8")
    return True


def main():
    n = 0
    for p in (ROOT / "_posts").glob("*.md"):
        if process_file(p):
            n += 1
            print("updated", p.relative_to(ROOT))
    skip = {"README.md", "CHANGELOG.md", "TODO.md"}
    for p in ROOT.glob("*.md"):
        if p.name in skip:
            continue
        if process_file(p):
            n += 1
            print("updated", p.relative_to(ROOT))
    print("Done. %d files changed." % n)
    return 0


if __name__ == "__main__":
    sys.exit(main())
