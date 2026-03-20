#!/usr/bin/env python3
"""
Export WordPress comments from MySQL to Jekyll _data/comments.yml.
Uses shared credentials from wp_mysql_credentials (scripts/.mysql-credentials, gitignored).
Usage: python scripts/export_wp_comments_mysql.py
"""
import re
from pathlib import Path

from wp_mysql_credentials import load_credentials

def escape_yaml_quoted(s):
    if s is None:
        return '""'
    s = str(s)
    return '"' + s.replace("\\", "\\\\").replace('"', '\\"').replace("\n", "\\n") + '"'

def main():
    creds = load_credentials()
    try:
        import pymysql
    except ImportError:
        raise SystemExit("Install pymysql: pip install pymysql")

    conn = pymysql.connect(
        host=creds["host"],
        port=creds.get("port", 3306),
        user=creds["user"],
        password=creds["password"],
        database=creds["database"],
        charset="utf8mb4",
    )
    # Detect table prefix (wp_, wp_2_, etc.)
    with conn.cursor() as cur:
        cur.execute("SHOW TABLES")
        tables = [list(row)[0] for row in cur.fetchall()]
    posts_tables = [t for t in tables if "posts" in t.lower()]
    if not posts_tables:
        conn.close()
        raise SystemExit("No WordPress posts table found. Tables: %s" % ", ".join(tables[:20]))
    # e.g. wp_posts or wp_2_posts -> prefix wp_ or wp_2_
    table_prefix = posts_tables[0].rsplit("posts", 1)[0]
    # Get post_id -> post_name (slug) for published posts
    with conn.cursor() as cur:
        cur.execute(
            f"SELECT ID, post_name FROM {table_prefix}posts WHERE post_type = 'post' AND post_status = 'publish'"
        )
        id_to_slug = {row[0]: (row[1] or "").lstrip("0123456789-") for row in cur.fetchall()}
    # Get approved comments
    with conn.cursor() as cur:
        cur.execute(f"""
            SELECT comment_post_ID, comment_author, comment_author_email, comment_author_url,
                   comment_date, comment_content
            FROM {table_prefix}comments
            WHERE comment_approved = '1'
            ORDER BY comment_post_ID, comment_ID
        """)
        rows = cur.fetchall()
    conn.close()

    by_slug = {}
    for r in rows:
        post_id, author, email, url, date, content = r
        slug = id_to_slug.get(post_id)
        if not slug:
            continue
        if slug not in by_slug:
            by_slug[slug] = []
        content = (content or "").strip()
        content = re.sub(r"<[^>]+>", " ", content)
        content = re.sub(r"\s+", " ", content).strip()
        # date: 2014-01-09 11:02:00 -> 09/01-2014 - 11:02
        date_str = str(date) if date else ""
        if date_str and len(date_str) >= 16:
            parts = date_str.replace("T", " ").split()
            ymd = parts[0].split("-") if len(parts[0]) >= 10 else ["", "", ""]
            hms = parts[1].split(":") if len(parts) > 1 and len(parts[1]) >= 5 else ["0", "0"]
            if len(ymd) == 3 and len(hms) >= 2:
                date_str = f"{ymd[2]}/{ymd[1]}-{ymd[0]} - {hms[0]}:{hms[1]}"
        # Gravatar from email
        if email:
            import hashlib
            avatar = f"https://www.gravatar.com/avatar/{hashlib.md5(email.strip().lower().encode()).hexdigest()}?s=96&d=mm&r=g"
        else:
            avatar = ""
        by_slug[slug].append({
            "author": author or "",
            "date": date_str,
            "content": content,
            "avatar_url": avatar,
            "author_url": (url or "").strip(),
        })

    repo_root = Path(__file__).resolve().parent.parent
    out_path = repo_root / "_data" / "comments.yml"
    out_path.parent.mkdir(parents=True, exist_ok=True)
    lines = ["# WordPress comments from MySQL export", ""]
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
    print("Wrote", out_path, "(%d posts with comments, %d total comments)" % (len(by_slug), sum(len(v) for v in by_slug.values())))

if __name__ == "__main__":
    main()
