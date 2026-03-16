#!/usr/bin/env python3
"""
Export WordPress posts and pages from MySQL to Jekyll.
Uses same DB and credentials as export_wp_comments_mysql.py.
Preserves WordPress URL structure: posts -> /:year/:month/:day/:title/ (slug = post_name),
pages -> /:slug/ (via root .md files). Requires _config.yml permalink: /:year/:month/:day/:title/
Reads credentials from scripts/.mysql-credentials (gitignored).
Usage: python scripts/export_wp_posts_pages_mysql.py
"""
import re
from pathlib import Path


def load_credentials():
    cred_path = Path(__file__).resolve().parent / ".mysql-credentials"
    if not cred_path.exists():
        raise SystemExit("Create scripts/.mysql-credentials with MySQL hostnavn, brugernavn, adgangskode, database.")
    lines = cred_path.read_text(encoding="utf-8").splitlines()
    creds = {}
    for line in lines:
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        if ":" in line:
            key, _, val = line.partition(":")
            key = key.strip().lower().replace(" ", "_")
            val = val.strip()
            if key == "mysql_hostnavn":
                creds["host"] = val
            elif key == "mysql_port":
                creds["port"] = int(val) if val.isdigit() else 3306
            elif key == "mysql_brugernavn":
                creds["user"] = val
            elif key == "mysql_adgangskode":
                creds["password"] = val
            elif key == "primær_database":
                creds["database"] = val
    if not creds.get("host") or not creds.get("user") or not creds.get("password") or not creds.get("database"):
        raise SystemExit(".mysql-credentials must contain MySQL hostnavn, brugernavn, adgangskode, Primær database.")
    creds.setdefault("port", 3306)
    return creds


def escape_liquid(content):
    """Escape Liquid delimiters so Jekyll doesn't interpret {{ }} or {% %} in body."""
    if not content:
        return ""
    # Order matters: escape longer sequences first
    content = content.replace("}}", "&#125;&#125;").replace("{{", "&#123;&#123;")
    content = content.replace("%}", "%&#125;").replace("{%", "&#123;%")
    return content


def escape_yaml(s):
    if s is None:
        return ""
    s = str(s)
    if "\n" in s or '"' in s or s.strip().startswith(("@", "#", "{", "[", "&", "*", "!", "|", ">", "'", "-")):
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

    # Published pages: post_title, post_name, post_content, post_date
    with conn.cursor() as cur:
        cur.execute(f"""
            SELECT post_title, post_name, post_content, post_date
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
        post_content = escape_liquid(post_content)

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
        post_title, post_name, post_content, post_date = row
        post_name = (post_name or "").strip().lstrip("0123456789-")
        if not post_name or post_name in skip_page_slugs:
            continue
        post_title = (post_title or "").strip()
        post_content = (post_content or "").replace("\r\n", "\n")
        post_content = escape_liquid(post_content)
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
