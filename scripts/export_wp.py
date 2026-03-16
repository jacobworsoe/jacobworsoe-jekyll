#!/usr/bin/env python3
"""
Export WordPress posts, pages, and comments to Jekyll via REST API.
Usage: python export_wp.py [--url=https://www.jacobworsoe.dk] [--no-pages]
"""
import json
import re
import sys
import urllib.request
from pathlib import Path

BASE_URL = "https://www.jacobworsoe.dk"
INCLUDE_PAGES = True
PER_PAGE = 100

def parse_args():
    global BASE_URL, INCLUDE_PAGES
    for a in sys.argv[1:]:
        if a.startswith("--url="):
            BASE_URL = a.split("=", 1)[1].rstrip("/")
        elif a == "--no-pages":
            INCLUDE_PAGES = False

def fetch_json(url):
    req = urllib.request.Request(url, headers={"User-Agent": "Jekyll-Export/1.0"})
    with urllib.request.urlopen(req) as r:
        return json.loads(r.read().decode())

def fetch_all(endpoint, params=None):
    params = params or {}
    params.setdefault("per_page", PER_PAGE)
    all_items = []
    page = 1
    while True:
        params["page"] = page
        q = "&".join(f"{k}={v}" for k, v in params.items())
        url = f"{BASE_URL}/wp-json/wp/v2/{endpoint}?{q}"
        try:
            data = fetch_json(url)
        except urllib.error.HTTPError as e:
            if e.code == 400 and page > 1:
                break
            raise
        if not data:
            break
        all_items.extend(data)
        if len(data) < PER_PAGE:
            break
        page += 1
    return all_items

def escape_yaml(s):
    if s is None:
        return ""
    s = str(s)
    if "\n" in s or '"' in s or ":" in s or "#" in s:
        return '"' + s.replace("\\", "\\\\").replace('"', '\\"') + '"'
    return s

def slugify(s):
    return re.sub(r"[^a-z0-9]+", "-", (s or "").lower()).strip("-")

def wp_date_to_jekyll(d):
    if not d:
        return ""
    # 2024-12-13T15:04:45 -> 2024-12-13 15:04:45 +0000
    return d.replace("T", " ").rstrip("Z") + " +0000" if d.endswith("Z") else d.replace("T", " ")

def md_from_post(post, is_page, category_names):
    date = post.get("date", "")
    ymd = date[:10] if date else "2020-01-01"
    slug = (post.get("slug") or slugify(post.get("title", {}).get("rendered", "")) or "post").lstrip("0123456789-")
    title = (post.get("title") or {}).get("rendered", "").replace('"', '\\"')
    content = (post.get("content") or {}).get("rendered", "")
    content = re.sub(r"\r\n", "\n", content)
    content = re.sub(r"<!-- /?wp:.*?-->", "", content)
    cat_ids = post.get("categories") or []
    categories = [category_names.get(c, str(c)) for c in cat_ids if category_names.get(c)]
    layout = "page" if is_page else "post"
    fm = [
        "---",
        f"layout: {layout}",
        f"title: {escape_yaml(title)}",
        f"date: {wp_date_to_jekyll(date)}",
        f"slug: {slug}",
    ]
    if categories:
        fm.append("categories:")
        for c in categories:
            fm.append(f"  - {escape_yaml(c)}")
    fm.append("---")
    return "\n".join(fm) + "\n\n" + content + "\n"

def main():
    parse_args()
    script_dir = Path(__file__).resolve().parent
    repo_root = script_dir.parent
    posts_dir = repo_root / "_posts"
    data_dir = repo_root / "_data"
    posts_dir.mkdir(exist_ok=True)
    data_dir.mkdir(exist_ok=True)

    api_base = f"{BASE_URL}/wp-json/wp/v2"
    print("Fetching categories...")
    cats = fetch_all("categories")
    category_names = {c["id"]: c.get("name") or c.get("slug", "") for c in cats}

    print("Fetching posts...")
    posts = fetch_all("posts", {"_embed": "1"})
    print(f"Fetched {len(posts)} posts")

    for post in posts:
        date = post.get("date", "2020-01-01")
        ymd = date[:10]
        slug = (post.get("slug") or slugify((post.get("title") or {}).get("rendered", "")) or "post").lstrip("0123456789-")
        filename = f"{ymd}-{slug}.md"
        filepath = posts_dir / filename
        body = md_from_post(post, False, category_names)
        filepath.write_text(body, encoding="utf-8")
        print("Wrote", filename)

    if INCLUDE_PAGES:
        print("Fetching pages...")
        pages = fetch_all("pages")
        print(f"Fetched {len(pages)} pages")
        skip_slugs = {"index", "sitemap"}
        for page in pages:
            slug = page.get("slug") or slugify((page.get("title") or {}).get("rendered", "page"))
            if slug in skip_slugs:
                print("Skip page (reserved):", slug)
                continue
            filename = f"{slug}.md"
            filepath = repo_root / filename
            body = md_from_post(page, True, category_names)
            filepath.write_text(body, encoding="utf-8")
            print("Wrote page", filename)

    print("Fetching comments...")
    comments = fetch_all("comments")
    print(f"Fetched {len(comments)} comments")
    # Use same slug as in post front matter (stripped) so site.data.comments[page.slug] matches
    def post_slug(p):
        s = p.get("slug") or slugify((p.get("title") or {}).get("rendered", "")) or "post"
        return s.lstrip("0123456789-")
    id_to_slug = {p["id"]: post_slug(p) for p in posts}

    def format_comment_date(date_str):
        if not date_str:
            return ""
        from datetime import datetime
        try:
            d = datetime.fromisoformat(date_str.replace("Z", "+00:00"))
            return d.strftime("%d/%m-%Y - %H:%M")
        except Exception:
            return date_str[:16]

    by_slug = {}
    for c in comments:
        post_id = c.get("post")
        slug = id_to_slug.get(post_id)
        if not slug:
            continue
        if slug not in by_slug:
            by_slug[slug] = []
        content = (c.get("content") or {}).get("rendered", "")
        content = re.sub(r"<[^>]+>", " ", content)
        content = re.sub(r"\s+", " ", content).strip()
        by_slug[slug].append({
            "author": c.get("author_name", ""),
            "date": format_comment_date(c.get("date", "")),
            "content": content,
            "avatar_url": (c.get("author_avatar_urls") or {}).get("96") or (c.get("author_avatar_urls") or {}).get("48", ""),
            "author_url": c.get("author_url", ""),
        })

    lines = ["# WordPress comments (keyed by post slug)", ""]
    for slug in sorted(by_slug.keys()):
        lines.append(f"{slug}:")
        for item in by_slug[slug]:
            lines.append(f"  - author: {escape_yaml(item['author'])}")
            lines.append(f"    date: {escape_yaml(item['date'])}")
            lines.append(f"    content: {escape_yaml(item['content'])}")
            lines.append(f"    avatar_url: {escape_yaml(item['avatar_url'])}")
            lines.append(f"    author_url: {escape_yaml(item['author_url'])}")
        lines.append("")
    comments_path = data_dir / "comments.yml"
    comments_path.write_text("\n".join(lines), encoding="utf-8")
    print("Wrote", comments_path)
    print("Done.")

if __name__ == "__main__":
    main()
