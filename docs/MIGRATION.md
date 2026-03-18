# WordPress → Jekyll migration (reference)

## If doing it again (recommended order)

1. **Credentials** — One file (e.g. `scripts/.mysql-credentials`) + shared `scripts/wp_mysql_credentials.py`.
2. **Single export pipeline** — Read `wp_options` (permalink, site settings); export posts + pages with transforms (Liquid escape, `[caption]` → `<figure>`, **rewrite `wp-content/uploads` URLs** to `{{ '/assets/images/…' | relative_url }}`); export comments by slug; write `_data/wordpress_settings.yml` and update `_config.yml` permalink.
3. **No runtime dependency on WordPress** — Mirror all media under `assets/images/`; never link images/favicon to the WordPress host (see `.cursor/rules/jekyll-no-wordpress-hosting.mdc`).
4. **Layouts & assets** — One CSS bundle (`scss/main-bundle.sass` → `assets/css/main.css`); Dart Sass via Grunt.
5. **CI vs export** — **GitHub Actions**: `npm install` → `npm run build` → `bundle exec jekyll build` (no MySQL in CI). **Local**: `python scripts/export_all.py` (or `scripts/build.ps1`) when refreshing content from DB before commit.

## Scripts (this repo)

| Script | Role |
|--------|------|
| `export_all.py` | Runs posts/pages export then comments export. |
| `export_wp_posts_pages_mysql.py` | Posts, pages, settings, permalink, asset URL rewrite in body. |
| `export_wp_comments_mysql.py` | `_data/comments.yml`. |
| `rewrite_markdown_off_wordpress.py` | Bulk-rewrite existing Markdown off `www.jacobworsoe.dk` (uploads + same-site links). |

## Archived doc

`docs/archive/CRAWL-COMPARISON.md` — historical WordPress vs Jekyll checklist from migration.
