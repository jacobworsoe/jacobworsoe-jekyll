#!/usr/bin/env python3
"""
Export WordPress posts and pages from MySQL to Jekyll.
Reads wp_options (permalink_structure, blogname, siteurl, etc.) and writes _data/wordpress_settings.yml;
updates _config.yml permalink from permalink_structure so no manual permalink config is required.
Rewrites www.jacobworsoe.dk/wp-content/uploads/... to {{ '/assets/images/...' | relative_url }} (host files under assets/images/).
Uses shared credentials from wp_mysql_credentials (scripts/.mysql-credentials, gitignored).
Usage: python scripts/export_wp_posts_pages_mysql.py
"""
import base64
import re
from pathlib import Path

from wp_mysql_credentials import load_credentials


def escape_liquid(content):
    """Escape Liquid delimiters so Jekyll doesn't interpret {{ }} or {% %} in body."""
    if not content:
        return ""
    # Order matters: escape longer sequences first
    content = content.replace("}}", "&#125;&#125;").replace("{{", "&#123;&#123;")
    content = content.replace("%}", "%&#125;").replace("{%", "&#123;%")
    return content


def convert_wp_caption_shortcodes(content):
    """
    Convert WordPress [caption id="..." align="..." width="..."]...[/caption] to <figure>/<figcaption>.
    Inner content is typically: <a href="..."><img ... /></a> Caption text.
    Caption may contain its own <a>...</a>; use the first </a> (closes the image link), not rfind.
    """
    if not content:
        return content
    pattern = re.compile(r"\[caption[^\]]*\](.*?)\[/caption\]", re.DOTALL | re.IGNORECASE)

    def repl(m):
        inner = m.group(1).strip()
        caption = ""
        if "</a>" in inner:
            pos = inner.find("</a>")
            content_part = inner[: pos + len("</a>")]
            caption = inner[pos + len("</a>") :].strip()
        elif "/>" in inner:
            last_self = inner.rfind("/>")
            content_part = inner[: last_self + 2]
            caption = inner[last_self + 2 :].strip()
        else:
            content_part = inner
        if caption:
            return "<figure>%s<figcaption>%s</figcaption></figure>" % (content_part, caption)
        return "<figure>%s</figure>" % content_part

    out = pattern.sub(repl, content)
    # Avoid <p><figure>...</figure></p> (invalid HTML): unwrap lone figure from p
    out = re.sub(r"<p>\s*<figure>", "<figure>", out, flags=re.IGNORECASE)
    out = re.sub(r"</figure>\s*</p>", "</figure>", out, flags=re.IGNORECASE)
    return out


# WordPress uploads → Jekyll assets (no runtime dependency on WP host). Tokens survive escape_liquid.
_WP_UPLOADS = re.compile(
    r"(?:https?:)?//www\.jacobworsoe\.dk/wp-content/uploads/([^\s\"\'<>\)]+)",
    re.IGNORECASE,
)


def rewrite_wp_uploads_to_asset_tokens(content):
    if not content:
        return content

    def repl(m):
        rel = m.group(1).strip()
        b = base64.urlsafe_b64encode(rel.encode("utf-8")).decode("ascii").rstrip("=")
        return "__JAS__" + b + "__JAE__"

    return _WP_UPLOADS.sub(repl, content)


def finalize_jekyll_asset_tokens(content):
    if not content:
        return content

    def repl(m):
        b = m.group(1)
        pad = (4 - len(b) % 4) % 4
        path = base64.urlsafe_b64decode(b + "=" * pad).decode("utf-8")
        full = "/assets/images/" + path.lstrip("/")
        return "{{ '" + full.replace("'", "\\'") + "' | relative_url }}"

    return re.sub(r"__JAS__([A-Za-z0-9_-]+)__JAE__", repl, content)


def escape_yaml(s):
    if s is None:
        return ""
    s = str(s)
    # Quote if contains colon (YAML treats unquoted colon as key separator), newline, or special start
    if ":" in s or "\n" in s or '"' in s or s.strip().startswith(("@", "#", "{", "[", "&", "*", "!", "|", ">", "'", "-")):
        return '"' + s.replace("\\", "\\\\").replace('"', '\\"').replace("\n", "\\n") + '"'
    return s


def wp_permalink_to_jekyll(permalink_structure):
    """
    Convert WordPress permalink_structure to Jekyll permalink.
    E.g. /%postname%/ -> /:title/   or   /%year%/%monthnum%/%postname%/ -> /:year/:month/:title/
    """
    if not permalink_structure or not permalink_structure.strip():
        return "/:year/:month/:day/:title/"
    s = permalink_structure.strip().strip("/")
    # Map WP tags to Jekyll tokens
    s = s.replace("%year%", ":year").replace("%monthnum%", ":month").replace("%day%", ":day")
    s = s.replace("%postname%", ":title").replace("%post_id%", ":id").replace("%category%", ":categories")
    s = s.replace("%author%", ":author")
    if "%" in s or (":year" not in s and ":title" not in s):
        return "/:year/:month/:day/:title/"
    return "/" + s.strip("/") + "/"


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

    with conn.cursor() as cur:
        cur.execute("SHOW TABLES")
        tables = [list(row)[0] for row in cur.fetchall()]
    posts_tables = [t for t in tables if "posts" in t.lower()]
    if not posts_tables:
        conn.close()
        raise SystemExit("No WordPress posts table found. Tables: %s" % ", ".join(tables[:20]))
    table_prefix = posts_tables[0].rsplit("posts", 1)[0]

    # WordPress options (permalink_structure, siteurl, etc.)
    wp_settings = {}
    options_table = table_prefix + "options"
    if any(t == options_table for t in tables):
        with conn.cursor() as cur:
            cur.execute(f"""
                SELECT option_name, option_value FROM {options_table}
                WHERE option_name IN (
                    'permalink_structure', 'blogname', 'siteurl', 'home',
                    'category_base', 'tag_base', 'page_on_front', 'show_on_front'
                )
            """)
            for row in cur.fetchall():
                wp_settings[(row[0] or "").strip()] = (row[1] or "").strip()

    # Post ID -> category names (from term_relationships -> term_taxonomy -> terms)
    post_categories = {}
    term_tables = [t for t in tables if "term_taxonomy" in t.lower()]
    if term_tables:
        tt = table_prefix + "term_taxonomy"
        tr = table_prefix + "term_relationships"
        te = table_prefix + "terms"
        for t in (tt, tr, te):
            if not any(t == tbl for tbl in tables):
                break
        else:
            with conn.cursor() as cur:
                cur.execute(f"""
                    SELECT tr.object_id, te.name
                    FROM {tr} tr
                    JOIN {tt} tt ON tt.term_taxonomy_id = tr.term_taxonomy_id AND tt.taxonomy = 'category'
                    JOIN {te} te ON te.term_id = tt.term_id
                """)
                for row in cur.fetchall():
                    post_id, name = row[0], (row[1] or "").strip()
                    if name:
                        post_categories.setdefault(post_id, []).append(name)

    # Published posts: ID, post_date, post_title, post_name, post_content
    with conn.cursor() as cur:
        cur.execute(f"""
            SELECT ID, post_date, post_title, post_name, post_content
            FROM {table_prefix}posts
            WHERE post_type = 'post' AND post_status = 'publish'
            ORDER BY post_date
        """)
        posts = cur.fetchall()

    # Published pages: ID, post_title, post_name, post_content, post_date
    with conn.cursor() as cur:
        cur.execute(f"""
            SELECT ID, post_title, post_name, post_content, post_date
            FROM {table_prefix}posts
            WHERE post_type = 'page' AND post_status = 'publish'
            ORDER BY post_name
        """)
        pages = cur.fetchall()
    conn.close()

    repo_root = Path(__file__).resolve().parent.parent
    posts_dir = repo_root / "_posts"
    posts_dir.mkdir(parents=True, exist_ok=True)

    # Skip page slugs that would conflict with Jekyll/site
    skip_page_slugs = {"index", "sitemap", "feed", "feed.xml"}

    posts_written = 0
    for row in posts:
        post_id, post_date, post_title, post_name, post_content = row
        post_date = post_date or ""
        post_title = (post_title or "").strip()
        post_name = (post_name or "").strip().lstrip("0123456789-")
        if not post_name:
            post_name = "post-%s" % post_id
        post_content = (post_content or "").replace("\r\n", "\n")
        post_content = convert_wp_caption_shortcodes(post_content)
        post_content = rewrite_wp_uploads_to_asset_tokens(post_content)
        post_content = escape_liquid(post_content)
        post_content = finalize_jekyll_asset_tokens(post_content)

        # Jekyll post filename: YYYY-MM-DD-slug.md -> URL /:year/:month/:title/ = /YYYY/MM/slug/
        date_str = str(post_date)[:10] if post_date else "2020-01-01"
        safe_slug = re.sub(r"[^\w\-]", "-", post_name).strip("-") or "post"
        filename = f"{date_str}-{safe_slug}.md"
        categories = post_categories.get(post_id, [])
        date_fm = date_str
        if post_date and len(str(post_date)) >= 19:
            date_fm = str(post_date).replace("T", " ")[:19]

        lines = [
            "---",
            "layout: post",
            "title: %s" % escape_yaml(post_title),
            "date: %s" % date_fm,
            "slug: %s" % post_name,
            "wordpress_id: %s" % post_id,
        ]
        if categories:
            lines.append("categories:")
            for c in categories:
                lines.append("  - %s" % escape_yaml(c))
        lines.append("---")
        lines.append("")
        lines.append(post_content.strip())
        (posts_dir / filename).write_text("\n".join(lines), encoding="utf-8")
        posts_written += 1

    pages_written = 0
    for row in pages:
        page_id, post_title, post_name, post_content, post_date = row
        post_name = (post_name or "").strip().lstrip("0123456789-")
        if not post_name or post_name in skip_page_slugs:
            continue
        post_title = (post_title or "").strip()
        post_content = (post_content or "").replace("\r\n", "\n")
        post_content = convert_wp_caption_shortcodes(post_content)
        post_content = rewrite_wp_uploads_to_asset_tokens(post_content)
        post_content = escape_liquid(post_content)
        post_content = finalize_jekyll_asset_tokens(post_content)
        date_str = str(post_date)[:10] if post_date else ""
        date_fm = date_str
        if post_date and len(str(post_date)) >= 19:
            date_fm = str(post_date).replace("T", " ")[:19]

        lines = [
            "---",
            "layout: page",
            "title: %s" % escape_yaml(post_title),
            "date: %s" % date_fm,
            "slug: %s" % post_name,
            "wordpress_id: %s" % page_id,
            "---",
            "",
            post_content.strip(),
        ]
        out = repo_root / f"{post_name}.md"
        out.write_text("\n".join(lines), encoding="utf-8")
        pages_written += 1

    # Write WordPress settings to _data and update Jekyll _config.yml permalink
    data_dir = repo_root / "_data"
    data_dir.mkdir(parents=True, exist_ok=True)
    permalink_structure = wp_settings.get("permalink_structure", "")
    jekyll_permalink = wp_permalink_to_jekyll(permalink_structure)

    settings_lines = [
        "# Exported from WordPress wp_options (run export_wp_posts_pages_mysql.py to refresh)",
        "",
    ]
    for k, v in sorted(wp_settings.items()):
        if v:
            settings_lines.append("%s: %s" % (k, escape_yaml(v)))
    settings_lines.append("")
    settings_lines.append("# Derived Jekyll permalink (from permalink_structure)")
    settings_lines.append("jekyll_permalink: %s" % escape_yaml(jekyll_permalink.strip("/")))
    (data_dir / "wordpress_settings.yml").write_text("\n".join(settings_lines), encoding="utf-8")

    config_path = repo_root / "_config.yml"
    config_text = config_path.read_text(encoding="utf-8")
    # Replace permalink block: optional comment line + "permalink: ..."
    permalink_pattern = re.compile(
        r"^(\s*)#.*[Pp]ermalink.*\n\s*permalink:\s*[^\n]+",
        re.MULTILINE,
    )
    replacement = "# Match WordPress permalink_structure (from wp_options)\npermalink: %s" % jekyll_permalink
    if permalink_pattern.search(config_text):
        config_text = permalink_pattern.sub(replacement, config_text, count=1)
    else:
        # No comment+permalink block; replace single permalink: line
        config_text = re.sub(r"^(\s*)permalink:\s*[^\n]+", r"\1" + "permalink: %s" % jekyll_permalink, config_text, count=1, flags=re.MULTILINE)
        if "permalink:" not in config_text:
            config_text = config_text.replace("highlighter: rouge\n", "highlighter: rouge\n" + replacement + "\n")
    config_path.write_text(config_text, encoding="utf-8")

    print("Wrote %d posts to _posts/, %d pages to root." % (posts_written, pages_written))
    print("WordPress permalink_structure: %s -> Jekyll permalink: %s" % (repr(permalink_structure), jekyll_permalink))
    print("Settings saved to _data/wordpress_settings.yml, _config.yml updated.")


if __name__ == "__main__":
    main()
