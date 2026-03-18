# Handover — jacobworsoe-jekyll

## Project rule (Cursor)

See **`.cursor/rules/jekyll-no-wordpress-hosting.mdc`**: the WordPress site will be taken down. The built Jekyll site must **not** load images, favicon, or other assets from the WordPress host. Use **`assets/images/…`** (mirroring old `wp-content/uploads/…`) and **`{{ '…' | relative_url }}`** in content/layouts.

## Migration doc

**`docs/MIGRATION.md`** — recommended pipeline if doing this again; how CI builds vs MySQL export.

## Export (MySQL, until cutover)

- **`python scripts/export_all.py`** — posts/pages + comments (or `build.ps1` / `build.bat`).
- **`scripts/rewrite_markdown_off_wordpress.py`** — rewrites remaining `www.jacobworsoe.dk/wp-content/uploads/` and same-site `href`/`src` in `_posts/*.md` and root `*.md` (skip hand-written docs).

## Next step: mirror uploads

1. Download files from former `wp-content/uploads/` into **`assets/images/`** (keep path after `uploads/`, e.g. `2022/01/file.jpg`). Use `scripts/download_referenced_images_ftp.py`.
2. Commit so images resolve at `{{ '/assets/images/…' | relative_url }}`.
3. Optional: script to download from attachment URLs in DB or a URL list.

## Build

- Local export only runs Python; **Jekyll** runs on **GitHub Actions** after push (`npm run build` + `bundle exec jekyll build`).

## Gotchas

- **Permalink** in `_config.yml` is overwritten when you run the posts export (from `wp_options.permalink_structure`).
- **YAML titles** with `:` must be quoted (export handles this).
- **`scripts/.mysql-credentials`** is gitignored.
