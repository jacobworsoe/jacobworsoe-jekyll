#!/usr/bin/env python3
"""
Build _data/comments.yml from jekyll-import WordPress output.
Run after: cd tmp_wp_import && bundle exec jekyll import wordpress ...
Reads tmp_wp_import/_posts/*.html (YAML front matter with comments), writes repo _data/comments.yml.
"""
import re
import os
from pathlib import Path

try:
    import yaml
except ImportError:
    yaml = None

def escape_yaml_quoted(s):
    if s is None:
        return '""'
    s = str(s)
    return '"' + s.replace("\\", "\\\\").replace('"', '\\"').replace("\n", "\\n") + '"'

def slug_from_filename(name):
    # 2014-01-09-post-slug.html -> post-slug
    m = re.match(r"\d{4}-\d{2}-\d{2}-(.+)\.(html|md)$", name, re.I)
    return m.group(1) if m else name

def format_date(d):
    if not d:
        return ""
    # "2014-01-09 11:02:00" or "2014-01-09 11:02:00 UTC" -> "09/01-2014 - 11:02"
    s = str(d).strip()
    s = s.replace(" UTC", "").replace(" +0000", "")
    parts = s.split()
    if len(parts) >= 1:
        date_part = parts[0]  # 2014-01-09
        time_part = parts[1] if len(parts) >= 2 else "00:00:00"
        ymd = date_part.split("-")
        if len(ymd) == 3:
            day, month, year = ymd[2], ymd[1], ymd[0]
            hms = time_part.split(":")
            h, m = (hms[0], hms[1]) if len(hms) >= 2 else ("00", "00")
            return f"{day}/{month}-{year} - {h}:{m}"
    return s[:16]

def gravatar_url(email):
    if not email or not email.strip():
        return ""
    import hashlib
    h = hashlib.md5(email.strip().lower().encode()).hexdigest()
    return f"https://www.gravatar.com/avatar/{h}?s=96&d=mm&r=g"

def main():
    repo_root = Path(__file__).resolve().parent.parent
    posts_dir = repo_root / "tmp_wp_import" / "_posts"
    out_path = repo_root / "_data" / "comments.yml"
    if not posts_dir.exists():
        print("Run first: cd tmp_wp_import && bundle install && bundle exec jekyll import wordpress ...")
        return 1
    by_slug = {}
    for f in sorted(posts_dir.iterdir()):
        if f.suffix.lower() not in (".html", ".md"):
            continue
        slug = slug_from_filename(f.name)
        text = f.read_text(encoding="utf-8", errors="replace")
        if not text.startswith("---"):
            continue
        parts = text.split("---", 2)
        if len(parts) < 3:
            continue
        try:
            fm = yaml.safe_load(parts[1]) if yaml else None
        except Exception:
            continue
        if not fm or "comments" not in fm or not fm["comments"]:
            continue
        by_slug[slug] = []
        for c in fm["comments"]:
            author = c.get("author") or ""
            email = c.get("author_email") or ""
            url = c.get("author_url") or ""
            date = format_date(c.get("date") or c.get("date_gmt"))
            content = (c.get("content") or "").strip()
            content = re.sub(r"<[^>]+>", " ", content)
            content = re.sub(r"\s+", " ", content).strip()
            by_slug[slug].append({
                "author": author,
                "date": date,
                "content": content,
                "avatar_url": gravatar_url(email),
                "author_url": url,
            })
    out_path.parent.mkdir(parents=True, exist_ok=True)
    lines = ["# WordPress comments from jekyll-import (keyed by post slug)", ""]
    for slug in sorted(by_slug.keys()):
        lines.append(f"{slug}:")
        for item in by_slug[slug]:
            lines.append(f"  - author: {escape_yaml_quoted(item['author'])}")
            lines.append(f"    date: {escape_yaml_quoted(item['date'])}")
            lines.append(f"    content: {escape_yaml_quoted(item['content'])}")
            lines.append(f"    avatar_url: {escape_yaml_quoted(item['avatar_url'])}")
            lines.append(f"    author_url: {escape_yaml_quoted(item['author_url'])}")
        lines.append("")
    out_path.write_text("\n".join(lines), encoding="utf-8")
    print("Wrote", out_path)
    return 0

if __name__ == "__main__":
    if not yaml:
        print("Install PyYAML: pip install pyyaml")
        exit(1)
    exit(main())
