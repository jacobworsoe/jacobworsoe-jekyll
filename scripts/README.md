# Export scripts (MySQL)

Content is exported from the **WordPress MySQL database** (until WP is taken down), not from the live site URL.

## Credentials

Create **`scripts/.mysql-credentials`** (gitignored), e.g.:

```
MySQL hostnavn: your-host
MySQL brugernavn: user
MySQL adgangskode: pass
Primær database: dbname
```

## Commands (from repo root)

```bash
pip install pymysql
python scripts/export_all.py
```

Or: `scripts/build.ps1` / `scripts/build.bat` (same as `export_all.py`).

- **`export_wp_posts_pages_mysql.py`** — `_posts/`, root pages, `_data/wordpress_settings.yml`, `_config.yml` permalink, rewrites media URLs to `assets/images/…` + Liquid.

### Static assets vs. embeds in the DB

WordPress may store **third-party image URLs** (e.g. Wistia video poster on Akamai) in `post_content`. Those are rewritten to **repo files** after each export via `_STATIC_IMAGE_OVERRIDES` in `export_wp_posts_pages_mysql.py` (function `rewrite_external_images_to_static_repo`). When you replace another embed with a file under `assets/images/`, add a regex + Liquid `relative_url` pair there so future `export_all.py` runs keep the Jekyll site self-hosted.
- **`export_wp_comments_mysql.py`** — `_data/comments.yml`.
- **`rewrite_markdown_off_wordpress.py`** — bulk-rewrite existing Markdown off `www.jacobworsoe.dk` (run after manual edits if needed).

## FTP: download referenced images only

Create **`scripts/.ftp-credentials`** (gitignored), one line:

`host user password`

Example host: `linux12.unoeuro.com`. Paths in posts are `/assets/images/YYYY/MM/file.ext`; the script fetches from `public_html/wp-content/uploads/YYYY/MM/file.ext`.

```bash
python scripts/download_referenced_images_ftp.py
python scripts/download_referenced_images_ftp.py --favicon
```

Legacy Node/REST export scripts are not used for this project.
