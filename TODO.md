# Handover Note — Next Session

*Last updated: end of session (before closing).*

---

## Summary: What we accomplished today

- **WordPress → Jekyll migration (content & URLs)**  
  - Posts and pages are exported from **MySQL** (not the REST API) via `scripts/export_wp_posts_pages_mysql.py`.  
  - Comments exported from MySQL with `scripts/export_wp_comments_mysql.py` → `_data/comments.yml`.  
  - **Permalink** is driven by WordPress: we read `permalink_structure` from `wp_options` and set Jekyll’s `permalink` in `_config.yml`. Current WordPress setting is **Post name only** (`/%postname%/`), so Jekyll uses **`permalink: /:title/`** (e.g. `/kan-browser-fingerprinting-erstatte-cookies/`).

- **WordPress settings export**  
  - Script fetches `permalink_structure`, `blogname`, `siteurl`, `home`, `category_base`, `tag_base`, etc. from `wp_options` and writes **`_data/wordpress_settings.yml`**.  
  - Same script updates **`_config.yml`** permalink from `permalink_structure` (via `wp_permalink_to_jekyll()`).

- **Alignment with WordPress site (www.jacobworsoe.dk)**  
  - Footer: “Senior Director, Measurement hos s360” + “Analytics ninja og datanørd”.  
  - Danish date format (e.g. `11. jan 2022`) via **`_includes/date-da.html`** on home, category, and post layouts.  
  - Homepage title set to WordPress-style tagline in **`index.md`**.  
  - **dataLayer / product data**: price = word count (from `content | number_of_words` at build time); product id uses `wordpress_id` from front matter when present (set by MySQL export).  
  - **`wordpress_id`** is written into post front matter by the export script so GA product IDs match WordPress.

- **Assets (Grunt / CSS/JS)**  
  - Switched from Ruby Sass to **Dart Sass** (`grunt-sass` + `sass` npm package); no Ruby needed for CSS build.  
  - Single CSS bundle: **`assets/css/main.css`** from **`scss/main-bundle.sass`**; all pages reference it.  
  - **Cache busting** and **preload** for CSS, **defer** for JS in **`_includes/head.html`** and **`_includes/footer.html`**.  
  - JS/CSS cleanup: null checks in JS, removed unused CSS (e.g. `_jetpack`, comment form styles), fixed drinksberegner bug.

- **Build & deploy**  
  - **`scripts/build.ps1`** / **`scripts/build.bat`** run MySQL export (posts+pages, then comments) only; Jekyll build runs on **GitHub Actions** after push.  
  - Workflow: Node 24 for actions, Node 20 for npm; single “Build” step that tees to **`jekyll-build.log`**; log upload on failure with `continue-on-error: true`.

- **Docs**  
  - **`docs/CRAWL-COMPARISON.md`** compares WordPress vs Jekyll (title, dates, footer, URLs).  
  - Duplicate `<title>` fixed (only **jekyll-seo-tag** outputs title).

- **Commit & push**  
  - See git history for latest. Migration and legacy cleanup (shared credentials, docstrings, removed legacy SCSS, slide-up-box in bundle, docs updated) are in place.

---

## Current state: Mid-edit files / pending bugs

- **No known mid-edit files.** All changes were committed and pushed.  
- **No known bugs** in the code we touched.  
- **Images:** Post/page content still references **`https://www.jacobworsoe.dk/wp-content/uploads/...`**. Images have **not** been copied into the repo or rewritten; that’s planned for later (see “Next step” and “Context”).

---

## The “Next step”: First thing to do tomorrow

1. **Copy WordPress images into the Jekyll site and point content at them.**  
   - Get list of image URLs (crawl post/page HTML for `jacobworsoe.dk/wp-content/uploads/` or query `wp_posts` for `post_type = 'attachment'` and use `guid` / `_wp_attached_file`).  
   - Download into e.g. **`assets/images/`** (or **`uploads/`**) preserving path (e.g. `2022/01/…`).  
   - Run a one-off replace in **`_posts/*.md`** and root **`*.md`** pages:  
     `https://www.jacobworsoe.dk/wp-content/uploads/` → `{{ site.baseurl }}/assets/images/` (or chosen path).  
   - Optional: add a small script under **`scripts/`** to do the download + replace so it’s repeatable.

2. **Optional follow-ups**  
   - Re-run **`python scripts/export_wp_posts_pages_mysql.py`** anytime you want to refresh content and permalink from WordPress.  
   - If WordPress permalink structure ever changes, the script will update **`_config.yml`** and **`_data/wordpress_settings.yml`** on next run.

---

## Context: Logic and gotchas

- **Permalink is from WordPress DB.**  
  We do **not** hardcode permalink in the repo long-term; the export script reads **`wp_options.permalink_structure`** and writes **`_config.yml`** + **`_data/wordpress_settings.yml`**. If someone edits **`_config.yml`** permalink by hand, it will be overwritten next time the export script runs.

- **Table prefix.**  
  All MySQL scripts **auto-detect** the WordPress table prefix (e.g. `wp_`, `wp_2_`) from tables whose name contains `posts`. No need to configure prefix in code.

- **Credentials.**  
  MySQL credentials live in **`scripts/.mysql-credentials`** (gitignored). Both export scripts use **`scripts/wp_mysql_credentials.py`** (`load_credentials()`). Format: `MySQL hostnavn:`, `MySQL brugernavn:`, `MySQL adgangskode:`, `Primær database:`.

- **Comments key.**  
  **`_data/comments.yml`** is keyed by **post slug** (same as in post front matter). The layout uses **`page.slug`** (and fallback from URL) to look up **`site.data.comments[slug]`**. With **`permalink: /:title/`**, the slug is the only path segment, so it still matches.

- **Product id in dataLayer.**  
  Use **`page.wordpress_id | default: page.id`** (and on list pages **`post.wordpress_id | default: post.id`**) so that after a MySQL export, GA sees the same numeric IDs as WordPress. Existing posts without **`wordpress_id`** keep using Jekyll’s id until the next export.

- **Images not in repo.**  
  All image URLs in content still point at **www.jacobworsoe.dk/wp-content/uploads/**. Until we download them and rewrite URLs, the Jekyll site will load images from the live WordPress site. Plan for “tomorrow” is to mirror those under **`assets/images/`** (or similar) and replace the base URL in Markdown.

- **Build script scope.**  
  **`scripts/build.ps1`** / **`.bat`** only run the **MySQL export** (posts+pages, then comments). They do **not** run `bundle exec jekyll build`; that happens in GitHub Actions after push. So no need for Ruby locally unless you want to build the site locally.

- **Single CSS file.**  
  **`assets/css/main.css`** is built from **`scss/main-bundle.sass`** (includes homepage, single, slide-up-box, highlight, tables, prism). Legacy **`homepage-bundle.sass`**, **`single-bundle.sass`**, and **`_jetpack.sass`** were removed.

---

*Use this file as the first context for the next session (e.g. “Read TODO.md and continue from the Next step”).*
